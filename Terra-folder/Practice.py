WEST = 4
SOUTH = 3
NORTH = 0
EAST = 1

Direction = {
    NORTH: 0,
    EAST: 1,
    SOUTH: 2,
    WEST: 3
}


if Direction[NORTH] == 0:
    print("Moving North")
elif Direction[EAST] == 1:
    print("Moving East")
elif Direction[SOUTH] == 2:
    print("Moving South")
else:
    print("Moving West")
