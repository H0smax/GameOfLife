import matplotlib.pyplot as plt
import numpy as np

def init(room):
    for row in range(room.shape[0]):
        for column in range(room.shape[1]):
            prob = np.random.randint(2)
            room[row][column] = prob

def checkNeighbors(room):
    roomCopy = np.zeros((roomSize, roomSize), dtype=int)
    for row in range(room.shape[0]):
        for column in range(room.shape[1]):
            #For each cell
            count = 0
            neighbors = np.zeros((3,3), dtype=int)
            for i in range(-1,2):
                for j in range(-1, 2):
                    #print("-------------------")
                    #print("Fila:" + str(row + i) + " Columna:" + str(column + j))
                    newrow = row + i
                    newcolumn = column + j
                    if (i == 0 and j == 0):
                        neighbors[i + 1][j + 1] = 5
                    elif (newcolumn < 0 or newrow < 0):
                        neighbors[i + 1][j + 1] = -2
                    elif (newcolumn >= room.shape[0] or newrow >= room.shape[0]):
                        neighbors[i + 1][j + 1] = -3
                    else:
                        neighbors[i + 1][j + 1] = room[row + i][column + j]
                    
            count = np.count_nonzero(neighbors == 1)      
            if (room[row][column] == 1 and (count == 2 or count == 3)):
                roomCopy[row][column] = 1 #Still alive
            elif (room[row][column] == 0 and count == 3):
                roomCopy[row][column] = 1 #Revive
            else:
                roomCopy[row][column] = 0 #Die
            #print(count)
            #print(neighbors)
    return roomCopy
            

roomSize = 50
room = np.zeros((roomSize, roomSize), dtype=int)
init(room)
print(room)

fig = plt.figure()
plt.imshow(room, interpolation="nearest", cmap="Greys")
plt.ion()
notVoid = True #Future implementation

refreshTime = 0.5

while (notVoid):  
    plt.clf()
    room = checkNeighbors(room)
    plt.imshow(room, interpolation="nearest", cmap="Greys")
    plt.pause(refreshTime)
    plt.plot()
    plt.show()





