

# assign task for each thread. Each thread have id is the index of mapping
# the element is a set (hash table best for finded) of tuple (containes a couple (i,j))
mapping: list[set[tuple[int,int]]] 

# memory table for Dynamic programming approach
m: list[list] 