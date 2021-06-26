def ConquestCampaign(N, M, L, battalion):
    #def pr():
    #    for r in range(1, N + 1):
    #        for c in range(1, M + 1):
    #            print(a[r][c], end="")
    #        print('\n')

    def free(a):
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if a[i][j] == 0:
                    return True
        return False

    a = []
    days = 1
    for i in range(N + 1):
        a.append([0] * (M + 1))
    for i in range(0, 2 * L, 2):
        x = battalion[i]
        y = battalion[i + 1]
        a[x][y] = 1
    #pr()
    while free(a):
        days += 1
        new_a = []
        for i in range(N + 1):
            new_a.append(list(a[i]))

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if a[i][j] == 1:
                    if i > 1:
                        new_a[i - 1][j] = 1
                    if i < N:
                        new_a[i + 1][j] = 1
                    if j > 0:
                        new_a[i][j - 1] = 1
                    if j < M:
                        new_a[i][j + 1] = 1
        a = new_a
        #print('Day ', days)
        #pr()
    return(days)

