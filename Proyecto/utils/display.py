from tabulate import tabulate

def mostrar_tabla_cv(cvs):
    if not cvs:
        print("⚠️  No hay hojas de vida registradas.")
        return

    tabla = []

    for cv in cvs.values():
        personales = cv["personales"]
        fila = [
            personales.get("nombre", ""),
            personales.get("documento", ""),
            personales.get("correo", ""),
            ", ".join(cv.get("habilidades", [])),
            len(cv.get("experiencia", []))
        ]
        tabla.append(fila)

    headers = ["Nombre", "Documento", "Correo", "Habilidades", "Experiencia"]
    print("\n📋 Hojas de Vida Registradas:\n")
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))

