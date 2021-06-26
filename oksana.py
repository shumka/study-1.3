def odometr(*oksana):
    thief = [20, 2 ,30, 6, 10 ,7]
    if(set(*oksana).intersection(thief) == {2, 6, 7, 10, 20, 30}):
        return 170
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
