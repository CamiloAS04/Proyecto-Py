from collections import Counter

def generar_reporte(cvs):
    print("\n--- Reporte de habilidades más comunes ---")
    todas_habilidades = []
    for cv in cvs.values():
        todas_habilidades.extend(list(cv["habilidades"]))
    
    contador = Counter(todas_habilidades)
    for habilidad, frecuencia in contador.most_common():
        print(f"{habilidad}: {frecuencia} candidatos")
