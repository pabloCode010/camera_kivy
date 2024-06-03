from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup

class GalleryImage(ButtonBehavior, Image):
    def show_image(self):
        popup_content = Image(
            source = self.source)

        popup = Popup(
            title = 'Image',
            content = popup_content,
            size_hint = (None, None),
            size = (self.parent.width, 800)
        )

        popup.open()