def odometer(*oksana):
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
