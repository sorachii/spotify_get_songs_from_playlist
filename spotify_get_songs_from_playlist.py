import json

with open('playlist_songs.json') as f:
    playlist = json.load(f)
    for ob in playlist["items"]:
        print(f'{ob["track"]["artists"][0]["name"]} - {ob["track"]["name"]}')
