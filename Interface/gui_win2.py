from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage, Button


class GUI:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets_win2")

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1500x780")
        self.window.configure(bg="#141416")
        self.window.resizable(False, False)

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

        self.image_1 = self.load_image("image_1.png", 750.0, 92.0)
        self.image_2 = self.load_image("image_2.png", 60.0, 392.0)

        self.image_3 = self.load_image("image_3.png", 1416.0, 57.0)
        self.button_3 = Button(
            self.window,
            image=self.image_3,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_3_click,
        )
        self.button_3.place(x=1385.0, y=20.0)

        self.image_4 = self.load_image("image_4.png", 806.0, 429.0)

        self.entry_image_1 = self.load_image("entry_1.png", 806.0, 724.0)
        self.entry_1 = Entry(bd=0, bg="#141416", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=176.0, y=685.0, width=1260.0, height=78.0)

    def on_button_3_click(self):
        print("Button 3 clicked!")

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return GUI.ASSETS_PATH / Path(path)

    def load_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run()
