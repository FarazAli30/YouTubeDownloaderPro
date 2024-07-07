# YouTube Downloader

YouTube Downloader is a Python-based GUI application that allows users to download videos and audio from YouTube. It supports both individual video URLs and playlists. The application is built using the Tkinter library for the GUI and Pytube for handling the video downloading.

[Watch the demo video](https://scontent.cdninstagram.com/o1/v/t16/f1/m86/EE4907095AF4DFB1DB27B5BF6A70D6AD_video_dashinit.mp4?efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2xpcHMuYzIuNzIwLmJhc2VsaW5lIn0&_nc_ht=instagram.fkhi4-3.fna.fbcdn.net&_nc_cat=108&vs=996766982139888_512515042&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9FRTQ5MDcwOTVBRjRERkIxREIyN0I1QkY2QTcwRDZBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dNcjN5eHE5UDc4cE1wc0JBSkl4NzJDRC1vVkRicV9FQUFBRhUCAsgBACgAGAAbABUAACa2iIz%2B3K3ZPxUCKAJDMywXQFgszMzMzM0YEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HAA%3D%3D&_nc_rid=e28e86780f&ccb=9-4&oh=00_AYD2TUgEJ8mEPHeL6_WmbEOKgMfxJHApMJVC_IrXQ5Zgzw&oe=668C8ABF&_nc_sid=d885a2)

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
