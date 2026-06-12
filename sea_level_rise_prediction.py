import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='steelblue', label='Original Data')

    # 3. Create first line of best fit (using all data)
    # Get the slope and y-intercept
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 1880 to 2050 for the x-axis
    x_pred_all = pd.Series([i for i in range(1880, 2051)])
    
    # Calculate the corresponding y values using the line equation (y = mx + b)
    y_pred_all = res_all.slope * x_pred_all + res_all.intercept
    
    # Plot the first line of best fit
    plt.plot(x_pred_all, y_pred_all, color='red', label='Best Fit (1880-2050)')

    # 4. Create second line of best fit (using data from 2000 onwards)
    # Filter the dataframe for years >= 2000
    df_recent = df[df['Year'] >= 2000]
    
    # Get the new slope and y-intercept
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 2000 to 2050 for the x-axis
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    
    # Calculate the corresponding y values
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    
    # Plot the second line of best fit
    plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit (2000-2050)')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
