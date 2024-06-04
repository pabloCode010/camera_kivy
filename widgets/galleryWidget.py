import os
from datetime import datetime
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
        
        dates  =  [date for date in grouped_files.keys()]
        sorted_dates = sorted(dates, key=lambda date_str: datetime.strptime(date_str, "%d-%m-%Y"),  reverse=True)

        for date in sorted_dates:
            photos_layout = DailyPhotosLayout()
            daily_photos = grouped_files[date]

            container.add_widget(photos_layout)
            photos_layout.add_photos(date, daily_photos)
