import math
tree = [54, -1, 9, 6]

strsize = 2 ** len(tree)
levels = len(tree)
current_level = 0
i = 0
 
level0 = [' ' * (levels-current_level) ** 2, str(tree[0]),' '* (levels-current_level) ** 2]
print(' '.join(i for i in level0))
current_level += 1
tree = tree[2**i:]
i = 1
level1_elem = tree[2**(i-1)-1:2**i]
level1 = [' ' * (levels-current_level) ** 2,(' ' * (levels-current_level) ** 2).join(str(i) for i in level1_elem),' ' *(levels-current_level) ** 2]
print(' '.join(i for i in level1))

tree = tree[2**i:]
i = 2
current_level += 1
level2 = [' ' * (levels-current_level) ** 2, str((' ' * (levels - current_level) ** 2).join(str(i) for i in tree[2*i+1])), ' ' * (levels-current_level) ** 2]
print(' '.join(i for i in level2))
