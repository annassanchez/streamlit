import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def valence_general(df, playlist_input):
    sns.set_theme(style="darkgrid", font_scale=0.75)
    sns.set(rc={'figure.figsize':(20,5)})
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

def general_kde(df, playlist_input, variable):
    df_filtered = df[df['chart'] == playlist_input]
    sns.set_theme(style="darkgrid")
    sns.set(rc={'figure.figsize':(20,5)})
    sns.kdeplot(data=df_filtered, x='playlist_date', hue = variable, multiple="fill", palette = 'pastel')
    plt.tight_layout()
    plt.savefig(f'imagenes/general_kde_{variable}.png')

def music_lineplot(df, playlist_input, top_music, variable = 'valence'):
    sns.set_theme(style="darkgrid", font_scale=0.75)
    sns.set(rc={'figure.figsize':(20,5)})
    #valence = df[df['chart'] == playlist_input].groupby(['date'])[['valence', 'energy', 'danceability']].mean().reset_index()
    df_playlist = df[df['chart'] == playlist_input]
    df_filtered = df_playlist[(df_playlist['music_genre'].isin(top_music))].groupby(['date', 'music_genre'])[variable].mean().reset_index()
    
    sns.lineplot(data = df_filtered, x = 'date', y = variable, hue='music_genre', palette='pastel')
    plt.xlabel('')
    plt.ylim(0,1)
    plt.axvline('2020-1', 0, 1, linestyle='dashed')
    plt.text('2020-1', 1, 'covid-19 pandemic', horizontalalignment='left', size='medium', color='black', weight='semibold')
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.savefig(f'imagenes/lineplot_genre_{variable}.png')

def general_chart_genres(df, playlist_input, top_music, column = 'valence', chart_type = 'boxplot'):
    valence = df[df['chart'] == playlist_input]#[['playlist_date', column]]#.groupby(['date'])['valence'].mean().reset_index()
    fig, axs = plt.subplots(ncols=len(top_music), nrows = len(df['playlist_date'].dt.year.unique().tolist()), figsize = (25,10), sharex=True,)
    list_years = valence.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    for genre in top_music:
        for year in list_years:
            if chart_type == 'boxplot':
                sns.boxplot(data = valence[valence['playlist_date'].dt.year == year], 
                    x = valence[valence['playlist_date'].dt.year == year][column], 
                    ax = axs[list_years.index(year)][top_music.index(genre)], palette='flare')
                axs[list_years.index(year)][top_music.index(genre)].set_title(str(year), fontsize=10, )
                axs[list_years.index(year)][top_music.index(genre)].set_xlabel(genre)
            elif chart_type == 'violinplot':
                sns.violinplot(data = valence[valence['playlist_date'].dt.year == year], 
                    x = valence[valence['playlist_date'].dt.year == year][column], 
                    ax = axs[list_years.index(year)][top_music.index(genre)], palette='flare')
                axs[list_years.index(year)][top_music.index(genre)].set_title(str(year), fontsize=10, )
                axs[list_years.index(year)][top_music.index(genre)].set_xlabel(genre)
    plt.tight_layout()
    plt.savefig(f'imagenes/genres_{chart_type}_{column}.png')

def genre_kde(df, playlist_input, top_music, variable = 'key_mapped'):
    df_filtered = df[df['chart'] == playlist_input]
    sns.set_theme(style="darkgrid")
    fig, axs = plt.subplots(ncols=len(top_music), nrows = 1, figsize = (25,5), sharex=True)
    for genre in top_music:
        data = df_filtered[df_filtered['music_genre'] == genre]
        sns.kdeplot(data=data, 
            x="playlist_date", 
            hue=variable, ax = axs[top_music.index(genre)],
            multiple="fill", palette = 'pastel')
        axs[top_music.index(genre)].set_title(genre, fontsize=10, )
        axs[top_music.index(genre)].set_ylabel('')
    plt.tight_layout()
    plt.savefig(f'imagenes/genres_kde_{variable}.png')

def artist_lineplot(df, playlist_input, top_artist, variable = 'valence'):
    sns.set_theme(style="darkgrid", font_scale=0.75)
    sns.set(rc={'figure.figsize':(20,5)})
    #valence = df[df['chart'] == playlist_input].groupby(['date'])[['valence', 'energy', 'danceability']].mean().reset_index()
    df_playlist = df[df['chart'] == playlist_input]
    df_filtered = df_playlist[(df_playlist['artist'].isin(top_artist))].groupby(['date', 'artist'])[variable].mean().reset_index()
    
    sns.lineplot(data = df_filtered, x = 'date', y = variable, hue='artist', palette='pastel')
    plt.xlabel('')
    plt.ylim(0,1)
    plt.axvline('2020-1', 0, 1, linestyle='dashed')
    plt.text('2020-1', 1, 'covid-19 pandemic', horizontalalignment='left', size='medium', color='black', weight='semibold')
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.savefig(f'imagenes/lineplot_artist_{variable}.png')

def general_chart_artist(df, playlist_input, top_artist, column = 'valence', chart_type = 'boxplot'):
    valence = df[df['chart'] == playlist_input]#[['playlist_date', column]]#.groupby(['date'])['valence'].mean().reset_index()
    fig, axs = plt.subplots(ncols=len(top_artist), nrows = len(df['playlist_date'].dt.year.unique().tolist()), figsize = (25,10), sharex=True,)
    list_years = valence.sort_values(by = ['playlist_date'])['playlist_date'].dt.year.unique().tolist()
    sns.set_theme(style="darkgrid")
    for artist in top_artist:
        for year in list_years:
            if chart_type == 'boxplot':
                sns.boxplot(data = valence[valence['playlist_date'].dt.year == year], 
                    x = valence[valence['playlist_date'].dt.year == year][column], 
                    ax = axs[list_years.index(year)][top_artist.index(artist)], palette='flare')
                axs[list_years.index(year)][top_artist.index(artist)].set_title(str(year), fontsize=10, )
                axs[list_years.index(year)][top_artist.index(artist)].set_xlabel(artist)
            elif chart_type == 'violinplot':
                sns.violinplot(data = valence[valence['playlist_date'].dt.year == year], 
                    x = valence[valence['playlist_date'].dt.year == year][column], 
                    ax = axs[list_years.index(year)][top_artist.index(artist)], palette='flare')
                axs[list_years.index(year)][top_artist.index(artist)].set_title(str(year), fontsize=10, )
                axs[list_years.index(year)][top_artist.index(artist)].set_xlabel(artist)
    plt.tight_layout()
    plt.savefig(f'imagenes/artist_{chart_type}_{column}.png')

def artist_kde(df, playlist_input, top_artist, variable = 'key_mapped'):
    df_filtered = df[df['chart'] == playlist_input]
    sns.set_theme(style="darkgrid")
    fig, axs = plt.subplots(ncols=len(top_artist), nrows = 1, figsize = (25,5), sharex=True)
    for artist in top_artist:
        data = df_filtered[df_filtered['artist'] == artist]
        sns.kdeplot(data=data, 
            x="playlist_date", 
            hue=variable, ax = axs[top_artist.index(artist)],
            multiple="fill", palette = 'pastel')
        axs[top_artist.index(artist)].set_title(artist, fontsize=10, )
        axs[top_artist.index(artist)].set_ylabel('')
    plt.tight_layout()
    plt.savefig(f'imagenes/artists_kde_{variable}.png')