import textwrap
from PIL import Image, ImageDraw, ImageFont
from aiogram.types import FSInputFile
import os


def create_form(lost_name_id, born, regions, description, feature, spec_feature, clothes, items, photo):
    image = Image.open(r"data\empty-form.jpg")
    drawer = ImageDraw.Draw(image)
    im2 = Image.open(f'photo{photo}.jpg')
    im2_n = im2.resize((290, 390))

    image.paste(im2_n, (75, 80))

    font = ImageFont.truetype("calibri.ttf", 50)
    name = lost_name_id.split(" ")
    if len(name) != 3:
        drawer.text((418, 60), f"{lost_name_id}", font=font, fill='black')
    else:
        drawer.text((418, 60), f"{name[0].upper()}\n{name[1].upper()} {name[2].upper()}", font=font, fill='black')

    font = ImageFont.truetype("calibri.ttf", 25)
    drawer.text((418, 145), f"{born} г. р.", font=font, fill='black')

    font = ImageFont.truetype("calibri.ttf", 25)
    drawer.text((418, 165), f"{regions}", font=font, fill='red')

    font = ImageFont.truetype("calibri.ttf", 25)
    lines = textwrap.wrap(description, width=50)
    y = 188
    for line in lines:
        drawer.text((418, y), line, font=font, fill="red")
        y += 20

    font = ImageFont.truetype("calibri.ttf", 35)
    lines = textwrap.wrap(feature, width=35)
    y = 272
    for line in lines:
        drawer.text((418, y), line, font=font, fill="black")
        y += 25

    font = ImageFont.truetype("calibri.ttf", 35)
    drawer.text((418, 375), f"{spec_feature}", font=font, fill='black')

    font = ImageFont.truetype("calibri.ttf", 35)
    lines = textwrap.wrap(clothes, width=35)
    y = 445
    for line in lines:
        drawer.text((418, y), line, font=font, fill="black")
        y += 25

    font = ImageFont.truetype("calibri.ttf", 35)
    lines = textwrap.wrap(items, width=35)
    y = 530
    for line in lines:
        drawer.text((418, y), line, font=font, fill="black")
        y += 25

    image.save(f"image{photo}.jpg")
    res = FSInputFile(f"image{photo}.jpg")
    os.system(f"del photo{photo}.jpg")
    return res
