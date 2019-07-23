def is_prime(n):
   if n<2:
      return False
   else:
      for i in range(2,n//2+1):
         if n%i==0:
            return False
   return True
n=[i for i in range(1,201)]
lst=list(filter(is_prime,n))
print(lst)
 

