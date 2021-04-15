from file_exception import file_exception
import textwrap
import uuid
import os
from PIL import Image, ImageDraw, ImageFont


class ImageCaptioner:
    """This class has following fuctionalities to load image,
    resize image, add caption,save modified image
    """

    def __init__(self, export_dir):
        self.export_dir = export_dir
        self.extensions = [".jpg", ".png"]

    def make_meme(self, img_path, text, author, width=500) -> str:
        """load image using PIL library, resize image,
        add text using quote body, author and save image"""

        image = Image.open(img_path)

        if width is not None:
            ratio = width / image.size[0]
            height = int(ratio * float(image.size[1]))
            image = image.resize((width, height), Image.LANCZOS)
        else:
            width, height = image.size

        if text is not None:
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("./_data/Font/Amatic-Bold.ttf", size=40)
            y_text = 50
            lines = textwrap.wrap(text, width=30)
            for line in lines:
                line_width, line_height = font.getsize(line)
                draw.text(
                    ((width - line_width) / 2, y_text), line, font=font, fill="white",
                )
                y_text += line_height

            author_font = ImageFont.truetype("./_data/Font/Amatic-Bold.ttf", size=30)
            # draw.text((20, 30), text, font=font, fill="white")
            draw.text(
                (width - 200, height - 100), author, font=author_font, fill="white"
            )
            if not os.path.exists(self.export_dir):
                raise file_exception.InvalidFilePath(self.export_dir)
            file_name = uuid.uuid4().hex
            out_path = f"{self.export_dir}/{file_name}.jpg"
            image.save(out_path)

        return out_path
