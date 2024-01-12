# coding: utf-8

x = 1
s = 0 


while True:

    s = s + x
    c = 0
    x = x +1

    for i in range(1,int(s ** 0.5+1)):

        if s%i == 0:
            c = c + 1
            if i*i != s:
                c = c+1


    if c>500:
        print(s,c)
        break


    
    




    
    


    

    


    
    


    
