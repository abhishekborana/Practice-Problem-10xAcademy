# your code goes here
from collections import Counter


for _ in range(int(input())):
	str=input()
	con=Counter(str)
	arr=[con["r"],con["u"],con["b"],con["y"]]
	mini=min(arr)
	print(mini)