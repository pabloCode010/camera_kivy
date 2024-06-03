from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

Factory.register("CameraWidget", module="widgets.cameraWidget")
Factory.register("GalleryWidget", module="widgets.galleryWidget")
Factory.register("DailyPhotosLayout", module="widgets.dailyPhotosLayout")
Factory.register("GalleryImage", module="widgets.galleryImage")

class CameraApp(App):
	def build(self):
		Builder.load_file("kv_files/CameraWidget.kv")
		Builder.load_file("kv_files/GalleryWidget.kv")
		Builder.load_file("kv_files/DailyPhotosLayout.kv")
		Builder.load_file("kv_files/GalleryImage.kv")
		
		screen_manager = Builder.load_file("screen_manager.kv")
		return screen_manager

if __name__ == "__main__":
	CameraApp().run()
