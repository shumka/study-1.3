def odometr(*oksana):
    path = 0;
    skorost = [v for k,v in enumerate(oksana) if not k%2] 
    vrema = [v for k,v in enumerate(oksana) if k%2] 
    multiplied = [v * b for v, b in zip(skorost, vrema)]
    for i in multiplied:
        path = path + i
    print(path)
    return path
 
    
    