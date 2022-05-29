from PIL import Image
from PIL import ImageDraw
from PIL import ImageFilter
from PIL import ImageFont


def filterImage(im, filter):
    if filter == 'BLUR':
        im = im.filter(ImageFilter.BLUR)
    elif filter == 'CONTOUR':
        im = im.filter(ImageFilter.CONTOUR)
    elif filter == 'DETAIL':
        im = im.filter(ImageFilter.DETAIL)
    elif filter == 'EMBOSS':
        im = im.filter(ImageFilter.EMBOSS)
    elif filter == 'EDGE_ENHANCE_MORE':
        im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter == 'FIND_EDGES':
        im = im.filter(ImageFilter.FIND_EDGES)
    elif filter == 'SHARPEN':
        im = im.filter(ImageFilter.SHARPEN)
    elif filter == 'SMOOTH':
        im = im.filter(ImageFilter.SMOOTH)
    return im


def resize(photo, size):
    if size == '1920x1080':
        im = photo.resize((1920, 1080))
    elif size == '1280x720':
        im = photo.resize((1280, 720))
    elif size == '1080x1080':
        im = photo.resize((1080, 1080))
    elif size == '720x720':
        im = photo.resize((720, 720))
    elif size == '640x360':
        im = photo.resize((640, 360))
    return im


def waterMark(photo, waterMark):
    width, height = photo.size

    draw = ImageDraw.Draw(photo)
    text = waterMark
    font = ImageFont.truetype("arial.ttf", 82)

    textwidth, textheight = draw.textsize(text, font)

    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, fill=(0, 0, 255), font=font)

    return photo


def rotate(photo, angle):
    if angle == 0:
        im = photo.rotate(0)
    elif angle == 45:
        im = photo.rotate(45)
    elif angle == 90:
        im = photo.rotate(90)
    elif angle == 180:
        im = photo.rotate(180)
    elif angle == 270:
        im = photo.rotate(270)
    elif angle == 360:
        im = photo.rotate(360)
    return im
