from PIL import Image
im=Image.open("3.gif")
im.save("pic{:02}.png".format(im.tell()))
