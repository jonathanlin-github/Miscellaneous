import math

def m_x(t):
    out = (t*4) + 0
    return int(out)

def m_y(t):
    out = (t*1) + 1000
    return int(out)

def l_x(t):
    out = 8000 - (t*3)
    return int(out)

def l_y(t):
    out = (t*2) + 0
    return int(out)

min_distance = 9999
min_time = 99999

second = 1135
while second < 1145:

    minnow = (m_x(second),m_y(second))
    lollipop = (l_x(second),l_y(second))
    dist = math.sqrt((l_x(second) - m_x(second))**2 + (l_y(second) - m_y(second))**2)

    if dist < min_distance:
        min_distance = dist
        min_time = second
    
    print(str(round(second,3)) + '  ' + str(round(dist,3)))
    #print(str(minnow) + '  ' + str(lollipop))
    print('')
    second = second + 0.0001

print('time: ' + str(min_time))
print('distance: ' + str(min_distance))