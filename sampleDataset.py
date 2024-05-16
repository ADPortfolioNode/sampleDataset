# These are the libraries will be used for this lab.

import torch
from torch.utils.data import Dataset
torch.manual_seed(1)


# Define class for dataset

class toy_set(Dataset):
    
    # Constructor with defult values 
    def __init__(self, length = 100, transform = None):
        self.len = length
        self.x = 2 * torch.ones(length, 2)
        self.y = torch.ones(length, 1)
        self.transform = transform
     
    # Getter
    def __getitem__(self, index):
        sample = self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample)     
        return sample
    
    # Get Length
    def __len__(self):
        return self.len
    
    
    
    # Create Dataset Object. Find out the value on index 1. Find out the length of Dataset Object.

our_dataset = toy_set()
print("Our toy_set object: ", our_dataset)
print("Value on index 0 of our toy_set object: ", our_dataset[0])
print("Our toy_set length: ", len(our_dataset))

# Use loop to print out first 3 elements in dataset

for i in range(3):
    x, y=our_dataset[i]
    print("index: ", i, '; x:', x, '; y:', y)
    
    
    for x,y in our_dataset:
        print(' x:', x, 'y:', y)
    
# Practice: Create a new object with length 50, and print the length of object out.

# Type your code here
# Practice: Create a new object with length 50, and print the length of object out.


our_dataset = toy_set(50)
print("Our toy_set object: ", our_dataset)
print("Value on index 0 of our toy_set object: ", our_dataset[0])
print("Our toy_set length: ", len(our_dataset))
      
      
#TRANSFORMS
# Create tranform class add_mult

class add_mult(object):
    
    # Constructor
    def __init__(self, addx = 1, muly = 2):
        self.addx = addx
        self.muly = muly
    
    # Executor
    def __call__(self, sample):
        x = sample[0]
        y = sample[1]
        x = x + self.addx
        y = y * self.muly
        sample = x, y
        return sample
    
# Create an add_mult transform object, and an toy_set object

a_m = add_mult()
data_set = toy_set()

# Use loop to print out first 10 elements in dataset

for i in range(10):
    x, y = data_set[i]
    print('Index: ', i, 'Original x: ', x, 'Original y: ', y)
    x_, y_ = a_m(data_set[i])
    print('Index: ', i, 'Transformed x_:', x_, 'Transformed y_:', y_)
    
    
# Create a new data_set object with add_mult object as transform
# Use loop to print out first 10 elements in dataset
# Practice: Construct your own my_add_mult transform. Apply my_add_mult on a new toy_set object. Print out the first three elements from the transformed dataset.

new_toy_set = toy_set(50)
my_add_mult = add_mult()


new_toy_set = toy_set(transform = my_add_mult)
new_toy_setLimit = new_toy_set.len

for i in range(new_toy_setLimit):
    x, y = new_toy_set[i]
    print('Index: ', i, 'Original x: ', x, 'Original y: ', y)
    x_, y_ = my_add_mult(new_toy_set[i])
    print('Index: ', i, 'Transformed x_:', x_, 'Transformed y_:', y_)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>End of Line<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")