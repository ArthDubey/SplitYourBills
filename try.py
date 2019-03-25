import math
import os,sys
def transoccurmulti(frndpd,amt,totamt,payms):     #Multiple friends gave contribution
    mn=totamt/len(friends)
    for i in range(0,len(payms)):
        payms[i]=payms[i]+mn
    for i in range(0,len(friends)):
        for j in range(0,len(frndpd)):
            if(friends[i]==frndpd[j]):
                payms[i]=payms[i]-amt[j]
    return payms


def addfriends(friends,payms,frnd):
    friends.append(frnd)
    payms.append(0)
    return friends,payms


def removefriends(friends,payms,frnd):
    friends.delete(frnd)
    payms.delete(0)
    return friends,payms    


def perspec(persp,paymsy):
    for i in range(0,len(friends)):
        if(friends[i]==persp):
            t=i
            val=paymsy[i]
    for i in range(0,len(friends)):
        if(i!=t):
            if(paymsy[i]<val):
                print(friends[i]+" Needs to recieve "+str((val-paymsy[i])/2)+" rupees from you.")
            elif(paymsy[i]>val):    
                print(friends[i]+" Needs to pay "+str((paymsy[i]-val)/2)+" rupees to you.")
            else:
                print("Records are equal with "+friends[i])


#Code starts
total=[]
friends=['a','b','c','d']
paym=[0,0,0,0]  #Total sum
#paym=transoccurmulti(['a','c','d'],[100,50,50,20],220,paym)       
#perspec('a',paym)
print("----WELCOME TO THE CONSOLE BASED APPLICATION-----")
while True:
    print("What do you wish to do\n1. Register an occured transaction\n2. Check records from your (or a friend's) perspective\n3. Exit")
    pl=int(input())
    if(pl==1):
        print("Please enter the total amount:")
        totamt=int(input())
        print("Please enter the name of the friends who have paid (with spaces in between)")
        frndpd=list(map(str,input().split()))
        print("Please enter the amount that the friends have paid respectively (with spaces in between)")
        amt=list(map(int,input().split()))
        paym=transoccurmulti(frndpd,amt,totamt,paym)
        print(paym)
    elif(pl==2):
        print("whose perspective do you want?")
        ro=input() 
        perspec(ro,paym)
    elif(pl==3):
        sys.exit()

