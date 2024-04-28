from pathlib import Path
from tkinter import Tk, Canvas, Entry, PhotoImage, Button


class FourthGUI:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets_win3")

    def __init__(self, shared_data=None):
        self.window = Tk()
        self.window.geometry("1500x780")
        self.window.configure(bg="#141416")
        self.window.resizable(False, False)
        self.shared_data = shared_data

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
        self.entry_1 = Entry(bd=0, bg="#141416", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=194.0, y=534.0, width=540.0, height=218.0)

    def on_button_2_click(self):
        print("Button 2 clicked!")

    def on_button_3_click(self):
        print("Button 3 clicked!")

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
