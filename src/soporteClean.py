import pickle
import pandas as pd
import src.biblioteca as bb 

def importDatasets():
    with open('data/playlist.pickle', 'rb') as base_data:
        base_data = pickle.load(base_data)
    with open('data/spotify.pickle', 'rb') as data_spotify:
        data_spotify = pickle.load(data_spotify)
    data_spotify.drop_duplicates(inplace=True)
    with open('data/lastfm.pickle', 'rb') as data_lastfm:
        data_lastfm = pickle.load(data_lastfm)
    data_lastfm.drop_duplicates(inplace=True)
    df = base_data.merge(data_lastfm, on = 'url', indicator = True, how = 'left')
    df.drop(['_merge'], axis = 1, inplace = True)
    df = df.merge(data_spotify, on = 'url', indicator = True, how = 'left')
    df.drop(['artist_y', 'track_x', 'artist', 'track_y', '_merge'], axis = 1, inplace= True)
    df.rename({'artist_x':'artist', 'date_x':'playlist_date', 'date_y':'release_date'}, inplace=True, axis=1)
    df['playlist_date'] = pd.to_datetime(df['playlist_date'])
    df['month'] = df['playlist_date'].dt.month
    df['year'] = df['playlist_date'].dt.year
    df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str)
    df['key_mapped'] = df['key'].replace(bb.dict_keys)
    df['mode_mapped'] = df['mode'].replace(bb.dict_scale)
    return df

def info_artists(df):
    top10_artists = df.groupby(['artist'])['streams'].sum().reset_index().sort_values(by = 'streams', ascending = False).head(5)
    top10_artists['ratio'] = top10_artists['streams'] * 100 / (df[~df['streams'].isnull()]['streams'].sum())
    return top10_artists

def info_genre(df):
    top10_musicgenre = df.groupby(['music_genre'])['streams'].sum().reset_index().sort_values(by = 'streams', ascending = False).head(5)
    top10_musicgenre['ratio'] = top10_musicgenre['streams'] * 100 / (df[~df['streams'].isnull()]['streams'].sum())
    return top10_musicgenre