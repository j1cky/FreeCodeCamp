import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import subprocess 

subprocess.call('clear')


# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight']/((df['height']*0.01)**2) > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol']>1).astype(int)
df['gluc'] = (df['gluc']>1).astype(int)

# 4
def draw_cat_plot():
    # 5 Melt the dataframe for categorical plotting
    df_cat = pd.melt(df, id_vars=['cardio'], 
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight','smoke'])


    # 6 Group and reformat the data to count occurrences
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7 Convert the data into long format and create a categorical plot
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', 
                      data=df_cat, kind='bar', height=5, aspect=1).figure


    # 9
    fig.savefig('catplot.png')
    return fig

draw_cat_plot()


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))      

    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="icefire",cbar_kws={"shrink": 0.5}, vmax=0.3, vmin=-0.3, center=0, linewidths=0.5)



    # 16
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()