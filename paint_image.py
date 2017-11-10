# coding = utf8
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('C:\\Users\\USER\\Downloads\\sample.png'))  #打开图像并转化为数字矩阵
plt.figure("prairie")
plt.imshow(img)
plt.axis('off')
plt.show()

print(img.shape)
print (img.dtype)
print (img.size)
print( type(img))