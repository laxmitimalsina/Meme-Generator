"""Takes a image and adds caption to the image."""

import textwrap
import uuid
from PIL import Image, ImageDraw, ImageFont


class ImageCaptioner:
    """This class has following fuctionalities to load image.

    Resize image, add caption,save modified image
    """

    def __init__(self, export_dir):
        """Instantiate ImageCaptioner class."""
        self.export_dir = export_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Load image using PIL library,resize image.

        Add text using quote body, author and save image,
        the path where its saved will be returned.
        If file not found will raise FileNotFound error and if
        unsupported file format is used, raise UnidentifiedImageError.
        """
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

            author_font = ImageFont.truetype("./_data/Font/Amatic-Bold.ttf", size=30,)
            # draw.text((20, 30), text, font=font, fill="white")
            draw.text(
                (width - 200, height - 100), author, font=author_font, fill="white",
            )
            file_name = uuid.uuid4().hex
            out_path = f"{self.export_dir}/{file_name}.jpg"
            image.save(out_path)

        return out_path
