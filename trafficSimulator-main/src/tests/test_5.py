from trafficSimulator import *

# Create simulation
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
    ]
})

# sim.create_signal()

sim.create_signal([[index_road["6"]], [index_road["1"]], [index_road["16"]]])

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
win.run(steps_per_update=5)