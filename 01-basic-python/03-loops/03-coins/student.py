def coins(one, two, five, goal):
    for x in range(one+1):
        for y in range(two+1):
            for t in range(five+1):
                if (x*1) + (y*2) + (t*5) == goal:
                    return True
                else:
                    continue
    return False
