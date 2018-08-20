import matplotlib.pyplot as plt

from greedy_boss import (GreedyBoss, LOGLOG, STANDARD)

def generate_lines_to_plot(days, plot_type):
    bribes_colors = [(0, 'orange'), (500, 'lightblue'),
                    (1000, 'red'), (2000, 'lightgreen')]
    return [(GreedyBoss(days, plot_type).greedy_boss(item[0]),
            item[1], 'Bribe increment = ' + str(item[0])) 
            for item in bribes_colors]

def days_to_plot(line):
    return [point[0] for point in line[0]]

def total_earnings_plot(line):
    return [point[1] for point in line[0]]

def generate_graph(plt):
    plt.xlabel('days')
    plt.ylabel('total earnings')
    plt.title('Greedy Boss')
    plt.legend()
    plt.grid()
    plt.show()

def run_simulations(days, plot_type):
    """
    Run simulations for several possible bribe increments
    """
    lines_to_plot = generate_lines_to_plot(days, plot_type)

    for line in lines_to_plot:
        plt.plot(days_to_plot(line),
                 total_earnings_plot(line),
                 color=line[1], label=line[2])

    generate_graph(plt)

run_simulations(70, STANDARD)
