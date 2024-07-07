# YouTube Downloader

YouTube Downloader is a Python-based GUI application that allows users to download videos and audio from YouTube. It supports both individual video URLs and playlists. The application is built using the Tkinter library for the GUI and Pytube for handling the video downloading.

[Watch the demo video](https://www.instagram.com/reel/C8_jp8jgKFz/?igsh=NG90anVyN2lleTJk)

## Features

- Download videos in 720p or 360p resolution.
- Download audio in MP4 format.
- Fetch and display videos from individual URLs or playlists.
- Display download progress with a progress bar.
- Simple and intuitive GUI.

## Requirements

- Python 3.x
- Tkinter library (included with Python standard library)
- Pytube library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/FarazAli30/YouTubeDownloaderPro.git
    cd youtube-downloader
    ```

2. **Install the required libraries:**

    ```bash
    pip install pytube3
    ```

## Usage

1. **Run the application:**

    ```bash
    python youtube_downloader.py
    ```

2. **Using the GUI:**
   - Enter the YouTube URL in the text field.
   - Click on the "Paste" button to paste the URL from the clipboard.
   - Click on "Fetch Videos" to retrieve the video(s).
   - Select the videos you want to download.
   - Choose the desired resolution (720p, 360p) or audio.
   - Monitor the download progress with the progress bar.

## Project Structure

```plaintext
youtube-downloader/
├── README.md
└── youtube_downloader.py
```


## Components

### 1. `YouTubeDownloader` Class

This is the main class of the application that initializes and controls the GUI. It contains methods for fetching videos, handling downloads, and updating the progress.

### 2. GUI Elements

The GUI is built using Tkinter and consists of various elements:
- **Labels**: Used for displaying text (e.g., "YouTube URL:").
- **Entry**: A text field for entering the YouTube URL.
- **Buttons**: For actions like "Paste", "Fetch Videos", "Download 720p", etc.
- **Canvas**: For displaying a scrollable list of fetched videos.
- **Progressbar**: For showing download progress.

### 3. Fetching Videos

The `fetch_videos` method retrieves the list of videos from the provided URL (individual or playlist) and displays them in the scrollable canvas.

### 4. Downloading Videos

The `start_download` and `download_videos` methods handle the downloading of selected videos in the desired resolution or audio format.

### 5. Progress Update

The `update_progress` method periodically updates the progress bar and label to show the current download status.

### 6. Error Handling

The application includes error handling for various scenarios, such as invalid URLs and download failures, providing appropriate messages to the user.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
