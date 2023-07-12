#%%
def step_function(x):
    if x>0:
        return 1
    else:
        return 0
#%%

import numpy as np

def step_function(x):
    y=x>0
    # 이 과정에서 모든 값이 bool 형태로 나오게 된다
    return y.astype(np.int)
    # 여기서 int 형으로 바꾸어준다


# %%
import matplotlib.pylab as plt
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()

# %%
import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0,5.0,0.1)
y = relu(x)
plt.plot(x,y)
plt.ylim(-0.1,10)
plt.show()


# %%
X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(X,W1) +B1
# 은닉층에서의 가중치 합을 a라고 한다.
# 이 a가 모인 행렬을 A라고 한다.
# 즉 A는 활성화 함수를 거치기 전의 값 

Z1 = sigmoid(A1)
# z는 활성화 함수를 거친 값이다.

# %%
