l1 = input()
l1 = [x for x in l1.split(',')]
l2 = input()
l2 = [x for x in l2.split(',')]
for i in l1:
  for j in l2:
    print("(",i,",",j,")")
