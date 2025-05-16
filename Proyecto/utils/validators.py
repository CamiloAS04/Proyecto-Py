import re
from datetime import datetime

def validar_correo(correo):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, correo) is not None

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_existencia_cv(cvs, id_cv):
    return id_cv in cvs

def validar_documento(documento):
    return documento.isdigit()

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) >= 7
