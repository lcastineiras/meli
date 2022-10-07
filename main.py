import os
dir = "coleccion_2022"
error = "error 404"
files = []
from flask import Flask, request
from funcion import *


app = Flask(__name__)
@app.route('/') # url a utilizar

def query ():
    """Funcion utilizada cada vez que se haga una peticion al / """
    args = request.args
    file = args.get('file', default=None, type=str)

    # verifica que se ingrese argumento word, en caso de que no exista devuelve error
    try:
        word = args.get('word', default=None, type=str).lower()
    except:
        return (error)

    cant = 0

    # Si no se ingresa ningun file como argumento, busca la palabra ingresada en todos los archivos
    if file is None: # Si en la peticion no se detalla el arg file, devuelve none

        path = os.listdir(f"./{dir}") # declara variable con contenido del directorio
        files = []
        for j in path: # Recorre el directorio actual

            if j.endswith('.txt'): # Verifica que los archivos sean .txt
                text_file = withopen(j)  # Abre los archivos con la funcion y devuelve una lista con las palabras

                if word in text_file: # Se busca la palabra ingresa
                    cant = cant + text_file.count(word) # Cuenta la frecuencia de la palabra y la suma a la variable cant
                    # si la palabra ingresada no se encuentra, devuelve frecuencia 0
        resDictionary = {"Frecuencia": cant}
        return f'{resDictionary}' # Devuelve diccionario con frecuencia de la palabra ingresada

    # Si se especifica un nombre de archivo, se verifica que el archivo exista y se pueda abrir
    else:
        try:
            withopen(file)
            text_file = withopen(file)
            if word in text_file:
                cant = text_file.count(word)
                resDictionary = {"Frecuencia": cant}
                return f'{resDictionary}'
            # Si la palabra ingresada no esta en el archivo, devuelve frecuencia 0
            else:
                return ("{'Frecuencia': 0}")
        except:
            return(error)
        # si la palabra ingresada esta en el archivo, las cuenta y devuelve frecuencia


    return (error)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
