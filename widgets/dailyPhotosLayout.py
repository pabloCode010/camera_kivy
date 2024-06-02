from kivy.uix.boxlayout import BoxLayout
from widgets.galeryImage import GaleryImage

class DailyPhotosLayout(BoxLayout):
    def add_photos(self, date_str: str, img_files: list):
        label_date = self.ids["label_date"]
        photos_grid = self.ids["photos_grid"]

        for image_file in img_files:
            image = GaleryImage(source = f"./pictures/{image_file}")
            label_date.text = date_str
            photos_grid.add_widget(image)
