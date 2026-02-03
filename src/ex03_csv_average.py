"""
EX03 (CSV) · Calcular la media de una columna

Objetivo:
- Leer un CSV con cabecera (primera línea).
- Usar la librería estándar `csv` (recomendado: csv.DictReader).
- Convertir datos a float y calcular una media.

Ejemplo típico:
- Un CSV de calificaciones con columnas: name, average
"""

from __future__ import annotations

from pathlib import Path

import csv

def csv_average(path: str | Path, column: str) -> float:
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"El fichero no existe: {path}")
    with open(path_obj, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None or column not in reader.fieldnames:
            raise ValueError(f"La columna '{column}' no existe.")
        total = 0.0
        count = 0
        for row in reader:
            try:
                total += float(row[column])
                count += 1
            except (ValueError, TypeError):
                raise ValueError(f"Dato no numérico en la columna '{column}'.")
        if count == 0:
            raise ValueError("El CSV no tiene filas de datos.")
        return total / count
    
   
                

    """
    Calcula y devuelve la media de la columna numérica `column` en el CSV `path`.

    Reglas:
    - El CSV tiene cabecera.
    - `column` debe existir en la cabecera. Si no, ValueError.
    - Todos los valores de esa columna deben poder convertirse a float. Si no, ValueError.
    - Si no hay filas de datos (CSV vacío tras la cabecera), ValueError.
    - Si el fichero no existe, FileNotFoundError.

    Ejemplo:
    name,average
    Ana,10
    Luis,6

    csv_average(..., "average") -> 8.0
    """
    
