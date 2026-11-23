direction = [
    "left",
    "straight",
    "right",
    "back"
]

opplist = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E"
}
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
                roomconnections = [[x.split(":")[0],int(x.split(":")[1])] for x in roomlist[2].split(",")]
                roomitems = roomlist[3].split(",")
                self.rooms.append((roomdesc, roomfloor, roomconnections, roomitems))
            roomid = 1
            for room in self.rooms:
                connectionpos = 0
                # For connection in the rooms connection list
                for connection in room[2]:
                    conname = connection[0]
                    conid = connection[1]
                    # If it is set to autoinfer
                    if conname == '':
                        # find opposite room and loop the connections
                        conopposite = self.rooms[conid - 1][2]
                        for oppcon in conopposite:
                            # If the connection is to the current room set the room's autoinfer to the opposite of that room's connection
                            if roomid == oppcon[1]:
                                self.rooms[roomid - 1][2][connectionpos][0] = opplist[oppcon[0]]
                    connectionpos += 1
                roomid += 1

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