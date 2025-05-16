from utils.display import mostrar_tabla_cv
from collections import Counter
from utils.file_utils import exportar_csv, exportar_txt, guardar_cvs

def generar_reporte(cvs):
    while True:
        print("\n--- Menú de Reportes ---")
        print("1. Ver tabla de hojas de vida")
        print("2. Ver habilidades más comunes")
        print("3. Exportar a JSON")
        print("4. Exportar a CSV")
        print("5. Exportar a TXT")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tabla_cv(cvs)

        elif opcion == "2":
            todas_habilidades = []
            for cv in cvs.values():
                todas_habilidades.extend(list(cv["habilidades"]))
            contador = Counter(todas_habilidades)
            print("\n--- Habilidades más comunes ---")
            for habilidad, cantidad in contador.most_common():
                print(f"{habilidad}: {cantidad} candidatos")

        elif opcion == "3":
            guardar_cvs(cvs)
            print("✅ Exportado a JSON en: data/cvs.json")

        elif opcion == "4":
            exportar_csv(cvs)

        elif opcion == "5":
            exportar_txt(cvs)

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")

