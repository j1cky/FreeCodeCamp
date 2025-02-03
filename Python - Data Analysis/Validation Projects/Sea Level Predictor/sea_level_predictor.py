import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import subprocess
subprocess.call('clear')
def draw_plot():

    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
    

    # Line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Years from 1880 to 2050 for prediction
    sea_levels_extended = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_levels_extended, label='Fit Line (1880-2050)', color = 'r', linewidth = 2)


    # Line of best fit for data from 2000 to most recent year
    data_recent = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])

    # Make the prediction only for the range from 2000 onward
    years_recent_extended = range(2000, 2051)  # Only for 2000-2050 range
    sea_levels_recent_extended = [slope_recent * year + intercept_recent for year in years_recent_extended]
    plt.plot(years_recent_extended, sea_levels_recent_extended, label='Fit Line (2000-2050)', linestyle='--', color = 'g', linewidth = 2)




    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Show legend
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()