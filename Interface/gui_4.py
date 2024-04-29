from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage


class App:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets_win4")

    def __init__(self, window):
        self.window = window
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        self.window.geometry("1500x780")
        self.window.configure(bg="#141416")
        self.window.resizable(False, False)

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return App.ASSETS_PATH / Path(path)

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

        self.entry_image_1 = self.load_image("entry_1.png", 809.0, 594.5)

        self.entry_1 = Entry(bd=0, bg="#141416", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=179.0, y=430.0, width=1260.0, height=331.0)

        self.image_3 = self.load_image("image_3.png", 824.0, 209.0)


if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()
