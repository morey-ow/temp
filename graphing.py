import matplotlib.pyplot as plt

#figure = 
# axes = x,y 

fig1, ax1 = plt.subplots()

x,y=(5,6)  #sets x=5 and y=6
ax1.scatter(x, y)

fig1.savefig('test.png')