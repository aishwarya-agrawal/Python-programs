l = int(input("Enter a lower number: "))
h = int(input("Enter a upper number: "))
print("Following numbers are Armstrong number between lower and upper:")
for i in range(l,h):
  order = len(str(i))
  sum = 0
  temp = i
  while temp>0:
    digit = temp%10
    sum+=digit**order
    temp//=10
  if i == sum:
      print(i)
