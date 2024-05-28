import kivy
kivy.require("2.3.0")

from kivy.app import App
from kivy.uix.camera import Camera

class CameraApp(App):
	def build(self):
		return Camera(play=True)

if __name__ == "__main__":
	CameraApp().run()
