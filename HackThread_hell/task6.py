def mutate_string(string,position,character):
  l = list(string)
  l[5] = 'k'
  string = ''.join(l)   
  print(string)


mutate_string("abracadabra", 5 ,'k')