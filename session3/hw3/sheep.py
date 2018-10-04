flock_size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hong and these are my sheep size")
print(flock_size)
print("*")
print()

max_size = max(flock_size)
print("Now my biggest sheep has size {0} let's shear it".format(max_size))
print("**")
print()

default_size = 8
position = flock_size.index(max_size)
print("After shearing, here is my flock ")
print(flock_size)
print("***")
print()

increase = 50
for i in range(len(flock_size)):
    flock_size[i] += increase
print("One month has passed, now here is my flock:")
print(flock_size)
print("****")
print()

# for k in range(2):
#     print("One month has passed, now here is my flock:")
#     print(flock_size)

#     print("After shearing, here is my flock ")
#     print(flock_size)
#     print("Now my biggest sheep has size", max_size, end='')
    
#     for i in range(len(flock_size)):
#         flock_size[i] += increase
#         print(flock_size)
# print("*****")

# total = 

