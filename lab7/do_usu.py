from PIL import Image, ImageChops, ImageFilter

def filter(img, kernel, scale):
    w, h = img.size
    kernel_len = len(kernel)
    img_result = img.copy()
    img_result_table = img_result.load()
    img_table = img.load()
    for i in range(int(kernel_len / 2), w - int(kernel_len / 2)):
        for j in range(int(kernel_len / 2), h - int(kernel_len / 2)):
            tmp = [0, 0, 0]
            for k in range(kernel_len):
                for l in range(kernel_len):
                    x = i + k - int(kernel_len / 2)
                    y = j + l - int(kernel_len / 2)
                    frame = img_table[x, y]
                    for m in range(3):
                        tmp[m] += frame[m] * kernel[k][l]
            img_result_table[i, j] = (int(tmp[0] / scale), int(tmp[1] / scale), int(tmp[2] / scale))
    return img_result


# 2.0
img = Image.open('obraz.jpg')


blur = filter(img, [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], ImageFilter.BLUR.filterargs[1])
# blur.show()