import numpy as np

def calculate(list):
    # Requirement: If a list containing less than 9 elements is passed, raise a ValueError.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list into a 3x3 Numpy array
    matrix = np.array(list).reshape((3, 3))
    
    # Calculate statistics and convert Numpy array results back to Python lists using .tolist()
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum().tolist()
        ]
    }
    
    return calculations

import mean_var_std
from pprint import pprint

# This matches the example from the instructions
print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
