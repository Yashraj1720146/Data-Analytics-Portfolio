import numpy as np


#without broadcasting 
# prices = [100, 200, 300]
# discount = 10  
# final_prices = []

# for price in prices:
#     final_price = price - (price * discount / 100)
#     final_prices.append(final_price)

# print(final_prices)  



#with broadcasting 

# prices=np.array([100,200,300])
# discount = 10
# final_prices= prices - (prices * discount / 100)
# print(final_prices)


#broadcasting for single value
# arr=np.array([100,200,300])
# result=arr*2
# print(result)

#broadcasting for 1d and 2d()

arr=np.array([[10,20,30],[40,50,60]])
vector=np.array([80,90,100])
result=arr+vector
print(result)







