import os
import re
from PIL import Image

metazoa = os.listdir('images/metazoa')

for mimage in metazoa:
    if os.path.isfile('images/metazoa_thumbs/' + mimage):
        continue

    size = (100, 80)
    image = Image.open('images/metazoa/' + mimage)
    image.thumbnail(size, Image.ANTIALIAS)
    background = Image.new('RGB', size, (0, 0, 0))
    background.paste(
        image,
        (int((size[0]-image.size[0]) / 2), int((size[1]-image.size[1]) / 2))
    )
    background.save('images/metazoa_thumbs/' + mimage)
    print(f'Created thumbnail for {mimage}')
