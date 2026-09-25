#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Muestra TUS parámetros personales del Lab #6 (dependen de tu cédula y del código de sesión)."""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "autograde"))
import autograde as a  # noqa: E402

try:
    est = json.loads((RAIZ / "estudiante.json").read_text(encoding="utf-8"))
except (OSError, ValueError):
    sys.exit("Primero completa estudiante.json")
if not all(str(est.get(k, "")).strip() for k in ("nombre", "apellido", "cedula", "codigo_sesion")):
    sys.exit("Completa TODOS los campos de estudiante.json (nombre, apellido, cedula, codigo_sesion)")

p = a.perfil(est["cedula"], est["codigo_sesion"])
print(f"""

╔════════════════════════════════════════════════════════════╗
  TUS PARÁMETROS PERSONALES · René Mariscal
╚════════════════════════════════════════════════════════════╝
 1. Tema de tu página ............ Estación meteorológica
    (debe aparecer en el <title> y en el <h1>)
 2. id del elemento <main> ........ ficha-1565
 3. class del elemento <main> ..... k-68814a
 4. Color principal ............... #362097
    (úsalo en el CSS: títulos, bordes o fondos)
 5. Filas de datos en <tbody> ..... 6  (cada fila con 3 o más celdas)
 6. <meta name="author"> .......... René Mariscal
 7. <meta name="codigo-sesion"> ... LAB6-V9S3
 8. <footer> ...................... debe incluir tu nombre y apellido

Estos valores son SOLO tuyos. Un compañero tendrá otros distintos.
