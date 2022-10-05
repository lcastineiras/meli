import re
import os
cantidad = 0

from flask import Flask, request
app = Flask(__name__)
@app.route('/') # url a utilizar
def query ():
    """Funcion utilizada cada vez que se haga una peticion al / """
    args = request.args
    file = args.get('file', default=None, type=str)# argumento recibido en la peticion
    word = args.get('word', default=None, type=str) # argumento recibido en la peticion
    cantidad = 0
    files = []
    if file is None: # Si en la peticion no se detalla el arg file, devuelve none

        path = os.listdir() # Declaro variable con contenido del directorio actual
        files = []
        for j in path: # Recorro el directorio actual

            if j.endswith('.txt'): # Filtro por archivos .txt
                files.append(j) # Guardo en la lista files los archivos .txt

        # Recorro y abro archivos .txt para leer su contenido
        for k in files: # Recorro y abro archivos .txt para leer su contenido

            with open(k, encoding='utf8') as file:
                mensaje3 = []
                mensaje = file.read()
                # Estandarizar el texto a minuscula:
                mensaje1 = mensaje.lower()
                # Reemplazo texto que no sea alfanumerico y con tildes por espacios
                mensaje2 = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', " ", mensaje1)
                # Convierto string a lista:
                mensaje3 = mensaje2.split()
                #Si la palabra esta en la lista, cuento la frecuencia:
                if word in mensaje3:
                    cantidad = cantidad + mensaje3.count(word)

        diccionario = {"Frecuencia": cantidad}
        return f'{diccionario}'


    if word is None:
        return f'Debe ingresar word'

    with open(file, encoding='utf8') as file:
        mensaje = file.read()
        mensaje1 = mensaje.lower()
        mensaje2 = re.sub(r'[^ \nA-Za-z0-9À-ÖØ-öø-ÿ/]+', " ", mensaje1)
        mensaje3 = mensaje2.split()
        if word in mensaje3:
            cantidad = mensaje3.count(word)
            diccionario = {"Frecuencia":cantidad}
            return f'{diccionario}'
        else:
            diccionario = {"Frecuencia": cantidad}
            return f'{diccionario}'


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
