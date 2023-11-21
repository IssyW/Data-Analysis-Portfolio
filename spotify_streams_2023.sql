-- Extract top 10 streamed songs
SELECT track_name, artist_s__name, released_year, SAFE_CAST(streams AS INT64) AS total_streams FROM `spotify-streams-data-project.Spotify_streams.Spotify_streams_2023`
FROM `spotify-streams-data-project.Spotify_streams.Spotify_streams_2023` 
WHERE total_streams IS NOT NULL
ORDER BY streams DESC 
LIMIT 10
