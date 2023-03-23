# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do python
from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGEM = ROOT_FOLDER / 'new.JPG'


pil_imagem = Image.open(ORIGINAL)
width, height = pil_imagem.size
exif = pil_imagem.info['exif']


# width    new_widht
# height   new_height

new_width = 640
new_height = round(height * new_width / width)


new_image = pil_imagem.resize(size=(new_width, new_height))

new_image.save(
    NEW_IMAGEM,
    optimize=True,
    quality=100,
    exif=exif,
)
