from PIL import Image

img = Image.open('pineapple.jpeg')
x = 200
y = 200
img = img.resize((x, y))
img_array = list(img.getdata())
new_array = []
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_list = list(ASCII_CHARS)
line_len = x

for i in range(len(img_array)):
    count = 0
    for j in img_array[i]:
        count += j
    avg = int(count / 3)
    new_array.append(avg)
    img_array[i] = avg

#print(img_array)

line_count = 0

for i in range(len(img_array)):
    line_count += 1
    y = int((0.25098 * img_array[i]) + 1)
    print(ascii_list[y], end="")
    print(ascii_list[y], end="")
    print(ascii_list[y], end="")
    if line_count >= x:
        print(' ')
        line_count = 0
