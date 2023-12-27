#----- modulo para leer el acrhivo csv --------
import csv #CSV (Comma-Separated Values)

def read_csv(path):
    # Abre el archivo ubicado en la ruta especificada por 'path'
    # 'r' : El archivo se abre en modo de lectura 
    # encoding="UTF-8" : convierte todo en letras
    # Voy a abrir este archivo como solo lectura y lo voy a cerrar cada que termino una operacion,de esta forma se guarda memoria
    # Al darle un alias hago todo ese proceso solo con llamar a csvfile
    with open(path,'r',encoding="UTF-8") as csvfile:
        # csv.reader sintaxis: csv.reader(iterable,parametros opcionales)
        # Crea un objeto 'csv.reader' que permite leer el contenido del archivo CSV
        # delimiter=',' , delimiter es la forma en la que vienen separados los datos
        # reader = Esta variable guarda todo el archivo leido
        reader = csv.reader(csvfile, delimiter=',')

        # Imprime la primera fila
        # La primera fila del archivo son keys o columnas
        header = next(reader)
        # lista vacia
        data = []
        # Itero sobre cada fila del reader
        for fila in reader:
            # zip une cada fila de header y fila en una tupla ('header','fila')
            # iterable guarda la lista de tuplas
            iterable = zip(header,fila)
            # Cada tupla se convierte en un par key : value
            # Esto se podria simplificar con dict(iterable)
            # Cada linea se hace un diccionario{header : fila}
            country_dict = {key: value for key, value in iterable}
            # Se guarda cada fila en la lista data
            data.append(country_dict)
        # Retorna la lista de diccionarios
        return data


# if __name__ == '__main__':
#     data = read_csv('app\data.csv')
#     print(data[0])