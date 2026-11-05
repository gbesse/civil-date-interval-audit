# civil-date-interval-audit

## Français

Comparer durées civiles et durées UTC entre échéances.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m civil_date_interval_audit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Compare durée civile et durée UTC réelle en résolvant explicitement les heures ambiguës ; l’exemple d’automne montre25h pour un jour civil.

### Limites

TZdb du runtime, pas calendrier contractuel ou règle juridique. Identifiants de fuseaux non valides refusés ; aucune tâche planifiée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Compare civil and UTC durations between deadlines.

Synthetic data; no network access or secret required.

```sh
python -m civil_date_interval_audit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Compares civil duration and actual UTC elapsed duration with explicit ambiguous-time handling; autumn example shows25h for one civil day.

### Limits

Runtime TZdb, not a contractual calendar or legal rule. Invalid zone identifiers rejected; no task scheduling.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Comparar duraciones civiles y UTC entre vencimientos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m civil_date_interval_audit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Compara duración civil y duración UTC real resolviendo horas ambiguas explícitamente; ejemplo de otoño muestra25h para un día civil.

### Límites

TZdb del entorno, no calendario contractual ni regla jurídica. Rechaza zonas inválidas; no programa tareas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.python.org/3/library/zoneinfo.html
