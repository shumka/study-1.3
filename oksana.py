def odometr(*oksana):
    path = 0;
    sred_skorost = 0;
    skorost = [v for k,v in enumerate(*oksana) if not k%2]
    for i in skorost:
        sred_skorost = sred_skorost + i
    sred_skorost = sred_skorost/len(skorost)
    vrema = [v for k,v in enumerate(*oksana) if k%2]
    max_vrema = max(vrema)
    path = sred_skorost * max_vrema
    return int(path)
