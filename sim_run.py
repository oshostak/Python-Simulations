import random

tries=0
wins=0
lost=0

start_sum=2

def money_function(start_sum):
	pot=start_sum
	a=random.randint(0,1)
	if a==0:
		return(pot)
	if a==1:
		pot1=2*pot
		money_function(pot1)

for i in range(20):
	print("try:",i,"won",money_function(start_sum))
