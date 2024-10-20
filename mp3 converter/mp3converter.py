import yt_dlp
from pydub import AudioSegment
import os

def download_and_convert_youtube_to_mp3(youtube_url, output_path=r"C:\Users\johnc\Downloads"):
    try:
        # Make sure the directory exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Download audio using yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print(f"Download and conversion complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
youtube_url = input("Enter the YouTube URL: ")
download_and_convert_youtube_to_mp3(youtube_url)
