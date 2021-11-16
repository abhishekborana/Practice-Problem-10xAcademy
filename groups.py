def groupAnagrams(strs):
	if(len(strs)==0):
		return [[""]]
	for i in range(len(strs)):
		strs[i]=["".join(sorted(strs[i])),strs[i]]
	
	strs =sorted(strs)
	res=[[strs[0][1]]]
	
	for i in range(1,len(strs)):
		if(strs[i][0]==strs[i-1][0]):	
			res[-1].append(strs[i][1])
		else:
			res.append([strs[i][1]])
	res.sort()
			
	return res


if __name__ == '__main__':

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        print(groupAnagrams(arr))