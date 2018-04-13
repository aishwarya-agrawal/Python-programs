a = 0
v = 0
s = 0
d = 0
sen = input("Enter a Sentence")
l = len(sen)
for i in sen:
  if ord(i) in range(65,90) or ord(i) in range(97,122):
    a =a+1
  if i=='a' or i =='e' or i=='o' or i=='u' or i == 'i' :
    v = v+1
  if ord(i) in range(48,57):
    d = d+1
  if ord(i) in range(32,47):
    s= s+1
print("no of alphabets=",a)
print("no of vowels=",v)
print("no of special characters=",s)
print("no of digits=",d)
print("length of string=",l)
