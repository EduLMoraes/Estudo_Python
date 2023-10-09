from ast import Import


from rembg import remove
from PIL import Image

img = input('Coloque o diretório da imagem')
img = remove(img)
img.save('~/Imagens')