# How to make a list from some elements, 
#     where some of the elements are lists, 
#     while the others are not?

vals = list(); 
for val in [0, [1,2], [3,4], [5,6], [7,8,9]]: vals.extend(val) if isinstance(val, list) else vals.append(val)
print(vals)

'''
Output: 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''