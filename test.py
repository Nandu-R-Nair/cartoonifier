import cv2 #image procesing
import easygui #open file box
import os
import matplotlib.pyplot as plt

#ImagePath = easygui.fileopenbox()
#newPath = ImagePath.replace(os.sep, '/')
#print(newPath)
#newPath = "C:/Users/91902/PycharmProjects/imagecartoonifier/girl.jpg"
image = cv2.imread("C:/Users/91902/PycharmProjects/imagecartoonifier/girl.jpg")
ReSized2 = cv2.resize(image, (960, 540))
plt.imshow(ReSized2, cmap='gray')
plt.show()

#cv2.imshow('graycsale image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


