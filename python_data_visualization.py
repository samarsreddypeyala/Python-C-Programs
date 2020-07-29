# Python Program illustrating numpy.linalg.lstsq() method
import numpy as np
# importing matplotlib module
from matplotlib import pyplot as plt
#x coordinatea
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])
#linearly generated sequence
y= [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
#obtaining the parameters of regression line
w= np.linalg.lstsq(A.T, y)[0]
# plotting the line
line = w[0]*x + w[1] # regression line
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.title('regression line')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
a=[1,2,3,4,5]
# x-axis values
x = [5, 2, 9, 4, 7]
# Y-axis values
y = [10, 5, 8, 4, 2]
# Function to plot
plt.plot(x,y)
# function to show the plot
plt.title('info plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
# Function to plot the bar
plt.bar(x,y)
# function to show the plot
plt.title('bar graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
# Function to plot histogram
plt.hist(y)
# Function to show the plot
plt.title('histogram')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
# Function to plot scatter
plt.scatter(x, y)
plt.title('scatter')
plt.xlabel('X axis')
plt.ylabel('Y axis')
# function to show the plot
plt.show()
#stack plot i.e how much covered area
plt.stackplot(a,x,y)
plt.title('stackplot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
#pie chart i.e percent of each in total
plt.pie(a,autopct='%1.1f%%',labels=['1','2','3','4','5'])
plt.title('pie chart')
plt.show()