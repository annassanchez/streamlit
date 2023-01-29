import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def valence_general(df, playlist_input):
    sns.set_theme(style="darkgrid")
    #valence = df[df['chart'] == playlist_input].groupby(['date'])[['valence', 'energy', 'danceability']].mean().reset_index()
    valence = pd.melt(df[df['chart'] == playlist_input].groupby(['date'])['valence', 'energy', 'danceability'].mean().reset_index(), id_vars=['date'], value_vars=['valence', 'energy', 'danceability'])
    
    sns.lineplot(data = valence, x = 'date', y = 'value', hue='variable', palette='flare')

    plt.xlabel('')
    plt.ylim(0,1)
    plt.axvline('2020-1', 0, 1, linestyle='dashed')
    plt.text('2020-1', 1, 'covid-19 pandemic', horizontalalignment='left', size='medium', color='black', weight='semibold')
    plt.xticks(rotation = 90);

    plt.tight_layout()
    plt.savefig('imagenes/valence_general.png')

def general_violin(df, playlist_input):
    valence = df[df['chart'] == playlist_input]#.groupby(['date'])['valence'].mean().reset_index()
    fig, axs = plt.subplots(ncols=1, nrows = len(df['playlist_date'].dt.year.unique().tolist()), figsize = (10, 15), sharex=True,)
    list_years = valence.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    for year in list_years:
        sns.violinplot(data = valence[valence['playlist_date'].dt.year == year], 
            x=valence[valence['playlist_date'].dt.year == year].valence,  
            ax=axs[list_years.index(year)], palette='flare')
        axs[list_years.index(year)].set_title(str(year), fontsize=10)
        axs[list_years.index(year)].set_xlabel("")
    plt.tight_layout()
    plt.savefig('imagenes/valence_general_violin.png')

def general_boxplot(df, playlist_input):
    valence = df[df['chart'] == playlist_input]#.groupby(['date'])['valence'].mean().reset_index()
    fig, axs = plt.subplots(ncols=1, nrows = len(df['playlist_date'].dt.year.unique().tolist()), figsize = (10, 15), sharex=True,)
    list_years = valence.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    for year in list_years:
        sns.boxplot(data = valence[valence['playlist_date'].dt.year == year], 
            x=valence[valence['playlist_date'].dt.year == year].valence, 
            ax=axs[list_years.index(year)], palette='flare')
        axs[list_years.index(year)].set_title(str(year), fontsize=10, )
        axs[list_years.index(year)].set_xlabel("")
    plt.tight_layout()
    plt.savefig('imagenes/valence_general_boxplot.png')

def general_chart(df, playlist_input, column = 'valence', chart_type = 'boxplot'):
    valence = df[df['chart'] == playlist_input]#[['playlist_date', column]]#.groupby(['date'])['valence'].mean().reset_index()
    fig, axs = plt.subplots(ncols=1, nrows = len(df['playlist_date'].dt.year.unique().tolist()), figsize = (10, 15), sharex=True,)
    list_years = valence.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    for year in list_years:
        if chart_type == 'boxplot':
            sns.boxplot(data = valence[valence['playlist_date'].dt.year == year], 
                x = valence[valence['playlist_date'].dt.year == year][column], 
                ax = axs[list_years.index(year)], palette='flare')
            axs[list_years.index(year)].set_title(str(year), fontsize=10, )
            axs[list_years.index(year)].set_xlabel("")
        elif chart_type == 'violinplot':
            sns.violinplot(data = valence[valence['playlist_date'].dt.year == year], 
                x = valence[valence['playlist_date'].dt.year == year][column], 
                ax = axs[list_years.index(year)], palette='flare')
            axs[list_years.index(year)].set_title(str(year), fontsize=10, )
            axs[list_years.index(year)].set_xlabel("")
    plt.tight_layout()
    plt.savefig(f'imagenes/general_{chart_type}_{column}.png')

def general_catplot(df, playlist_input, chart_type = 'swarm'):
    df_filtered = df[df['chart'] == playlist_input]#[['playlist_date', column]]#.groupby(['date'])['valence'].mean().reset_index()
    fig, axs = plt.subplots(ncols=1, nrows = len(df['playlist_date'].dt.year.unique().tolist()), figsize = (10, 15), sharex=True,)
    list_years = df_filtered.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    for year in list_years:
        sns.catplot(
            data = df_filtered[df_filtered['playlist_date'].dt.year == year], 
            x = df_filtered[df_filtered['playlist_date'].dt.year == year]['key_mapped'], 
            hue = df_filtered[df_filtered['playlist_date'].dt.year == year]['mode_mapped'],
            ax = axs[list_years.index(year)], palette='flare', kind = chart_type
            )
        axs[list_years.index(year)].set_title(str(year), fontsize=10, )
        axs[list_years.index(year)].set_xlabel("")
    plt.tight_layout()
    plt.savefig(f'imagenes/general_catplot_keymode.png')