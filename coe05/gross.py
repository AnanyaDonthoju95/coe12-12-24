basic=int(input("Enter salary:"))
if(basic<10000):
    hra=67%100*basic
    da=73%100*basic
elif(basic<20000):
    hra=69%100*basic
    da=76%100*basic
elif(basic>20000):
    hra=73%100*basic
    da=89%1010*basic
gs=hra+da+basic
print("The gross salary:",gs)