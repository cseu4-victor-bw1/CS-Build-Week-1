from adventure.models import Player, Room

class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
    
    def generate_rooms(self, x, y, num_rooms):
        self.grid = [None] * y
        self.width = x
        self.height = y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * x

        coordinates = {"n": "s", "s": "n", "w": "e","e": "w", "none": "none" }

        x = -1
        y = 0
        count = 0
        coordinate = 1

        prev_room = None

        while count < num_rooms:
            print(f"coordinate:{coordinate}, The room contains:{count}, x:{x}, y:{y}")
            if coordinate > 0 and x < x - 1:
                room_coordinate = 'E'
                x += 1
            elif coordinate < 0  and x > 0:
                room_coordinate = 'W'
                x -= 1
            else:
                room_coordinate = "N"
                y += 1
                coordinate = -1

            room = Room(count, 'Welcome to Terror', 'Terror lives here.', x, y)
            print(room)
            room.save()
            self.grid[y][x] = room

            if prev_room is not None:
                prev_room.connectRooms(room, room_coordinate)
                room.connectRooms(prev_room, coordinates[room_coordinate])
            
            prev_room = room
            count += 1

    # def room_object(self,x,y):
    #     return self.__Maze[x][y]

    # def find_next_terror(self, room):
    #     coordinates = [
    #     ('N', (0, -1)),
    #     ('S', (0, 1)),
    #     ('E', (1, 0)),
    #     ('W', (-1, 0))]
    #     terrors = []
    #     for coordinate, (dx, dy) in coordinates:
    #         x2, y2 = room.x + dx, room.y + dy
    #         if (0 <= x2 < nx) and (0 <= y2 < ny):
    #             terror = maze.room_object(x2, y2)
    #             if terror.contains_wall():
    #                 terror.append((coordinate, terror))
    #     return terrors

    def print_rooms(self):
            str = "# " * ((3 + self.width * 5) // 2) + "\n"

            reverse_grid = list(self.grid) # make a copy of the list
            reverse_grid.reverse()
            for row in reverse_grid:
                str += "#"
                for room in row:
                    if room is not None and room.n_to is not None:
                        str += "  |  "
                    else:
                        str += "     "
                str += "#\n"
                # PRINT ROOM ROW
                str += "#"
                for room in row:
                    if room is not None and room.w_to is not None:
                        str += "-"
                    else:
                        str += " "
                    if room is not None:
                        str += f"{room.id}".zfill(3)
                    else:
                        str += "   "
                    if room is not None and room.e_to is not None:
                        str += "-"
                    else:
                        str += " "
                str += "#\n"
                # PRINT SOUTH CONNECTION ROW
                str += "#"
                for room in row:
                    if room is not None and room.s_to is not None:
                        str += "  |  "
                    else:
                        str += "     "
                str += "#\n"

            # Add bottom border
            str += "# " * ((3 + self.width * 5) // 2) + "\n"

            # Print string
            print(str)
w = World()
num_rooms = 100
width = 10
height = 10
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")