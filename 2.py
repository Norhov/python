x=0
z=0
qanak=0
while x!="done":
    
    x=input()
    if x.isdecimal():
      
        qanak=qanak+1
        z=int(x)+z
    if x.isdecimal()==False and x!="done":
        print('pleas input only numbers or (done)')
print('gumar',z)    
print(qanak,"qanak")    
print('mijin tvabanakan',z/qanak)



