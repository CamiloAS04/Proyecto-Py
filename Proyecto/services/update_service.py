from utils.validators import validar_existencia_cv

def actualizar_cv(cvs):
    print("\n--- Actualizar Hoja de Vida ---")
    id_cv = input("Ingrese ID del CV a actualizar (documento_fecha): ")

    if not validar_existencia_cv(cvs, id_cv):
        print("❌ CV no encontrado.")
        return

    cv = cvs[id_cv]

    print("¿Qué sección desea actualizar?")
    print("1. Datos personales")
    print("2. Formación académica")
    print("3. Experiencia profesional")
    print("4. Habilidades")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        telefono = input("Nuevo teléfono: ")
        direccion = input("Nueva dirección: ")
        correo = input("Nuevo correo: ")
        cv["personales"]["telefono"] = telefono
        cv["personales"]["direccion"] = direccion
        cv["personales"]["correo"] = correo
        print("✅ Datos personales actualizados.")
    elif opcion == "2":
        institucion = input("Institución educativa: ")
        titulo = input("Título obtenido: ")
        anios = input("Años cursados: ")
        nueva_formacion = {"institucion": institucion, "titulo": titulo, "anios": anios}
        cv["formacion"].append(nueva_formacion)
        print("✅ Formación añadida.")
    elif opcion == "3":
        empresa = input("Empresa: ")
        cargo = input("Cargo: ")
        funciones = input("Funciones: ")
        duracion = input("Duración (meses o años): ")
        nueva_exp = {"empresa": empresa, "cargo": cargo, "funciones": funciones, "duracion": duracion}
        cv["experiencia"].append(nueva_exp)
        print("✅ Experiencia añadida.")
    elif opcion == "4":
        nuevas = input("Ingrese habilidades separadas por coma: ").split(",")
        for habilidad in nuevas:
            cv["habilidades"].add(habilidad.strip().lower())
        print("✅ Habilidades actualizadas.")
    else:
        print("Opción inválida.")
