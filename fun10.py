def slicer(seq, start=None, stop=None, step=None): 
    return seq[start:stop:step] 

d = 'abcdefghijklmnopqrstuvwxyz'
print(slicer(d,2))
print(slicer(d,2,10))
print(slicer(d,2,10,2))
print(slicer(d,step=2))