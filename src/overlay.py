from flask import Flask, request
from flask_cors import CORS
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading

app = Flask(__name__)
CORS(app)

DEBUG = False

def log_debug(message):
    if DEBUG:
        print(message)

class NowPlayingOverlay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Now Playing")
        self.geometry("400x100")
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.configure(background='black')

        # Set the window to be transparent
        self.wm_attributes('-transparentcolor', 'black')

        # Position the window at the top right corner of the screen
        screen_width = self.winfo_screenwidth()
        #self.geometry(f"+{screen_width - 300}+0")
        #self.geometry(f"+{screen_width - 1380}+0")
        self.geometry(f"+0+10")

        self.album_art_label = tk.Label(self, bg="black")
        self.album_art_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        self.song_label = tk.Label(self, text="Song: ", font=("Helvetica", 12), fg="white", bg="black")
        self.song_label.grid(row=0, column=1, sticky="w")

        self.artist_label = tk.Label(self, text="Artist: ", font=("Helvetica", 12), fg="white", bg="black")
        self.artist_label.grid(row=1, column=1, sticky="w")

    def update_song_info(self, song, artist, album_art):
        log_debug(f"Updating song info: Song={song}, Artist={artist}, AlbumArt={album_art}")
        self.song_label.config(text=f"Song: {song}")
        self.artist_label.config(text=f"Artist: {artist}")

        if album_art:
            try:
                log_debug(f"Fetching album art from URL: {album_art}")
                response = requests.get(album_art)
                log_debug(f"Album art request status: {response.status_code}")
                image = Image.open(BytesIO(response.content))
                image = image.resize((50, 50), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                self.album_art_label.config(image=photo)
                self.album_art_label.image = photo
            except Exception as e:
                log_debug(f"Error loading album art: {e}")
                self.album_art_label.config(image='')
        else:
            self.album_art_label.config(image='')

overlay = NowPlayingOverlay()

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    song = data.get('song', '')
    artist = data.get('artist', '')
    album_art = data.get('albumArt', '')

    log_debug(f"Received update: Song={song}, Artist={artist}, AlbumArt={album_art}")

    overlay.update_song_info(song, artist, album_art)
    return {"status": "success"}

def run_flask():
    app.run(host='0.0.0.0', port=5000, use_reloader=False)

if __name__ == "__main__":
    log_debug("Starting Flask server")
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    overlay.mainloop()
