def repeat(n, sym): 
  if n <= 0:
    return '' 
  else:
    half = n // 2
    part = repeat(half, sym)
    res = part + sym
    return res

n = 5
sym = '*'
s = repeat(n, sym)
