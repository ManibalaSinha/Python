#math module gives access for floating point math
import math
print(math.cos(math.pi/4))
print(math.log(1024, 2))# log(1024) of base 2
#random module provides tools for making random selections
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))   # sampling without replacement
print(random.random())    # random float
print(random.randrange(6))    # random integer chosen from range(6)
#statistics module calcuates basic statistical properties(mean, median, variance)
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))#mean is avg of numbers
print(statistics.median(data))# median is halfway into the set.
print(statistics.variance(data))#for each number,subtract the Mean and square the squared difference,
#then find out the average of those squared differences.