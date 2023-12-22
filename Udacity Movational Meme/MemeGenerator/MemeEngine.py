"""
Creating a meme with a given image.

Text - quote and author - randomly placed inside the image.
"""

from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap


class MemeEngine():
    """Loads image to create meme."""

    def __init__(self, output_dir):
        """Create output file."""
        self.output_dir = output_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        """Create meme and stores in output file."""
        img = Image.open(img_path)

        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        rand_x = random.randint(0, int(width/2))
        rand_y = random.randint(0, int(height/2))

        text = text.replace("\u2019", "")
        author = author.replace("\u2019", "")
        wrapper = textwrap.TextWrapper(width=50)
        wrapped_text = wrapper.fill(text=text)

        draw = ImageDraw.Draw(img)
        draw.text((rand_x, rand_y), wrapped_text, fill='white')
        draw.text((rand_x, (rand_y+30)), ('   -'+author), fill='white')

        out_file = (self.output_dir+'/'+str(random.randint(0, 1000))+'.jpg')

        img.save(out_file, "JPEG")
        return (out_file)
