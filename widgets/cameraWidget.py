import os
from time import strftime
from kivy.uix.widget import Widget

class CameraWidget(Widget):
    def capture(self):
        camera = self.ids["camera"]
        time_str = strftime("%d-%m-%Y_%H-%M-%S")
        
        if not os.path.exists("./pictures"):
            os.mkdir("./pictures")
            
        camera.export_to_png(f"./pictures/{time_str}.png")
