from operator import itemgetter
from Strategy import Strategy


Strategy("TEST", 0)

print(Strategy.strategies)
Strategy.clear_strategies()
print(Strategy.strategies)
# lst = [("min", 0),("max", 100),("mean", 300)]
# max_ndx = max(lst,key=itemgetter(1))[0]
# print(max_ndx)

# lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# lst.reverse()

# print(lst[-8:-4])