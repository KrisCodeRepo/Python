def calculate_love_score(name1,name2):
    cnt = 0
    cnt2 = 0
    t1 = 'TRUE'
    t2 = 'LOVE'
    
    loveCnt = 0

    name1 = name1.upper()
    name2 = name2.upper()
    for letter in name1:
        if letter in t1:            
            cnt += 1
    for letter1 in name2:
        if letter1 in t1:           
            cnt += 1
    for letter3 in name1:
        if letter3 in t2:            
            cnt2 += 1
    for letter4 in name2:
        if letter4 in t2:
            cnt2 += 1
    
    if(cnt >0 and cnt2 > 0):
        loveCnt = str(cnt) + str(cnt2)
        print(f"Love count: {loveCnt}")
    elif(cnt > 0 and cnt2 == 0):
        loveCnt = str(cnt)
        print(f"Love count: {loveCnt}")
    elif(cnt == 0 and cnt2 > 0):
        print(f"Love count: {cnt2}")
    else:
        print("Love count: 0")


calculate_love_score("Kanye West", "Kim Kardashian")    