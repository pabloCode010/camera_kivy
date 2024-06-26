import os
from time import strftime
from kivy.app import App
from kivy.uix.widget import Widget

class CameraWidget(Widget):
    def capture(self):
        camera = self.ids["camera"]
        time_str = strftime("%d-%m-%Y_%H-%M-%S")
        
        if not os.path.exists("./pictures"):
            os.mkdir("./pictures")
            
        camera.export_to_png(f"./pictures/{time_str}.png")
    
    def switch_to_gallery(self):
        app = App.get_running_app()
        app.root.current = "gallery"

        gallery_widget = app.root.ids["gallery_widget"]
        gallery_widget.ids["container"].clear_widgets()
        gallery_widget.load_daily_photos()
