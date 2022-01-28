import matplotlib.pyplot as plt
import numpy as np

def add1(n):
	total=0
	for i in range(1, n+1):
		total=total+i
	return total

def add2(n):
	return sum(range(1, n+1))


if __name__=='__main__':
	x=np.arange(1,100)
	y=np.array([add1(i) for i in x])
	plt.scatter(x, y)