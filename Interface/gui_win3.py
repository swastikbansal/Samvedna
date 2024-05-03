from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage, Button
import tkinter as tk
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from Text2ASL import T2S


class FourthGUI:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets_win3")
    
    def record_audio(duration, filename, fs=44100):
        print("Recording...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(filename, fs, recording)  # Save as WAV file
        print("Recording finished and saved to", filename)

    def convert_audio_to_text(filename):
        r = sr.Recognizer()
        audio_file = sr.AudioFile(filename)
        with audio_file as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        return text

    def __init__(self, shared_data=None):
        self.shared_data = shared_data
        self.window = Tk()
        window_width = 1500
        window_height = 780
        screen_width = self.window.winfo_screenwidth()
        position_top = 0
        position_right = int(screen_width / 2 - window_width / 2)
        self.window.geometry(
            f"{window_width}x{window_height}+{position_right}+{position_top}"
        )
        self.window.configure(bg="#141416")

        self.canvas = Canvas(
            self.window,
            bg="#141416",
            height=780,
            width=1500,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        self.image_1 = self.load_image("image_1.png", 810.0, 475)

        self.image_2 = self.load_image("image_2.png", 330.0, 345.0)
        self.button_2 = Button(
            self.window,
            image=self.image_2,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_2_click,
        )
        self.button_2.place(x=240.0, y=255.0)

        self.image_3 = self.load_image("image_3.png", 767.0, 190.0)
        self.button_3 = Button(
            self.window,
            image=self.image_3,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_3_click,
        )
        self.button_3.place(x=635.0, y=146.0)

        self.image_4 = self.load_image("image_4.png", 750.0, 71.0)

        self.image_5 = self.load_image("image_5.png", 1416.0, 70.02142333984375)
        self.button_5 = Button(
            self.window,
            image=self.image_5,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_5_click,
        )
        self.button_5.place(x=1380.0, y=30.0)

        self.image_6 = self.load_image("image_6.png", 60.0, 391.02142333984375)

        self.entry_image_1 = self.load_image("entry_1.png", 464.0, 643.0)
        self.entry_1 = Entry(
            bd=0, bg="#141416", fg="#ffffff", font=("Arial", 20), highlightthickness=0
        )
        self.entry_1.place(x=194.0, y=534.0, width=540.0, height=218.0)

    def on_button_2_click(self):
        # t = T2S()
        # text = t.speech_to_text()
        # self.entry_1.delete(0, tk.END)
        # self.entry_1.insert(0, text)
        pass

    def on_button_3_click(self):
        print("Convert")
        entry = self.entry_1.get()
        t = T2S()
        from PIL import Image, ImageTk
        import os
        import io

        # Create a container widget to display the video widgets
        folder_path = (
            os.getcwd() + r"\ASL dataset"
        )  # Change this to the path of your image folder
        video_widgets = t.display_word_videos(entry, folder_path)

        self.vedio_canvas = Canvas(
            self.window,
            bg="#141416",
            height=500,
            width=500,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.vedio_canvas.place(x=880, y=400)

        # Create a list to store the PhotoImage objects
        self.photos = []

        # Create a generator that yields the PhotoImage objects
        def get_photos():
            for widget in video_widgets:
                # Save the image data to a BytesIO object
                image_data = io.BytesIO(widget.value)

                # Open the image data with PIL
                image = Image.open(image_data)

                # Convert the PIL Image to a PIL ImageTk.PhotoImage
                photo = ImageTk.PhotoImage(image)

                # Store the PhotoImage object in the list
                self.photos.append(photo)

                yield photo

        self.photo_gen = get_photos()

        def update_image():
            try:
                # Get the next PhotoImage object from the generator
                photo = next(self.photo_gen)

                # Display the image on the canvas
                self.vedio_canvas.create_image(0, 0, image=photo, anchor=tk.NW)

                # Schedule the next update
                self.window.after(500, update_image)  # Adjust the delay as needed
            except StopIteration:
                pass  # No more images to display

        # Start the update process
        update_image()

    def on_button_5_click(self):
        self.window.destroy()
        from gui_base import GUI

        second_window = GUI(self.shared_data)
        second_window.run()

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return FourthGUI.ASSETS_PATH / Path(path)

    def load_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = FourthGUI()
    gui.run()
