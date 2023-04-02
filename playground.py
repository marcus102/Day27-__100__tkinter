def add(*args):
  result = 0
  for num in args:
    result += num
  return f'The result is {result}'
  
addition =  add(1, 2, 4, 5, 29, 49, 100)
print(addition)