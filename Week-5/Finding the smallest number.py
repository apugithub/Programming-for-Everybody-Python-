### Findiding the smallest number
smallest=None
for value in [3,50,1,78,5]:
  if smallest is None:
    smallest=value
  elif value<smallest:
    smallest=value
    
print (" Smallest is: "), smallest    
    
    
