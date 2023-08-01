string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
num=4
l=int(len(string)/num)
temp1=0
for i in range(l+1):
  s=""
  temp2=temp1+num
  s=s+string[temp1:temp2]
  temp1=temp2
  print(s)
