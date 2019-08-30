from PIL import Image, ImageDraw, ImageFont
from random import randint


no = 300
fontsize = 40

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


for m in range(no):
    font = ImageFont.truetype("arial.ttf", fontsize)
    img = Image.new('RGB', (320, 320), color=(0+m, 0+m*1, 0+m*2))
    d = ImageDraw.Draw(img)
    d.text((10,50), str('+91')+str(random_with_N_digits(10)), font=font, fill=(255, 255, 255))
    img.save('/home/navaneeth/work/OCR-darknet/images/'+str(m)+'.png')
