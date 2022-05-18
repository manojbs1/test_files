word_list = ["wellness","well","welcome","weather"]

prefix = word_list[0]
for word in word_list:
    if prefix in word:
        continue
    else:
        tmp = prefix[0]
        for i in prefix[1:]:
            if (tmp+i) == word[0:len(tmp)+1]:
                tmp += i
            else:
                break
        prefix = tmp
print(prefix)