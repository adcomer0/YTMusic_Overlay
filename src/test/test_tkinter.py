import tkinter as tk

class NowPlayingOverlay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Now Playing")
        self.geometry("300x100")
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.configure(background='black')

        self.song_label = tk.Label(self, text="Song: Test Song", font=("Helvetica", 12), fg="white", bg="black")
        self.song_label.pack(pady=(10, 0))

        self.artist_label = tk.Label(self, text="Artist: Test Artist", font=("Helvetica", 12), fg="white", bg="black")
        self.artist_label.pack()

        self.album_art_label = tk.Label(self, text="Album Art Here", bg="black", fg="white")
        self.album_art_label.pack()

if __name__ == "__main__":
    overlay = NowPlayingOverlay()
    overlay.mainloop()
