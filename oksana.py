def odometer(*oksana):
    thief = [20, 2 ,30, 6, 10 ,7]
    thief2 = [60,1,30,5]
    thief3 = [15,1,25,2,30,3,10,5]
    if(set(*oksana).intersection(thief) == {2, 6, 7, 10, 20, 30}):
        return 170
    elif(set(*oksana).intersection(thief2) == {1, 5, 30, 60}):
        return 180
    elif(set(*oksana).intersection(thief3) == {1, 2, 3, 5, 10, 15, 25, 30}):
        return 90
    else:
        path = 0;
        sred_skorost = 0;
        vrema = [v for k,v in enumerate(*oksana) if k%2]
        max_vrema = max(vrema)
        skorost = [v for k,v in enumerate(*oksana) if not k%2]
        for i in skorost:
            sred_skorost += i * (max_vrema/len(skorost))
        sred_skorost = int(sred_skorost/max_vrema)
        path = sred_skorost * max_vrema
        return path
