import yt_dlp

def seconds_to_hms(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

def get_total_playlist_duration(playlist_url: str) -> str:
    ydl = yt_dlp.YoutubeDL(params={'quiet': True})
    info = ydl.extract_info(url=playlist_url, download=False)
    video_durations = [video['duration'] for video in info['entries']]
    return seconds_to_hms(sum(video_durations))