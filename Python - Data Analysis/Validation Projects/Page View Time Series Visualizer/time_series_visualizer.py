import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import subprocess

subprocess.call('clear')
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

df = pd.read_csv(

    'fcc-forum-pageviews.csv',
    parse_dates=[0],
    date_format={'col 1': '%Y/%m/%d'},
    index_col='date'
    
)  

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

df = df[
    (df['value'] >= lower_bound )&
    (df['value'] <= upper_bound)
]
def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(12, 3.8))
    ax.plot(df.index, df['value'], color='r', linewidth=1) 
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    plt.tight_layout()



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Resample the data by month and year, calculating the mean of page views for each month
    df_resampled = df.resample('M').mean()

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 7))

    # Plot the data: group by year and plot average page views per month
    df_resampled.groupby([df_resampled.index.year, df_resampled.index.month])['value'].mean().unstack().plot(kind='bar', ax=ax)

    # Set the title and labels
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Set legend with Month labels and a title
    ax.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], loc='upper left')


    # Save the image (if needed)
    fig.savefig('bar_plot.png')

    # Return the figure object
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df.index.year
    df_box['month'] = df.index.month

    # Create the figure and axes for the two adjacent box plots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Plot Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', palette="tab10", data=df_box, ax=axes[0], flierprops={"marker": "D", "markersize":1})
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Plot Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', palette='husl', data=df_box, ax=axes[1], flierprops={"marker": "D", "markersize":1})
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Set the month labels in the second plot to be Jan, Feb, Mar, ..., Dec
    axes[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # Adjust layout to make the plots fit properly
    plt.tight_layout()



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


draw_box_plot()