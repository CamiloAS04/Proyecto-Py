from services.report_service import generar_reporte
from utils.file_utils import guardar_cvs

def main():
    # Un diccionario de ejemplo de hojas de vida, en formato de prueba.
    cvs = {
        "12345678": {
            "personales": {
                "nombre": "Laura Martínez",
                "documento": "12345678",
                "correo": "laura@email.com",
                "nacimiento": "1990-05-23",
                "telefono": "3001234567",
                "direccion": "Calle 123 #45-67"
            },
            "habilidades": ["python", "liderazgo"],
            "experiencia": [
                {"empresa": "TechCorp", "cargo": "Desarrolladora", "funciones": "Desarrollo web", "duracion": "2 años"}
            ]
        }
    }
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar nueva hoja de vida")
        print("2. Consultar hojas de vida")
        print("3. Generar reportes")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Función para registrar CV (por completar)
            pass

        elif opcion == "2":
            # Consultar hojas de vida (por completar)
            pass

        elif opcion == "3":
            generar_reporte(cvs)

        elif opcion == "4":
            print("Hasta luego!")
            break

        else:
            print("Opción inválida.")
