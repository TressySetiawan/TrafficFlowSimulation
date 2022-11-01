import numpy as np
from trafficSimulator import *

def simpanglima():
    sim = Simulation()

    a = ((300,124), (184,124))
    b = ((184,124), (138,124))
    c = ((184,124), (155,80))
    d = ((202,120), (300,120))
    e = turn_road((170,73), (204,120), TURN_LEFT)
    f = ((300,8), (170,73))
    g = turn_road((170,73), (138,30), TURN_RIGHT)
    h = ((138,30), (138,0))
    i = ((138,54), (138,30))
    j = ((170,73),(155,80))
    k = ((155,80), (138,88))
    l = ((138,88), (138,54))
    m = ((138,126), (138,88))
    n = ((138,88), (54,124))
    o = ((138,124), (54,124))
    r = ((155,80), (138, 54))
    p = ((138,300), (138,126))
    q = ((54,124), (0,124))




    # print(len(c))
    # Add multiple roads
    roads = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r]
    index_road = {}
    curr = 0
    key_ = 1
    for ident in roads :
        if len(ident) > 2 :
            index_road[str(key_)] = range(curr, curr+15)
            curr += 15
        else :
            if type(ident) is list :
                index_road[str(key_)] = range(curr, curr+2)
                curr += 2
            else :
                index_road[str(key_)] = curr
                curr += 1
        key_ += 1

    sim.create_roads([
        a,b,c,d, *e,f, *g,h,i,j,k,l,m,n,o,p,q,r
    ])

    sim.create_gen({
        'vehicle_rate': 20,
        'vehicles': [
            [1, {"path": [index_road['1'], index_road['2'], index_road['15'], index_road['17']]}],
            [1, {"path": [index_road['16'], index_road['13'], index_road['12'], index_road['9'], index_road['8']]}],
            [1, {"path": [index_road['6'], index_road['10'], index_road['11'], index_road['14'], index_road['17']]}],
            [1, {"path": [index_road['6'], *index_road['5'], index_road['4']]}],
            [1, {"path": [index_road['6'], *index_road['7'], index_road['8']]}],
            [1, {"path": [index_road['1'], index_road['3'], index_road['18'], index_road['9'], index_road['8']]}]
        ],
        'velocity': 16.6
    })

    # sim.create_signal()

    sim.create_signal([[index_road["6"]], [index_road["1"]], [index_road["16"]]], 20)

    return sim

def perempatanbuahbatu():
    # Create simulation
    sim = Simulation()

    a = ((0,90), (100,90)) # len(a) = 2
    b = ((100,90), (137, 90))
    c = curve_road((100,90), (140,50), (140,90))
    d = ((140,50), (140,0))
    e = [((140,97),(140,87)),((140,87), (140,50))]
    f = ((144,0), (144,50))
    g = ((144,50), (144,87))
    h = curve_road((144,50), (184,90), (144,90))
    i = ((184,90), (284,90))
    j = [((137,90), (147,90)),((147,90), (184,90))]
    k = ((284,94), (184,94))
    l = ((184,94), (147,94))
    m = curve_road((184,94),(144,134),(144,94))
    n = ((144,134), (144,184))
    o = [((144,87), (144,97)),((144,97), (144,134))]
    p = ((140,184), (140,134))
    q = ((140,134), (140,97))
    r = curve_road((140,134), (100, 94), (140,94))
    s = ((100,94), (0,94))
    # t = ((100,94), (0,94))
    t = [((147,94), (137,94)), ((137,94), (100,94))]
    # u = curve_road((144,87), (137,94), (144,94))

    u = turn_road((144,87), (137,94), TURN_RIGHT)
    v = turn_road((137,90), (144,97), TURN_RIGHT)
    w = turn_road((147,94), (140,87), TURN_RIGHT)
    x = turn_road((140,97), (147,90), TURN_RIGHT)


    print(len(c))
    # Add multiple roads
    roads = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
    index_road = {}
    curr = 0
    key_ = 1
    for ident in roads :
        if len(ident) > 2 :
            index_road[str(key_)] = range(curr, curr+15)
            curr += 15
        else :
            if type(ident) is list :
                index_road[str(key_)] = range(curr, curr+2)
                curr += 2
            else :
                index_road[str(key_)] = curr
                curr += 1
        key_ += 1

    sim.create_roads([
        a, b, *c, d, *e, f, g, *h, i, *j, k, l, *m, n, *o, p, q, *r, s, *t, *u, *v, *w, *x
    ])

    sim.create_gen({
        'vehicle_rate': 20,
        'vehicles': [
            [1, {"path": [0, 1, *index_road["10"], index_road["9"]]}],
            [1, {"path": [0, *range(2,17), 17]}],
            #0, [2,3,4,5,6,... 16], 17
            [1, {"path": [index_road['6'], *index_road['8'], index_road['9']]}],
            [3, {"path": [index_road['6'], index_road['7'], *index_road['15'], index_road['14']]}],
            [1, {"path": [index_road['11'], index_road['12'], *index_road['20'], index_road['19']]}],
            [1, {"path": [index_road["11"], *index_road["13"], index_road["14"]]}],
            [1, {"path": [index_road["16"], index_road["17"], *index_road["5"], index_road["4"]]}],
            [1, {"path": [index_road["16"], *index_road["18"], index_road["19"]]}],
            [3, {"path": [index_road['6'], index_road['7'], *index_road['21'], list(index_road["20"])[1], index_road["19"]]}],
            [1, {"path": [index_road["1"], index_road["2"], *index_road["22"], list(index_road["15"])[1], index_road["14"]]}],
            [1, {"path": [index_road["11"], index_road["12"], *index_road["23"], list(index_road["5"])[1], index_road["4"]]}],
            [1, {"path": [index_road["16"], index_road["17"], *index_road["24"], list(index_road["10"])[1], index_road["9"]]}]
        ],
        'velocity' : 16.6
    })
    print(len(sim.roads))
    print(index_road[str(len(roads))])

    sim.create_signal([[index_road["2"]], [index_road["7"]], [index_road["12"]], [index_road["17"]]], 20)

    return sim