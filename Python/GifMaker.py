import imageio
filenames = ["1.png", "3.png","4.png"] #you can add any type of image
images = []
for filename in filenames:
  images.append(imageio.imread(filename))
imageio.mimsave('ritesh1.gif', images, 'GIF', duration=1)
