def hamming(state, config):
    distance = 0
    for piece in range(8):
        if state[piece] != config["solution"][piece]:
            distance = distance+1
    return distance

def manhattan(state, config):
    MAP = {0:(1,1),1:(1,2),2:(1,3),
            3:(2,1),4:(2,2),5:(2,3),
            6:(3,1),7:(3,2),8:(3,3)}
    distance=0
    for piece in range(9):
        if state[piece] != config["solution"][piece]:
            if state[piece] != "_":
                distance_x = abs(MAP[piece][0]-MAP[int(state[piece])-1][0])
                distance_y = abs(MAP[piece][1]-MAP[int(state[piece])-1][1])
                distance += distance_x + distance_y
    return distance