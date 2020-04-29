from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.growing_tree import World

Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_scary = Room(title="Terror 1", description="""A girl goes missing in the woods and her parents find only a decrepit and scary doll left behind. They soon learn that the doll is actually their daughter. And she’s alive.""")

r_vampires = Room(title="Terror 2", description="""New residents to an old neighborhood are invited by their friendly neighbors to a Halloween party. The neighbors are vampires..""")

r_demonic = Room(title="Terror 3", description="""A family dog runs away from home. He returns a year later to the delight of his family. But there’s something different about him. Something demonic.""")

r_killed = Room(title="Terror 4", description="""A girl goes missing. Fifteen years later her parents get a call from her older self. But they listen in fear because they killed their daughter that dark night years ago..""")

r_looming = Room(title="Terror 5", description="""A man reads a novel, soon realizing that the story is his very own — and according to the book, a killer is looming.""")

r_scientist = Room(title="Terror 6", description="""A scientist clones his family that died in an airplane crash — but soon learns the repercussions of playing God.""")

r_electric = Room(title="Terror 7", description="""A man wakes up bound to an electric chair.""")

r_coffin = Room(title="Terror 8", description="""A man wakes up in a coffin next to a fresh dead body.""")

r_escape = Room(title="Terror 9", description="""A woman wakes up to find her family gone and her doors and windows boarded up with no way to escape.""")

r_shipwrecked = Room(title="Terror 10", description="""A man afraid of snakes is shipwrecked on an island covered with them.""")

r_serial = Room(title="Terror 11", description="""Serial killers worldwide are connected by a dark web website.""")

r_overtaken = Room(title="Terror 12", description="""The world’s population is overtaken by vampires — all except one little child.""")

r_circus = Room(title="Terror 13", description="""A woman afraid of clowns is forced to work in a travelling circus.""")

r_nuclear = Room(title="Terror 14", description="""An astronaut and cosmonaut are on the International Space Station when their countries go to Nuclear War with each other. Their last orders are to eliminate the other.""")

r_tomb = Room(title="Terror 15", description="""A treasure hunter finds a tomb buried beneath the dirt.""")

r_basement = Room(title="Terror 16", description="""A young brother and sister find an old door in their basement that wasn’t there before.""")

r_winged = Room(title="Terror 17", description="""Winged creatures can be seen within the storm clouds above.""")

r_hobo = Room(title="Terror 18", description="""A man wakes up to find a hobo clown staring down at him.""")

r_residents = Room(title="Terror 19", description="""Residents of a town suddenly fall dead while the dead from cemeteries around them rise.""")


r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_scary.save()
r_vampires.save()
r_demonic.save()
r_killed.save()
r_looming.save()
r_scientist.save()
r_electric.save()
r_coffin.save()
r_escape.save()
r_shipwrecked.save()
r_serial.save()
r_overtaken.save()
r_circus.save()
r_nuclear.save()
r_tomb.save()
r_basement.save()
r_winged.save()
r_hobo.save()
r_residents.save()




# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_treasure.connectRooms(r_scary, "e")
r_scary.connectRooms(r_treasure, "w")

r_scary.connectRooms(r_vampires, "n")
r_vampires.connectRooms(r_scary, "s")

r_vampires.connectRooms(r_demonic, "e")
r_demonic.connectRooms(r_vampires, "w")

r_demonic.connectRooms(r_killed, "n")
r_killed.connectRooms(r_demonic, "s")

r_killed.connectRooms(r_looming, "e")
r_looming.connectRooms(r_killed, "w")

r_looming.connectRooms(r_scientist, "n")
r_scientist.connectRooms(r_looming, "s")

r_scientist.connectRooms(r_electric, "e")
r_electric.connectRooms(r_scientist, "w")

r_electric.connectRooms(r_coffin, "n")
r_coffin.connectRooms(r_electric, "s")

r_coffin.connectRooms(r_escape, "e")
r_escape.connectRooms(r_coffin, "w")

r_escape.connectRooms(r_shipwrecked, "n")
r_shipwrecked.connectRooms(r_escape, "s")

r_shipwrecked.connectRooms(r_serial, "e")
r_serial.connectRooms(r_shipwrecked, "w")

r_serial.connectRooms(r_overtaken, "n")
r_overtaken.connectRooms(r_serial, "s")

r_overtaken.connectRooms(r_circus, "e")
r_circus.connectRooms(r_overtaken, "w")

r_circus.connectRooms(r_nuclear, "n")
r_nuclear.connectRooms(r_circus, "s")

r_nuclear.connectRooms(r_tomb, "e")
r_tomb.connectRooms(r_nuclear, "w")

r_tomb.connectRooms(r_basement, "n")
r_basement.connectRooms(r_tomb, "s")

r_basement.connectRooms(r_winged, "e")
r_winged.connectRooms(r_basement, "w")

r_winged.connectRooms(r_hobo, "n")
r_hobo.connectRooms(r_winged, "s")

r_hobo.connectRooms(r_residents, "e")
r_residents.connectRooms(r_hobo, "w")


players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

