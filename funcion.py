dir = "coleccion_2022"
import re


files = []

def withopen (file):
    """Funcion que abre archivo pasado como parametro, formatea y convierte el texto en una lista que contiene las palabras"""

    with open(f"./{dir}/{file}", encoding="utf8", errors='ignore') as file:
        content_file = file.read()
        list_words = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', " ", content_file).lower().split()
        return (list_words)

