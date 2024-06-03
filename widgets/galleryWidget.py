import os
from kivy.uix.widget import Widget
from widgets.dailyPhotosLayout import DailyPhotosLayout

def group_by_date(img_files) -> dict:
    groups = {}

    for image_file in img_files:
        date = image_file.split("_")[0]
        if date not in groups:
            groups[date] = []
        
        groups[date].append(image_file)
    
    return groups

class GalleryWidget(Widget):
    def load_daily_photos(self):
        container = self.ids["container"]
        
        if not os.path.exists("./pictures"):
            os.mkdir("./pictures")

        img_files = os.listdir("./pictures")
        grouped_files = group_by_date(img_files)

        for date in grouped_files:
            photos_layout = DailyPhotosLayout()
            daily_photos = grouped_files[date]

            container.add_widget(photos_layout)
            photos_layout.add_photos(date, daily_photos)
