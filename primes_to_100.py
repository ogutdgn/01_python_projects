print(""" 
*** Hello I'am Prime Machine ***
""")
upper = int(input("Enter upper range: "))  
primes = []
un_primes = []
for num in range(1,upper):  
    if num > 1:  
        for i in range(2,num):  
           if (num % i) == 0:  
               break
        else:
           primes.append(num) 
print(primes)      