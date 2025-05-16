from datetime import datetime

def registrar_cv():
    print("\n--- Registro de Hoja de Vida ---")
    nombre = input("Nombre completo: ")
    documento = input("Documento de identidad: ")
    correo = input("Correo electrónico: ")
    nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    telefono = input("Teléfono de contacto: ")
    direccion = input("Dirección: ")

    id_cv = f"{documento}_{nacimiento}"

    cv = {
        "id": id_cv,
        "personales": {
            "nombre": nombre,
            "documento": documento,
            "correo": correo,
            "nacimiento": nacimiento,
            "telefono": telefono,
            "direccion": direccion
        },
        "formacion": [],
        "experiencia": [],
        "referencias": [],
        "habilidades": set()
    }

    return cv
