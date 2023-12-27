#plt es un alias para matplotlib.pyplot
import matplotlib.pyplot as plt

# Funcion que genera un grafico de barras
def generate_bar_chart(labels, values):
    # fig: se refiere a la figura
    # ax: se refiere a las cordenadas en las que se comienza a graficar
    # plt.subplots(): ejecuta el metodo subplot (todavia no se que hace)
    fig, ax = plt.subplots()
    # ax.bar: Aqui indico que las coordenadas van a ser para un grafico de barras
    # labels vendria a ser el nombre de los valores
    # values son los valores que tendra cada barra
    # sintaxis: ax.bar(lista de nombres,lista de valores)
    ax.bar(labels,values)
    # show: funcion para visualizar la grafica
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    # ax.pie: Aqui indico que las coordenadas van a ser para un grafico de tortas
    # labels vendria a ser el nombre de los valores
    # values son los valores que tendra cada barra
    # sintaxis: ax.pie(lista de valores,labels = lista de nombres)
    ax.pie(values , labels=labels)
    # Esto indica que la grafica este en el centro y con forma de circulo
    ax.axis('equal')
    plt.show()

# Grafico para diccionarios
def generate_dict_graphic(dict):
    fig , ax = plt.subplots()
    labels = list(dict.keys())
    values = list(dict.values())
    ax.bar(labels, values)
    plt.show()

if __name__ == '__main__' :
    labels = ['a', 'b', 'c']
    values = [10, 270, 40]
    generate_bar_chart(labels,values)
    generate_pie_chart(labels, values)