# SpotIDL - Spotify Playlist Downloader

SpotIDL is a simple Python script that allows you to download Spotify playlists using the SpotDL library. The downloaded songs are saved to a `downloads` folder in your current working directory.

---

## Features

- **Easy to Use**: Just paste a Spotify playlist link and the script handles the rest.
- **Progress Tracking**: Displays download progress for each track.
- **Automatic Directory Management**: Creates a `downloads` folder if it doesn't already exist.

---

## Requirements

Ensure the following prerequisites are installed:

1. **Python 3.7 or newer**
   - Install Python if it's not already installed:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip -y
     ```

2. **SpotDL**: Install the SpotDL library via pip:
   ```bash
   pip install spotdl

3 **FFmpeg**: Required for audio processing.
    - Install FFmpeg:
    ```bash
    sudo apt install ffmpeg -y

## Setup

1. Clone or download the spotidl.py script to your system.

2. Add executable permissions to the script:
```bash
chmod +x spotidl.py
```

3. (Optional) Move it to a directory in your PATH to make it globally accessible:

```bash
Copy code
