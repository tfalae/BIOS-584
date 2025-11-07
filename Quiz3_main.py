from self_py_fun.Quiz3Fun import *

# You can use this .py script to perform debugging task.
sample_arr_1 = np.array([1,2,3,4,5])
d_1 = compute_D_partial(sample_arr_1)
# The correct d_1 should be 5.66.

# Step 1: define the sample array
sample_arr_2 = np.array([1, 2, 3, 5, 6])

# Step 2: call the function and store the result
d_val_2 = compute_D_correct(sample_arr_2)

# Step 3: print the result
print("Answer:", d_val_2)

