import kivy
kivy.require("2.3.0")

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

Factory.register("CameraWidget", module="widgets.camera_widget")

class CameraApp(App):
	def build(self):
		Builder.load_file("kv_files/CameraWidget.kv")
		
		screen_manager = Builder.load_file("screen_manager.kv")
		return screen_manager

if __name__ == "__main__":
	CameraApp().run()
