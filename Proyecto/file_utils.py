import json
import os

FILE_PATH = "data/cvs.json"

def cargar_cvs():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as f:
        data = json.load(f)
        # Convertimos habilidades a set
        for cv in data.values():
            cv["habilidades"] = set(cv["habilidades"])
        return data

def guardar_cvs(cvs):
    # Convertir sets a listas para guardar en JSON
    cvs_serializable = {k: {**v, "habilidades": list(v["habilidades"])} for k, v in cvs.items()}
    with open(FILE_PATH, "w") as f:
        json.dump(cvs_serializable, f, indent=4)
