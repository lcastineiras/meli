import re
import os

error = "error 404"
files = []
from flask import Flask, request

def withopen (archivo):

    try:
        with open(f"./coleccion_2022/{archivo}", encoding="utf8", errors='ignore') as file:
            mensaje = file.read()
            mensaje2 = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', " ", mensaje).lower().split()
            return (mensaje2)
    except:
        return (error)



app = Flask(__name__)
@app.route('/') # url a utilizar

def query ():
    """Funcion utilizada cada vez que se haga una peticion al / """
    args = request.args
    file = args.get('file', default=None, type=str)

    try:
        word = args.get('word', default=None, type=str).lower()
    except:
        return (error)

    cantidad = 0

    if file is None: # Si en la peticion no se detalla el arg file, devuelve none

        path = os.listdir("./coleccion_2022") # Declaro variable con contenido del directorio actual
        files = []
        for j in path: # Recorro el directorio actual

            if j.endswith('.txt'): # Filtro por archivos .txt
                files.append(j) # Guardo en la lista files los archivos .txt

        # Recorro y abro archivos .txt para leer su contenido
        for k in files: # Recorro y abro archivos .txt para leer su contenido
            subcant = withopen(k)


            if word in subcant:
                cantidad = cantidad + subcant.count(word)
        diccionario = {"Frecuencia": cantidad}
        return f'{diccionario}'

    else:
        try:
            archivo2 = withopen(file)

            if word in archivo2:
                cantidad = archivo2.count(word)
                diccionario = {"Frecuencia": cantidad}
                return f'{diccionario}'


        except:
            return (error)




    return (error)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
