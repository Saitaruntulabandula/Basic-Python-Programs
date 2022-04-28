def max_min_function(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min_function([-145,65,-30,86,43,0,145,93]))