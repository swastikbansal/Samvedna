from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from gui_win2 import ThirdGUI
from gui_win3 import FourthGUI
import threading

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from model_execute import Model

class SecondGUI:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets_win1")

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

        self.image_1 = self.load_image("image_1.png", 750.0, 80.0)

        self.image_2 = self.load_image("image_2.png", 1406.0, 81.0)
        self.button_2 = Button(
            self.window,
            image=self.image_2,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_2_click,
        )
        self.button_2.place(x=1370.0, y=40.0)

        self.image_3 = self.load_image("image_3.png", 827.0, 478.0)

        self.image_4 = self.load_image("image_4.png", 496.0, 534.0)
        self.button_4 = Button(
            self.window,
            image=self.image_4,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_4_click,
        )
        self.button_4.place(x=345.0, y=380.0)

        self.image_5 = self.load_image("image_5.png", 1148.0, 534.0)
        self.button_5 = Button(
            self.window,
            image=self.image_5,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_5_click,
        )
        self.button_5.place(x=1000.0, y=385.0)

        self.image_6 = self.load_image("image_6.png", 70.0, 390.0)

    def on_button_2_click(self):
        self.window.destroy()
        from gui_base import GUI

        second_window = GUI(self.shared_data)
        second_window.run()

    def on_button_4_click(self):
        self.window.destroy()
        model = Model()
        # model.execute()
        second_window = ThirdGUI(self.shared_data)
        # second_window.run()
        
        thread1 = threading.Thread(target=model.execute)
        thread1.start()
        
        thread2 = threading.Thread(target=second_window.run)
        thread2.start()

    def on_button_5_click(self):
        self.window.destroy()
        
        second_window = FourthGUI(self.shared_data)
        second_window.run()

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return SecondGUI.ASSETS_PATH / Path(path)

    def load_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = SecondGUI()
    gui.run()
