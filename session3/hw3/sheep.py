# 1
flock_sizes = [5, 7, 300, 90, 24, 50, 75]
flock_number = len(flock_sizes)
print("Hello, my name is Hong and these are my ship size")
print(flock_sizes)
print()

# 2
max_size = max(flock_sizes)
print("Now my biggest sheep has size {0} let's shear it".format(max_size))
print()

#3
default_size = 8
position = flock_sizes.index(max_size)
flock_sizes[position] = default_size
print("After shearing, here is my flock:")
print(flock_sizes)
print()

#4
increase_growth = 50
for i in range(flock_number):
    flock_sizes[i] += increase_growth
print("One month has passed, now here is my flock:")
print(flock_sizes)
print()