import unittest
from civil_date_interval_audit.core import run
class DomainTests(unittest.TestCase):
 def test_fall_25_hours(self):
  x=run({'zone':'Europe/Paris','start':'2026-10-25T00:00:00','end':'2026-10-26T00:00:00'});self.assertEqual(x['civil_seconds'],86400);self.assertEqual(x['elapsed_utc_seconds'],90000)
 def test_spring_23_hours(self):self.assertEqual(run({'zone':'Europe/Paris','start':'2026-03-29T00:00:00','end':'2026-03-30T00:00:00'})['elapsed_utc_seconds'],82800)
 def test_ambiguous_requires_fold(self):
  with self.assertRaises(ValueError):run({'zone':'Europe/Paris','start':'2026-10-25T02:30:00','end':'2026-10-25T04:00:00'})
