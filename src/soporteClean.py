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
    df['month'] = df['playlist_date'].dt.month
    df['year'] = df['playlist_date'].dt.year
    df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str)
    df['key_mapped'] = df['key'].rename(bb.dict_keys, axis = 0)
    df['mode_mapped'] = df['mode'].rename(bb.dict_scale, axis = 0)
    return df

def info_artistas(artista, df):
    sliced_df = df[df['artists'] == artista].groupby(['artist', 'track'])['valence'].mean().reset_index()
    return sliced_df