#list swap 1th and n-1th element.



List = [12,34,56,55,67,89]

# FUNCTION THAT SWAPS 1ST DATA OF THE LIST WIHT THE LAST DATA.SWAP USING INDEX.
def SwapList():
    A = List[-1]
    List[-1] = List[0]
    List[0] = A
    print(List)


SwapList()
    
