# spotify_get_songs_from_playlist
Lists the songs in a given playlist so people without login can view the playlist.

# Usage:
- Get your PLAYLIST_ID
- Get your OAuth Token
- use generated request

# PLAYLIST_ID example:
https://open.spotify.com/playlist/4jUcozZNAVFJXP2DMGOQ1f?si=035205063cfb41b5
https://open.spotify.com/playlist/${PLAYLIST_ID}?si=035205063cfb41b5

# How to get OAuth Token:
- https://stackoverflow.com/questions/60659902/how-to-get-oauth-token-from-spotify

# Request
curl -X "GET" "https://api.spotify.com/v1/playlists/${PLAYLIST_ID}/tracks?market=ES&offset=5" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer ${AUTH_TOKEN}" > playlist_songs.json
