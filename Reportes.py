import csv
import json
from collections import Counter
from rich.console import Console
from tabulate import tabulate

console = Console()

def generar_reportes(hojas):
    console.print("\n[bold cyan]--- Generar Reportes ---[/bold cyan]")
    print("1. Listado con más de N años de experiencia")
    print("2. Candidatos con certificación específica")
    print("3. Habilidades más comunes")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        n = int(input("¿Cuántos años de experiencia mínimo?: "))
        tabla = []
        for hoja in hojas:
            total = calcular_total_experiencia(hoja)
            if total >= n:
                tabla.append([hoja['datos_personales']['nombre'], total])
        if tabla:
            console.print("[green]Resultados:[/green]")
            print(tabulate(tabla, headers=["Nombre", "Años de experiencia"], tablefmt="fancy_grid"))
        else:
            console.print("[red]No se encontraron candidatos con esa experiencia.[/red]")

    elif opcion == "2":
        cert = input("Ingrese habilidad o certificación: ").lower()
        encontrados = [h for h in hojas if cert in map(str.lower, h["habilidades"])]
        if encontrados:
            tabla = [[h["datos_personales"]["nombre"], ", ".join(h["habilidades"])] for h in encontrados]
            print(tabulate(tabla, headers=["Nombre", "Habilidades"], tablefmt="grid"))
        else:
            console.print(f"[red]No se encontraron candidatos con la certificación '{cert}'.[/red]")

    elif opcion == "3":
        todas = []
        for hoja in hojas:
            todas.extend(hoja["habilidades"])
        conteo = Counter(todas)
        if conteo:
            tabla = [[hab, cant] for hab, cant in conteo.most_common()]
            print(tabulate(tabla, headers=["Habilidad", "Cantidad"], tablefmt="github"))
        else:
            console.print("[red]No hay habilidades registradas aún.[/red]")

def calcular_total_experiencia(hoja):
    total = 0
    for exp in hoja.get("experiencia", []):
        try:
            inicio, fin = exp["duracion"].split("-")
            total += int(fin) - int(inicio)
        except Exception:
            continue
    return total

def exportar_datos(hojas):
    formato = input("Exportar en formato (json/csv/txt): ").lower()
    if formato == "json":
        with open("exportado.json", "w", encoding="utf-8") as file:
            json.dump(hojas, file, indent=2, ensure_ascii=False)
    elif formato == "csv":
        with open("exportado.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Correo", "Habilidades"])
            for h in hojas:
                writer.writerow([h["datos_personales"]["nombre"], h["datos_personales"]["correo"], ", ".join(h["habilidades"])])
    elif formato == "txt":
        with open("exportado.txt", "w", encoding="utf-8") as file:
            for h in hojas:
                file.write(f"Nombre: {h['datos_personales']['nombre']}\n")
                file.write(f"Correo: {h['datos_personales']['correo']}\n")
                file.write(f"Habilidades: {', '.join(h['habilidades'])}\n\n")
    else:
        console.print("[red]Formato no soportado.[/red]")
        return
    console.print(f"[green]Datos exportados correctamente a exportado.{formato}[/green]")
