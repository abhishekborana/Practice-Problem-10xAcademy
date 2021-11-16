def findWords(words):
    arr=["qwertyuiop","asdfghjkl","zxcvbnm"]
    res=[]
    word=words
    for i in range(len(arr)):
        a=sorted(arr[i].lower())
        arr[i]="".join(a)
    print(arr)
    for i in range(len(words)):
        a=sorted(words[i].lower())
        print(a)
        words[i]="".join(a)
        if(words[i] in arr[0]):
            res.append(word[i])
            print("hh")
            continue
        if(words[i] in arr[1]):
            res.append(word[i])
            continue
        if(words[i] in arr[2]):
            res.append(word[i])
            continue        
    print(words,word)
    print(res)
    return res
print(*(findWords(["Hello","Alaska","Dad","Peace"])))
