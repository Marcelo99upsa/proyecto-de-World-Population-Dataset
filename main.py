# https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset
import utils
import read_csv as read
import charts

if __name__ == '__main__':
    data = read.read_csv('app\data.csv')
    dictionary = utils.get_population(data)
    population_dict, labels, values = utils.population_by_country(dictionary)
    charts.generate_bar_chart(labels, values)
    # o
    # charts.generate_dict_graphic(population_dict)

    # Poblacion mundial
    world_population_dict, world_labels, world_values = utils.get_world_population_percentage(data)
    charts.generate_pie_chart(world_labels,world_values)