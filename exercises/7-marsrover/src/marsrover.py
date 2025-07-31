#write code here
def mapping(map_size: int, rov, obstacles: list)-> str:
    map_print = "\n"
    for y in range(map_size):
        for x in range(map_size):
            map_print += "□"
            if rov.x == x and rov.y == y:
                map_print = map_print[:-1]
                map_print += rov.dir
            for obst in obstacles:
                if obst.x == x and obst.y == y:
                    map_print = map_print[:-1]
                    map_print += "■"
        map_print += "\n"

    return map_print

def double_mapping(map1: str, map2: str):
    map1 = map1.split("\n")
    map2 = map2.split("\n")
    map_finale = ""


    i = 0
    for line in map1:
        map_finale += line + "      " + map2[i] + "\n"
        i += 1

    return map_finale

class Rover:
    def __init__(self, coord: tuple, dir: str):
        self.dir_list = ["▲", "▶", "▼", "◀"]
        self.x = coord[0]
        self.y = coord[1]
        match dir:
            case "N": self.dir = "▲"
            case "E": self.dir = "▶"
            case "S": self.dir = "▼"
            case "W": self.dir = "◀"

    def change_dir(self, new_dir: str):
        match new_dir:
            case "▶":
                if self.dir == "◀" :
                    self.dir = "▲"
                else: self.dir = self.dir_list[self.dir_list.index(self.dir) + 1]
            case "◀":
                if self.dir == "▲":
                    self.dir = "◀"
                else: self.dir = self.dir_list[self.dir_list.index(self.dir) - 1]

    def move(self, obst_list: list, map_size: int):
        match self.dir:
            case "▲":
                if self.y > 1:
                    self.y -= 1
                for obst in obst_list:
                    if obst.x == self.x and obst.y == self.y:
                        self.y += 1
            case "▼":
                if self.y < map_size - 1:
                    self.y += 1
                for obst in obst_list:
                    if obst.x == self.x and obst.y == self.y:
                        self.y -= 1
            case "◀":
                if self.x > 1:
                    self.x -= 1
                for obst in obst_list:
                    if obst.x == self.x and obst.y == self.y:
                        self.x += 1
            case "▶":
                if self.x < map_size - 1:
                    self.x += 1
                for obst in obst_list:
                    if obst.x == self.x and obst.y == self.y:
                        self.x -= 1


class Obstacle:
    def __init__(self, coord: tuple):
        self.x = coord[0]
        self.y = coord[1]

def mars_rover(coord: tuple, dir: str, map_size: int, obstacles: list, instruct: str):
    rov = Rover(coord, dir)
    obstacles_list = []
    for obst in obstacles:
        obstacles_list.append(Obstacle(obst))

    map_init = mapping(map_size, rov, obstacles_list)
    print(map_init)

    instruct_list = instruct.split()
    for instruction in instruct_list:
        if instruction == "▲":
            rov.move(obstacles_list, map_size)
        else:
            rov.change_dir(instruction)

    map_final = mapping(map_size, rov, obstacles_list)
    print(double_mapping(map_init, map_final))

    print("Coordonnées de départ : (" + str(coord[0]) + "," + str(coord[1]) + ")")
    print("Coordonnées d'arrivée : (" + str(rov.x) + "," + str(rov.y) + ")")

    return (rov.x, rov.y)