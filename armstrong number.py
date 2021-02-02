i=int(input("enter number:"))
orignal=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
    if (orignal==sum):
        print("number is armstrong")
    else:
        print("number is not rmstrong")