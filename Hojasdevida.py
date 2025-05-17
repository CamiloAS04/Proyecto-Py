import json

ARCHIVO = "datos.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_datos(hojas):
    with open(ARCHIVO, "w", encoding="utf-8") as file:
        json.dump(hojas, file, indent=2, ensure_ascii=False)

def registrar_hoja_de_vida(hojas):
    print("\n--- Registro de Hoja de Vida ---")
    datos = {
        "nombre": input("Nombre: "),
        "documento": input("Documento: "),
        "contacto": input("Teléfono: "),
        "direccion": input("Dirección: "),
        "correo": input("Correo: "),
        "fecha_nacimiento": input("Fecha de nacimiento (YYYY-MM-DD): ")
    }

    formacion = []
    while input("¿Agregar formación? (s/n): ").lower() == "s":
        formacion.append({
            "institucion": input("Institución: "),
            "titulo": input("Título: "),
            "años": input("Años (ej. 2010-2014): ")
        })

    experiencia = []
    while input("¿Agregar experiencia? (s/n): ").lower() == "s":
        experiencia.append({
            "empresa": input("Empresa: "),
            "cargo": input("Cargo: "),
            "funciones": input("Funciones: "),
            "duracion": input("Duración (ej. 2015-2019): ")
        })

    referencias = []
    while input("¿Agregar referencia? (s/n): ").lower() == "s":
        referencias.append({
            "nombre": input("Nombre: "),
            "relacion": input("Relación: "),
            "telefono": input("Teléfono: ")
        })

    habilidades = set()
    while input("¿Agregar habilidad o certificación? (s/n): ").lower() == "s":
        habilidades.add(input("Habilidad: "))

    hoja = {
        "datos_personales": datos,
        "formacion": formacion,
        "experiencia": experiencia,
        "referencias": referencias,
        "habilidades": list(habilidades)
    }

    hojas.append(hoja)
    print("Hoja de vida registrada con éxito.")

def consultar_hoja_de_vida(hojas):
    print("\n--- Consultar Hojas de Vida ---")
    criterio = input("Buscar por (nombre/documento/correo): ").lower()
    valor = input("Valor a buscar: ").lower()
    encontrados = []

    for hoja in hojas:
        campo = hoja["datos_personales"].get(criterio, "").lower()
        if campo == valor:
            encontrados.append(hoja)

    if encontrados:
        for h in encontrados:
            print(json.dumps(h, indent=2, ensure_ascii=False))
    else:
        print("No se encontraron resultados.")

def actualizar_hoja_de_vida(hojas):
    doc = input("Ingrese el documento de la persona a actualizar: ")
    for hoja in hojas:
        if hoja["datos_personales"]["documento"] == doc:
            print("1. Editar datos personales")
            print("2. Agregar experiencia")
            print("3. Agregar formación")
            print("4. Agregar habilidad")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                hoja["datos_personales"]["nombre"] = input("Nuevo nombre: ")
                hoja["datos_personales"]["contacto"] = input("Nuevo contacto: ")
                hoja["datos_personales"]["direccion"] = input("Nueva dirección: ")
                hoja["datos_personales"]["correo"] = input("Nuevo correo: ")

            elif opcion == "2":
                hoja["experiencia"].append({
                    "empresa": input("Empresa: "),
                    "cargo": input("Cargo: "),
                    "funciones": input("Funciones: "),
                    "duracion": input("Duración: ")
                })

            elif opcion == "3":
                hoja["formacion"].append({
                    "institucion": input("Institución: "),
                    "titulo": input("Título: "),
                    "años": input("Años: ")
                })

            elif opcion == "4":
                hoja["habilidades"].append(input("Habilidad: "))

            print("Información actualizada.")
            return

    print("Documento no encontrado.")
