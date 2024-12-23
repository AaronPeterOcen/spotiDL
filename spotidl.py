#!/usr/bin/env python3

import os
import subprocess

def main():
    print("Welcome to SpotIDL: Your Spotify Playlist Downloader!")
    
    # Ask for the Spotify playlist link
    playlist_link = input("Please paste the Spotify playlist link: ").strip()
    
    if not playlist_link.startswith("https://open.spotify.com/playlist/"):
        print("Invalid playlist link. Please make sure it is a Spotify playlist link.")
        return
    
    # Create a downloads directory if it doesn't exist
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    
    print("\nDownloading playlist to the 'downloads' folder...\n")
    
    # Run SpotDL with progress tracking
    try:
        subprocess.run(
            ["spotdl", "download", playlist_link, "--output", download_dir],
            check=True,
        )
        print(f"\nDownload complete! Files saved in: {download_dir}")
    except subprocess.CalledProcessError:
        print("\nAn error occurred while downloading the playlist. Please try again.")
    except FileNotFoundError:
        print("\nSpotDL is not installed. Please install it with `pip install spotdl`.")

if __name__ == "__main__":
    main()
