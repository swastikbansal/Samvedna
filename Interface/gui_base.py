from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage


class GUI:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets_baseui")

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

        self.image_1 = self.load_image("image_1.png", 750.0, 53.0)
        self.image_2 = self.load_image("image_2.png", 759.0, 447.0)
        self.image_3 = self.load_image("image_3.png", 55.0, 390.0)
        
        self.image_4 = self.load_image("image_4.png", 50.0, 459.0)
        self.button_4 = Button(
            self.window,
            image=self.image_4,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_4_click,
        )
        self.button_4.place(x=20.0, y=420.0)
        
        self.image_5 = self.load_image("image_5.png", 50.0, 260.0)
        self.button_5 = Button(
            self.window,
            image=self.image_5,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_5_click,
        )
        self.button_5.place(x=20.0, y=222.0)
        
        self.image_6 = self.load_image("image_6.png", 50.0, 363.0)
        self.button_6 = Button(
            self.window,
            image=self.image_6,
            bg="#141416",
            borderwidth=0,
            highlightthickness=0,
            command=self.on_button_6_click,
        )
        self.button_6.place(x=20.0, y=320)
        
    def on_button_4_click(self):
        print("Button 4 clicked!")    
    def on_button_5_click(self):
        print("Button 5 clicked!")    
    def on_button_6_click(self):
        print("Button 6 clicked!")    

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
