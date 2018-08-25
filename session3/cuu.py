# 1
flock_sizes = [5, 7, 300, 90, 24, 50, 75]
flock_num = len(flock_sizes)
print("Hello, my name is Hong and these are my ship sizes: ")
print(flock_sizes)
print()

#2
max_size = max(flock_sizes)
print("Now my biggest sheep has size {0} let's shear it".format(max_size))
print()

#3
default_size = 8
max_size_position = flock_sizes.index(max_size)
flock_sizes[max_size_position] = default_size
print("After shearing, here is my flock:")
print(flock_sizes)
print()

#4
monthly_growth = 50
for i in range(flock_num):
    flock_sizes[i] += monthly_growth
print("One month has passed, now here is my flock:")
print(flock_sizes)
print()