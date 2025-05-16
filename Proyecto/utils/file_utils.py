import csv
import os

def exportar_csv(cvs, archivo="data/exportado.csv"):
    campos = ["nombre", "documento", "correo", "nacimiento", "telefono", "direccion", "habilidades"]
    
    if not os.path.exists("data"):
        os.makedirs("data")
    
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        
        for cv in cvs.values():
            fila = {
                "nombre": cv["personales"]["nombre"],
                "documento": cv["personales"]["documento"],
                "correo": cv["personales"]["correo"],
                "nacimiento": cv["personales"]["nacimiento"],
                "telefono": cv["personales"]["telefono"],
                "direccion": cv["personales"]["direccion"],
                "habilidades": ", ".join(cv["habilidades"])
            }
            writer.writerow(fila)
    
    print(f"✅ Exportado a CSV: {archivo}")

def exportar_txt(cvs, archivo="data/exportado.txt"):
    if not os.path.exists("data"):
        os.makedirs("data")
    
    with open(archivo, "w", encoding="utf-8") as f:
        for cv in cvs.values():
            f.write(f"Nombre: {cv['personales']['nombre']}\n")
            f.write(f"Documento: {cv['personales']['documento']}\n")
            f.write(f"Correo: {cv['personales']['correo']}\n")
            f.write(f"Fecha Nacimiento: {cv['personales']['nacimiento']}\n")
            f.write(f"Teléfono: {cv['personales']['telefono']}\n")
            f.write(f"Dirección: {cv['personales']['direccion']}\n")
            f.write(f"Habilidades: {', '.join(cv['habilidades'])}\n")
            f.write("-" * 40 + "\n")
    
    print(f"✅ Exportado a TXT: {archivo}")

def guardar_cvs(cvs):
    with open("data/cvs.json", "w", encoding="utf-8") as f:
        import json
        json.dump(cvs, f, ensure_ascii=False, indent=4)

