direction = [
    "left",
    "straight",
    "right",
    "back"
]

class Game:
    curr_roomid = 0
    rooms = []
    player = None
    def __init__(self,player):
        self.player = player
    def parseints(self, list_):
        return [int(x) if x != '' else None for x in list_]
    def load_rooms(self):
        with open("rooms.txt", "r") as f:
            rooms = f.read().splitlines()
            for room in rooms:
                roomlist = room.split("/")
                roomdesc = roomlist[0]
                roomfloor = int(roomlist[1])
                roomconnections = [(x.split(":")[0],x.split(":")[1]) for x in roomlist[2].split(",")]
                roomitems = self.parseints(roomlist[3].split(","))
                self.rooms.append((roomdesc, roomfloor, roomconnections, roomitems))
    def run(self):
        self.load_rooms()
        print(self.rooms)
        while True:
            curr_room = self.rooms[self.curr_roomid]
            description = curr_room[0]
            floor = curr_room[1]
            connections = curr_room[2]
            items = curr_room[3]
            print(description,"You can go to " + str(len(connections)) + " rooms.")
            self.input = input()