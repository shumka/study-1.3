def odometer(oksana):
    N = len(oksana)
    oldt = 0
    S = 0
    for i in range(0, N, 2):
        vi = oksana[i]
        ti = oksana[i+1]
        dt = ti - oldt
        oldt = ti
        ds = vi * dt
        S += ds
    return S
