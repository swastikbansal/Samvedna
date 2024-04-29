from pathlib import Path
from tkinter import Button, Tk, Canvas, Entry, PhotoImage

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from ImageSummarizer import ImageSummarizer
import os


class SixthGUI:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets_win4")

    def __init__(self, shared_data=None):

        self.window = Tk()

        self.create_widgets()
        self.window.geometry("1500x780")
        self.window.configure(bg="#141416")
        self.window.resizable(False, False)
        self.shared_data = shared_data

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return SixthGUI.ASSETS_PATH / Path(path)

    def load_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def create_widgets(self):
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

        self.image_1 = self.load_image("image_1.png", 750.0, 392.0)
        self.image_2 = self.load_image("image_2.png", 1416.0, 63.0)
        self.button_2 = Button(
            self.window,
            image=self.image_2,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_2_click,
        )
        self.button_2.place(x=1380.0, y=25.0)

        self.entry_image_1 = self.load_image("entry_1.png", 809.0, 594.5)

        self.entry_1 = Entry(
            bd=0,
            bg="#141416",
            fg="#ffffff",
            font=("Helvetica", 20),
            highlightthickness=0,
        )
        self.entry_1.place(x=179.0, y=430.0, width=1260.0, height=331.0)

        self.image_3 = self.load_image("image_3.png", 824.0, 209.0)
        self.button_3 = Button(
            self.window,
            image=self.image_3,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_3_click,
        )
        self.button_3.place(x=690.0, y=152.0)

    def on_button_2_click(self):
        self.window.destroy()
        from gui_base import GUI

        second_window = GUI(self.shared_data)
        second_window.run()

    def on_button_3_click(self):
        summarizer = ImageSummarizer()
        summarizer.capture_and_save_image()
        output = summarizer.query(os.getcwd() + "\general_image.jpg")
        formatted_output = output[0]["generated_text"].capitalize()
        formatted_output += "."
        self.entry_1.delete(0, "end")
        self.entry_1.insert(0, formatted_output)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = SixthGUI()
    gui.run()
