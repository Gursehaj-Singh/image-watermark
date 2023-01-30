filename = "original_puppy.jpg"
image = Image.open(filename)
image.show()


width, height = image.size
draw = ImageDraw.Draw(image)

text = "Gursehaj"  # watermarked
font = ImageFont.truetype('arial.ttf', 100)
textwidth, textheight = draw.textsize(text, font)

margin = 40
x = width - textwidth - margin
y = height - textheight - margin

draw.text(xy=(x, y), text=text, font=font)
image.show()
image.save('watermark_puppy.jpg')
