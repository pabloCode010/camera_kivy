from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

Factory.register("CameraWidget", module="widgets.cameraWidget")
Factory.register("GaleryWidget", module="widgets.galeryWidget")
Factory.register("DailyPhotosLayout", module="widgets.dailyPhotosLayout")
Factory.register("GaleryImage", module="widgets.galeryImage")

class CameraApp(App):
	def build(self):
		Builder.load_file("kv_files/CameraWidget.kv")
		Builder.load_file("kv_files/GaleryWidget.kv")
		Builder.load_file("kv_files/DailyPhotosLayout.kv")
		Builder.load_file("kv_files/GaleryImage.kv")
		
		screen_manager = Builder.load_file("screen_manager.kv")
		return screen_manager

	def on_start(self):
		galery_widget = self.root.ids["galery_widget"]
		galery_widget.load_daily_photos()

if __name__ == "__main__":
	CameraApp().run()
