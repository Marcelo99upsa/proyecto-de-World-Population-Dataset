# Funcion para buscar los datos de un pais
def get_population(data):
    country = input('Introduce el pais a buscar: ')
    country_dict = {}
    # Itero sobre el data.csv para comparar y guardar el diccionario del pais solicitado
    for fila in data:
        if fila['Country/Territory'] == country:
            country_dict.update(fila)
    return country_dict

def get_world_population_percentage(data):
    world_country_list = []
    world_population_list = []
    # Itero sobre el data.csv para comparar y guardar los nombres de cada pais y su World Population Percentage
    for fila in data:
        # Itero sobre cada Item del diccionario fila
        for key , value in fila.items():
            # Si la key es un nombre de territorio lo guardo en world_country_list
            if key == 'Country/Territory':
                world_country_list.append(value)
            # Si la key es un World Population Percentage lo guardo convierto en flotante y lo guardo en world_population_list
            if key == 'World Population Percentage':
                world_population_list.append(float(value))
    # Junto el nombre del pais y su world population en una tupla,convierto el par key:value en diccionario
    world_population_dict = dict(zip(world_country_list,world_population_list))
    # Guardo las keys y values en diferentes variables
    labels = world_population_dict.keys()
    values = world_population_dict.values()
    # Retorna el diccionario completo,sus llaves , sus valores
    return world_population_dict, labels, values

# Funcion para obtener la poblacion de un pais
def population_by_country(country_dict):

    filter_list = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
    # for element in data:
    #     print(element)
    # Diccionario vacio para guardar los datos buscados
    population_dict = {}
    # Itero sobre los items del diccionario
    # Si la key iterada se encuentra en la lista filter_list
    # Se guarda el item en population_dict
    for key , value in country_dict.items():
        if key in filter_list:
            population_dict[key] = int(value)
    # otra forma
    # population_dict = {
    #     '2022' : int(country_dict['2022 Population']),
    #     '2020' : int(country_dict['2022 Population']),
    #     '2015' : int(country_dict['2022 Population']),
    #     '2010' : int(country_dict['2022 Population']),
    #     '2000' : int(country_dict['2022 Population']),
    #     '1990' : int(country_dict['2022 Population']),
    #     '1980' : int(country_dict['2022 Population']),
    #     '1970' : int(country_dict['2022 Population'])
    # }
    # Guardo las keys y values en diferentes variables
    labels = population_dict.keys()
    values = population_dict.values()
    # Retorna el diccionario completo,sus llaves , sus valores
    return population_dict,labels, values