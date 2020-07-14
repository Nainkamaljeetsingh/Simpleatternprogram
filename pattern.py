str1=True
def pat1():
    num=int(input('enter the number of rows '))
    for i in range(0,num):
      for j in range(0,i):
          print('*',end=' ')
      print()
    
def pat2():
    num=int(input('enter the number of rows '))
    for i in range(0,num):
        for j in range(num,i,-1):
            print('*',end=' ')
        print()

def pat3():
    num=int(input('enter the number of rows '))
    for i in range(0,num):
        for j in range(0,i):
            print('*',end=' ')
        print('')
    for i in range(0,num*2):
        for j in range(num-2,i,-1):
            print('*',end=' ')
        print('')

def pat4():
        num=int(input('enter the number of rows '))
        for i in range(0,num):
            for j in range(num,i,-1):
                print(' ',end='')
            for k in range(0,i):
                print('*',end='')
            print('')
    
def pat5():
    num=int(input('enter the number of rows '))
    for i in range(0,num):
        for j in range(0,i):
            print(' ',end=' ')
        for k in range(0,num-i):
            print('*',end=' ')
        print()    
            
 
def pat6():
    num=int(input('enter the number of rows '))
    for i in range(0,num):
        for j in range(num,i,-1):
            print(' ',end='')
        for k in range(0,i):
            print('*',end='')
        print()
    for i in range(0,num):
        for j in range(0,i):
            print(' ',end='')
        for k in range(0,num-i):
            print('*',end='')
        print()


def pat7():
        num=int(input('enter the number of rows '))
        for i in range(0,num):
            for j in range(num,i,-1):
                print(' ',end='')
            for k in range(0,i):
                print(' *',end='')
            print('')
   
def pat8():
    num=int(input('Enter the no of number of rows'))
    for i in range(0,num):
        for j in range(num,i,-1):
            print(' ',end=' ')
        for k in range(0,i):
            print('*',end=' ')
        for l in range(1,i):
            print('*',end=' ')
        print()

def pat8a():
    num=int(input('Enter the no of number of rows'))
    for i in range(0,num):
        for j in  range(num,i,-1):
            print(' ',end=' ')
        for k in range(1,2*i):
            print('*',end=' ')
        print()

def pat9():
    num=int(input('enter the number of rows '))
    for i in range(0,num):
        for j in range(0,i):
            print(' ',end=' ')
        for k in range(0,num-i):
            print('*',end=' ')
        for j in range(num*1,i,-1):
            print('*',end=' ')
        print()
   

def pat10():
    num=int(input('Enter the no of number of rows'))
    for i in range(0,num):
        for j in  range(num,i,-1):
            print(' ',end=' ')
        for k in range(1,2*i):
            print('*',end=' ')
        print()
    for i in range(0,num):
        for j in range(0,i):
            print(' ',end=' ')
        for k in range(0,num-i):
            print('*',end=' ')
        for j in range(num-1,i,-1):
            print('*',end=' ')
        print()

def pat11():
    str1=int(input('enter 1 to terminate othewise 0......'))
    return str1
def pat12():
    num=int(input('enter the no of rows'))
    for i in range(num):
        for j in range(num):
           if i>0 and i<num-1 and j>0 and j<num-1:
             print(' ',end=' ')
           elif(i==0 and j==0) or (i==num-1 and j==num-1) or (i==num-1 and j==0) or(i==0 and j==num-1):
             print(' ',end=' ')
           else:
             print('*',end=' ')
        
        print()
def pat13():
    num=int(input('enter the no of rows'))
    for i in range(num):
        for j in range(num):
            if i<=num//2:
                if i==j:
                  print('*',end='')
                elif i+j==num-1:
                  print('*',end='')
                else:
                  print(' ',end='')
        print()
def pat14():
    num=int(input('enter the no of rows'))
    for i in range(num):
        for j in range(num):
            if i>=num//2:
                if i==j:
                  print('*',end='')
                elif i+j==num-1:
                  print('*',end='')
                else:
                  print(' ',end='')
        print()
def pat15():
    num=int(input('enter the no of rows'))
    while True:
     for i in range(num):
         for j in range(num):
            if i==j:
              print('*',end='')
            elif i+j==num-1:
              print('*',end='')
            else:
              print(' ',end='')
         print()
     for i in range(num):
         for j in range(num):
            if i==j:
              print('*',end='')
            elif i+j==num-1:
              print('*',end='')
            else:
              print(' ',end='')
         print()     
while str1:
    try:
     pat1()
     pat2()
     pat3()
     pat4()
     pat5()
     pat6()
     pat7()
     pat8()
     pat8a()
     pat9()
     pat10()
     pat12()
     pat13()
     pat14()
     pat15()
     k=pat11()
     if k==1:
         break
     print('task over')
    except:
      print('please enter the valid row number')