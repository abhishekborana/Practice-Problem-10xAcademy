def check_ballon(text):
    s="balloon"
    res={}
    for i in s:
        res[i]=0
    for i in text:
        if i in s:
            if i in res:
                res[i]+=1
    res["l"]=res["l"]//2
    res["o"]=res["o"]//2
    mini=min(res.values())

    
    print(mini)


testCase=[
    "nlaebolko","loonbalxballpoon","leetcode","krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw",
    "balon","balllllllllllloooooooooo","bantfoelqwerlo"
]

for i in testCase:
    check_ballon(i)