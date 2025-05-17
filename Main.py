from hojasdevida import *
from reportes import *
from rich.console import Console

console = Console()

def mostrar_menu():
    console.print("\n[bold cyan]--- Menú Principal ---[/bold cyan]")
    print("1. Registrar hoja de vida")
    print("2. Consultar hojas de vida")
    print("3. Actualizar hoja de vida")
    print("4. Generar reportes")
    print("5. Exportar datos")
    print("6. Salir")

def main():
    hojas = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_hoja_de_vida(hojas)
        elif opcion == "2":
            consultar_hoja_de_vida(hojas)
        elif opcion == "3":
            actualizar_hoja_de_vida(hojas)
        elif opcion == "4":
            generar_reportes(hojas)
        elif opcion == "5":
            exportar_datos(hojas)
        elif opcion == "6":
            guardar_datos(hojas)
            console.print("[bold green]Saliendo del sistema. ¡Hasta pronto![/bold green]")
            break
        else:
            console.print("[bold red]Opción inválida. Intente de nuevo.[/bold red]")

if __name__ == "__main__":
    main()
