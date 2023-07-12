import matplotlib.pylab as plt
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(X,W1) +B1
# 은닉층에서의 가중치 합을 a라고 한다.
# 이 a가 모인 행렬을 A라고 한다.
# 즉 A는 활성화 함수를 거치기 전의 값 
# x는 입력 신호 값이며
# w는 그에 해당하는 가중치이다
# 거기에 편향을 더하여 값을 구한다

Z1 = sigmoid(A1)
# z는 활성화 함수를 거친 값이다.