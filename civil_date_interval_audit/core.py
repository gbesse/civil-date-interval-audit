import json,math
from .common import number,integer,identifier
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
def resolve(text,zone,fold):
 x=datetime.fromisoformat(text)
 if x.tzinfo is not None:raise ValueError('naive_local_required')
 valid=[]
 for f in [0,1]:
  a=x.replace(tzinfo=zone,fold=f);u=a.astimezone(timezone.utc)
  if u.astimezone(zone).replace(tzinfo=None)==x and all(u!=v for v in valid):valid.append(u)
 if not valid:raise ValueError('nonexistent_local_time')
 if len(valid)>1 and fold is None:raise ValueError('ambiguous_local_time')
 if fold is not None:integer(fold,0,1)
 return x.replace(tzinfo=zone,fold=fold or 0)
def run(d):
 zone=ZoneInfo(identifier(d['zone']));a=resolve(d['start'],zone,d.get('start_fold'));b=resolve(d['end'],zone,d.get('end_fold'));civil=(b.replace(tzinfo=None)-a.replace(tzinfo=None)).total_seconds();elapsed=(b.astimezone(timezone.utc)-a.astimezone(timezone.utc)).total_seconds()
 if civil<0 or elapsed<0:raise ValueError('reverse_interval')
 return dict(civil_seconds=civil,elapsed_utc_seconds=elapsed,difference_seconds=elapsed-civil,start_utc=a.astimezone(timezone.utc).isoformat(),end_utc=b.astimezone(timezone.utc).isoformat(),zone=d['zone'],tzdb_source='runtime_zoneinfo')
