# %%
import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0,6,0.1) # 0에서 6까지 0.1단위로 생성
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x,y1,label = "sin")
plt.plot(x,y2,linestyle="--",label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()
# %%
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('ex1.jpg') # 이미지 읽어오기

plt.imshow(img)
plt.show()

# %%