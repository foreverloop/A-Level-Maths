#basic revision of graphing linear equations
from matplotlib import pyplot as plt

x = range(-100,100)
y = [3 * z - 6 for z in x]
yq2 = [10 - (2 * z) for z in x]

#value 100 in x = 0, so we get the y intercept at this same point in y or yq2
for idx,axis_point in enumerate(y):
    if idx == 100:
        print "orange line passes y axis at {0}".format(axis_point)

for idx,axis_point in enumerate(yq2):
    if idx == 100:
        print "blue line passes y axis at {0}".format(axis_point)

plt.plot(x,yq2,color='blue')
plt.plot(x,y,color='orangered')
plt.title('Baisc Linear Equations')
plt.show()