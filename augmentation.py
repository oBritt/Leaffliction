
from PIL import Image, ImageFilter
import sys


def get_picture(path):
    try:
        return Image.open(path)
    except Exception:
        return None
    
def rotate(picture: Image.Image) -> Image.Image:
    copy = picture.copy()
    copy = copy.rotate(-22.5)
    return copy

def blur(picture: Image.Image) -> Image.Image:
    copy = picture.copy()
    copy = copy.filter(ImageFilter.BoxBlur(4))

    return copy

def scale(picture: Image.Image, scale=0.7)-> Image.Image:
    copy = picture.copy()
    old_size = copy.size
    new_size = (copy.size[0] * scale, copy.size[1] * scale)
    start = ((old_size[0] - new_size[0]) // 2, (old_size[1] - new_size[1]) // 2)
    copy = copy.crop((start[0], start[1], start[0] + new_size[0], start[1] + new_size[1]))
    copy = copy.resize(old_size)
    return copy

def contrast(picture: Image.Image, contrast_factor=1.5)-> Image.Image:
    copy = picture.copy()
    copy = copy.point(lambda x: (x - 127.5) * contrast_factor + 127.5)
    return copy

def shear(picture: Image.Image, shear_factor = 0.2) -> Image.Image:
    copy = picture.copy()
    copy = copy.transform((picture.width + int(picture.height * shear_factor) , picture.height + int(picture.height * shear_factor)),
                            Image.AFFINE, (1, -1 + 1 / (1 + shear_factor), 0, 0, 1 / (1 + shear_factor), 0))
   
    copy = copy.resize(picture.size)
    return copy


def main() -> None:
    if len(sys.argv) == 1:
        print("Format [augmentation.py]  [picture1] ... [pictureN] ")
        exit(1)
    pictures:list[Image.Image] = []
    for i in range(1, len(sys.argv)):
        picture = get_picture(sys.argv[i])
        if picture is None:
            print(f"Couldnt open {sys.argv[i]}")
            exit(1)
        pictures.append(picture)
    
    for pic in pictures:
        better_pictures = []
        better_pictures.append(rotate(pic))
        better_pictures.append(blur(pic))
        better_pictures.append(scale(pic))
        better_pictures.append(contrast(pic))
        better_pictures.append(shear(pic))

if __name__ == "__main__":
    main()