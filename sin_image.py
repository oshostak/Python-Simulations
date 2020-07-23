from PIL import Image
import math

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

a = 128
i = 0

for i in range(a):
	image.putpixel((i,i), (255, 0, 0))
	image.putpixel((i,imgy-i-1), (255, 0, 0))
for i in range(a, 2*a):
	image.putpixel((i,2*a-i), (255, 0, 0))
	image.putpixel((i,imgy+i-2*a), (255, 0, 0))
for i in range(2*a, 3*a):
	image.putpixel((i,i-2*a), (255, 0, 0))
	image.putpixel((i,imgy-i-1+2*a), (255, 0, 0))
for i in range(3*a, 4*a-1):
	image.putpixel((i,4*a-i), (255, 0, 0))
	image.putpixel((i,imgy+i-4*a), (255, 0, 0))

image.save('sin_image.png', "PNG")
