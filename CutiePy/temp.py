def prime_number(n):
  flag = 0
  it = 2
  while it <= n/2:
    if n % it == 0:
      flag = 1
      break
    it += 1
  if flag == 0:
    print(n, end = ' ')

for i in range(2, 100):
  prime_number(i)