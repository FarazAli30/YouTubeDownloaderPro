import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube, Playlist
import threading
import time

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        # Set fixed window size for Android device
        self.root.geometry("720x1080")

        container = tk.Frame(root)
        container.pack(fill="both", expand=True)

        self.url_label = tk.Label(container, text="YouTube URL:", font=("Arial", 7))
        self.url_label.pack(pady=6)

        self.url_entry = tk.Entry(container, width=40, font=("Arial", 8))
        self.url_entry.pack(pady=6)
        self.url_entry.bind("<KeyRelease>", self.check_validity)

        self.paste_button = tk.Button(container, text="Paste", font=("Arial", 5), command=self.paste_clipboard)
        self.paste_button.pack(pady=5)

        self.fetch_button = tk.Button(container, text="Fetch Videos", font=("Arial", 6), state=tk.DISABLED, command=self.fetch_videos)
        self.fetch_button.pack(pady=7)

        self.canvas = tk.Canvas(container, bg='white', highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, pady=7)

        self.scrollbar_y = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scrollbar_y.pack(side="right", fill="y")

        self.scrollbar_x = ttk.Scrollbar(container, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")

        self.canvas.configure(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

        self.scrollable_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.video_checkboxes = []

        self.download_720p_button = tk.Button(container, text="Download 720p", font=("Arial", 6), state=tk.DISABLED, command=lambda: self.start_download("720p"))
        self.download_720p_button.pack(pady=10, fill="x")

        self.download_360p_button = tk.Button(container, text="Download 360p", font=("Arial", 6), state=tk.DISABLED, command=lambda: self.start_download("360p"))
        self.download_360p_button.pack(pady=7, fill="x")

        self.download_audio_button = tk.Button(container, text="Download Audio", font=("Arial", 6), state=tk.DISABLED, command=lambda: self.start_download("audio"))
        self.download_audio_button.pack(pady=10, fill="x")

        self.progress_label = tk.Label(container, text="", font=("Arial", 11))
        self.progress_label.pack(pady=7)

        self.progress_bar = ttk.Progressbar(container, orient="horizontal", mode="determinate")
        self.progress_bar.pack(pady=7, fill="x")

    def check_validity(self, event=None):
        url = self.url_entry.get()
        if 'youtube.com' in url or 'youtu.be' in url:
            self.fetch_button.config(state=tk.NORMAL)
        else:
            self.fetch_button.config(state=tk.DISABLED)

    def paste_clipboard(self):
        try:
            clipboard_content = self.root.clipboard_get()
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, clipboard_content)
            self.check_validity()
        except tk.TclError:
            messagebox.showerror("Error", "Clipboard is empty")

    def fetch_videos(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        self.fetch_button.config(state=tk.DISABLED)
        self.download_720p_button.config(state=tk.DISABLED)
        self.download_360p_button.config(state=tk.DISABLED)
        self.download_audio_button.config(state=tk.DISABLED)
        self.progress_label.config(text="Fetching videos, please wait...")

        threading.Thread(target=self._fetch_videos, args=(url,)).start()

    def _fetch_videos(self, url):
        try:
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            self.video_checkboxes.clear()

            if 'playlist' in url:
                self.playlist = Playlist(url)
                for video in self.playlist.videos:
                    var = tk.BooleanVar()
                    chk = tk.Checkbutton(self.scrollable_frame, text=video.title, variable=var, font=("Arial", 14))
                    chk.pack(anchor='w', padx=10, pady=5)
                    self.video_checkboxes.append((chk, var, video.watch_url))
            else:
                video = YouTube(url)
                var = tk.BooleanVar()
                chk = tk.Checkbutton(self.scrollable_frame, text=video.title, variable=var, font=("Arial", 14))
                chk.pack(anchor='w', padx=10, pady=5)
                self.video_checkboxes.append((chk, var, video.watch_url))

            self.progress_label.config(text="Fetch complete")
            self.download_720p_button.config(state=tk.NORMAL)
            self.download_360p_button.config(state=tk.NORMAL)
            self.download_audio_button.config(state=tk.NORMAL)
        except Exception as e:
            self.progress_label.config(text="Fetch failed")
            messagebox.showerror("Error", f"Failed to fetch videos: {str(e)}")
        finally:
            self.fetch_button.config(state=tk.NORMAL)

    def start_download(self, resolution):
        selected_videos = [video_url for chk, var, video_url in self.video_checkboxes if var.get()]
        if not selected_videos:
            messagebox.showerror("Error", "Please select at least one video to download")
            return

        self.download_720p_button.config(state=tk.DISABLED)
        self.download_360p_button.config(state=tk.DISABLED)
        self.download_audio_button.config(state=tk.DISABLED)
        threading.Thread(target=self.download_videos, args=(selected_videos, resolution)).start()

    def download_videos(self, video_urls, resolution):
        for url in video_urls:
            self.download_individual_video(url, resolution)
        self.download_720p_button.config(state=tk.NORMAL)
        self.download_360p_button.config(state=tk.NORMAL)
        self.download_audio_button.config(state=tk.NORMAL)

    def download_individual_video(self, url, resolution):
        yt = YouTube(url, on_progress_callback=self.progress_function, on_complete_callback=self.complete_function)

        if resolution == "720p":
            stream = yt.streams.filter(progressive=True, res="720p", file_extension='mp4').first()
        elif resolution == "360p":
            stream = yt.streams.filter(progressive=True, res="360p", file_extension='mp4').first()
        elif resolution == "audio":
            stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        if not stream:
            messagebox.showerror("Error", f"No stream available for {resolution}")
            return

        self.total_size = stream.filesize
        self.bytes_downloaded = 0
        self.start_time = time.time()

        self.progress_bar['value'] = 0
        self.progress_bar['maximum'] = self.total_size
        self.progress_label.config(text="Downloading...")

        self.update_progress()
        stream.download()

    def progress_function(self, stream, chunk, bytes_remaining):
        self.bytes_downloaded = self.total_size - bytes_remaining

    def complete_function(self, stream, file_path):
        self.progress_label.config(text=f"Download complete: {file_path}")
        messagebox.showinfo("Download Complete", f"Download complete: {file_path}")

    def update_progress(self):
        if self.bytes_downloaded < self.total_size:
            elapsed_time = time.time() - self.start_time
            download_speed = self.bytes_downloaded / elapsed_time / 1024  # in KB/s

            self.progress_bar['value'] = self.bytes_downloaded
            self.progress_label.config(text=f"Downloaded: {self.bytes_downloaded / 1024 / 1024:.2f} MB / {self.total_size / 1024 / 1024:.2f} MB | Speed: {download_speed:.2f} KB/s")

            self.root.after(1000, self.update_progress)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
