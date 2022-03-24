from image_combination.utils.io import read_image
from image_combination.processing.transformation import resize_image
from image_combination.processing.combination import find_difference, transfer_histogram
from image_combination.utils.plot import plot_result, plot_histogram

img1 = read_image('https://www.theuniplanet.com/wp-content/uploads/2018/02/floresta.jpg')
img2 = read_image('https://cdn.noticias.ambientebrasil.com.br/wp-content/uploads/2020/05/nature-3294681_1280-1024x576-1.jpg')


img1 = resize_image(img1, 300, 600)
img2 = resize_image(img2, 300, 600)
find_difference(img1, img2)

plot_histogram(img1)
plot_histogram(img2)

combination1 = transfer_histogram(img1, img2)
combination2 = transfer_histogram(img2, img1)

plot_result(img1, img2, combination1)
plot_result(img2, img1, combination2)