"""Workit 1.0.0"""

import re
from modulo import conectar_bbdd, crear_tabla_base, agregar, consultar, borrar
# pylint: disable=broad-except, line-too-long

CONEXION = conectar_bbdd()
crear_tabla_base(CONEXION)

def validar_registro(ejercicio: str, peso: str, reps: str, series: str, fecha: str) -> bool:
    """Valida el input mediante expresiones regulares"""
    patrones_regex = {
        "letras": r"^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$",
        "numeros":  r"^\d+(\.\d+)?$",
        "fecha": r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    }

    if not re.match(patrones_regex["letras"], str(ejercicio)):
        print("❌ Input inválido para ejercicio, solo se admiten letras")
        return False
    if not re.match(patrones_regex["numeros"], str(peso)):
        print("❌ Input inválido para peso, solo se admiten números")
        return False
    if not re.match(patrones_regex["numeros"], str(reps)):
        print("❌ Input inválido para reps, solo se admiten números")
        return False
    if not re.match(patrones_regex["numeros"], str(series)):
        print("❌ Input inválido para series, solo se admiten números")
        return False
    if not re.match(patrones_regex["fecha"], str(fecha)):
        print("❌ Input inválido para fecha, solo se admite formato dd-mm-yyyy")
        return False

    return True

def agregar_registro(ejercicio: str, peso: str, reps: str, series: str, fecha: str) -> None:
    """Añade un registro"""

    if validar_registro(ejercicio, peso, reps, series, fecha):
        datos = (ejercicio, peso, reps, series, fecha)
        return agregar(CONEXION, datos)
    else:
        print("❌ Error al añadir registro: datos inválidos.")
        return None

def borrar_registro(id_borrar: int) -> None:
    """Elimina un registro"""
    return borrar(CONEXION, id_borrar)

def consultar_registros():
    """Consulta los registros en la base de datos"""
    return consultar(CONEXION)
