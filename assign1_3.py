def is_prime(n):
   if n<2:
      return False
   else:
      for i in range(2,n//2+1):
         if n%i==0:
            return False
   return True

LB=int(input("enter lower bound: "))
UB=int(input("enter upper bound: "))
for i in range(LB,UB+1):
   if is_prime(i):
      print(i)