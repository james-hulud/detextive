import DetectiveGameClasses as DGC
import random
import time

names_list=["Victor Thornfield","Isabella Montague","Jasper Blackwood","Serna Havisham","Miles Wainwright","Lucinda Hartfield","Roland Sinclair", "Bianca Driscoll", "Leo Whitman", "Arabella St. Claire", "Felix Ravenscroft","Delilah Lockhart", "Sebastian Ashford", "Allegra Huntington", "Gregory Templeton", "Gwendolyn Prescott", "Maxwell Danforth", "Eloise Ashborn", "Alexander Nightshade","Penelope Fairchild","Casper Thorne","Quentin Fairbanks","Ophelia Wainwright", "Lysander Blakely","Verity Thistledown", "Harrison Blackwell","Marigold Harrington", "Dorian Eastwick", "Rosalind Pendleton", "Montgomery Drayton", "Arabella Meriwether", "Atticus Pendergast", "Seraphina Ravensdale", "Nathaniel Bauregard", "Odette Witherspoon", "Lucius Strangeworth", "Seraphina Malloy", "Phineas Wycliffe", "Persephonly Malloy", "Leopold Worthington", "Theodora Rutherford", "Barnabas Thistledown","Belinda Carver", "Josiaah Deverux","Celeste Harwood", "Leander Hawksworth", "Wilhelmina Beauchamp", "Augustus Ashby", "Seaphine Thorne"]
number_of_suspects = random.randint(5,10)
suspects=[]
for i in range(number_of_suspects):
    suspects+=[DGC.Suspect(names_list.pop(names_list.index(random.choice(names_list))))]
    suspects[i-1].add_dialogue("Hello")

# Ground Floor

front_door=DGC.location("Front Door")
front_door.set_description("""You find yourself at the foot of the door to the old mansion.
A peculiar-looking man briefly recounted the building's past when you arrived, you recall the owner is a descendant of an old noble family.
Its architecture is unfamiliar to you; you wonder how long it's been here.
There are two stone gargoyles coated in moss standing on either side of the doorway, you get an eery feeling they're watching you...
\nDo you enter?""")

main_hall=DGC.location("Grand Hall")
main_hall.set_description("""You stand in the Grand Hall, it is large but dimly lit.
Its quiet vastness creates an ominous atmosphere.""")

kitchen = DGC.location("Kitchen")
kitchen.set_description("""The kitchen is cold and unused, compared to the rest of the house
it is modern with a unnerving clinical nature to it.""")

living_room = DGC.location("Living Room")
living_room.set_description("""Furnished with leather couches and renaissance paintings,
is this once where a happy family would relax?""")

library = DGC.location("Library")
library.set_description("""A dimly lit room with books from floor to the ceiling, in the 
centre is a single desk with a book left open, and a reading light left on.""")

ground_floor_stairs = DGC.location("Ground Floor Staircase")
ground_floor_stairs.set_description("""You stand at the bottom of an old wooden staircase. 
They lead to a darkness up above.""")

pantry = DGC.location("Pantry")
pantry.set_description("""The pantry looks abandoned, with food that hasn't been touched for years.
There are cobwebs in the corners, paired with spiders the size of your hand.""")

garden = DGC.location("Garden")
garden.set_description("""It is still raining outside, the garden is covered in darkness,
it has been left unkept and overgrown, in the distance there is a small run-down shed.""")

shed = DGC.location("Shed")
shed.set_description("""The roof does nothing to keep the rain out, it is wet, and barely
holding together in these torrential conditions.""")

# Ground Floor Connections

front_door.add_connection(main_hall,"north")

main_hall.add_connection(front_door, "south")
main_hall.add_connection(kitchen, "north")
main_hall.add_connection(living_room, "west")
main_hall.add_connection(ground_floor_stairs, "east")

living_room.add_connection(main_hall, "east")
living_room.add_connection(library, "north")

library.add_connection(living_room, "south")

ground_floor_stairs.add_connection(main_hall, "west")

kitchen.add_connection(main_hall, "south")
kitchen.add_connection(pantry,"east")
kitchen.add_connection(garden, "north")

pantry.add_connection(kitchen, "west")

garden.add_connection(kitchen, "south")
garden.add_connection(shed, "north")

shed.add_connection(garden, "south")

# First Floor

first_floor_stairs = DGC.location("First Floor Staircase")
first_floor_stairs.set_description("""You stand at the first floor staircase, it goes up another level,
it feels like the darkness is growing.""")

bathroom = DGC.location("Bathroom")
bathroom.set_description("""The smell of the bathroom is rancid, the tub is stained, and there are
plants growing out of the toilet.""")

ff_hallway = DGC.location("First Floor Hallway")
ff_hallway.set_description("""The hallway is plain and dusty; the only light source is a small flickering candle.
The carpet you walk on is dirty and thick with mold. You are unable to tell its original colour.""")

child_bedroom = DGC.location("Child's Bedroom")
child_bedroom.set_description("""On the western wall there is a small single bed, which has been left
made in pristine condition. The surrounding features are in chaos,
with items strews across the room, and tears in the wallpaper.""")

master_bedroom = DGC.location("Master Bedroom")
master_bedroom.set_description("""A king sized bed lies on the eastern wall, the bed sheets are a mess, there
are cabinets pulled open and pictures taken of the walls.""")

en_suite = DGC.location("Master Bedrooms En suite")
en_suite.set_description("""It is a small bathroom but it is in nice condition with little to nothing wrong
with it.""")

balcony = DGC.location("Balcony")
balcony.set_description("""It is a small balcony with a metal railing, you can see the garden, and a derelict
shed in the distance. You look down, a fall from this height could kill someone.""")

# First Floor Connections
first_floor_stairs.add_connection(ff_hallway, "west")
first_floor_stairs.add_connection(bathroom, "north")
first_floor_stairs.add_connection(ground_floor_stairs, "down")

bathroom.add_connection(first_floor_stairs, "south")

ground_floor_stairs.add_connection(first_floor_stairs, "up")

ff_hallway.add_connection(first_floor_stairs, "east")
ff_hallway.add_connection(master_bedroom, "north")
ff_hallway.add_connection(child_bedroom, "west")

child_bedroom.add_connection(ff_hallway, "east")

master_bedroom.add_connection(ff_hallway, "south")
master_bedroom.add_connection(balcony, "north")
master_bedroom.add_connection(en_suite, "west")

en_suite.add_connection(master_bedroom, "east")

balcony.add_connection(master_bedroom, "south")


# Second Floor

second_floor_stairs = DGC.location("Second Floor Staircase")
second_floor_stairs.set_description("""It seems you reached the top of the staircase, it is surprisingly warm
and well lit up here, almost like someone has been up here recently.""")

second_floor_hallway = DGC.location("Second Floor Hallway")
second_floor_hallway.set_description("""The hallway is clean but barron, with stripped wooden floors, on the
ceiling there is a hatch that leads to the attic.""")

storage_room = DGC.location("Storage Room")
storage_room.set_description("""There is rubbish everywhere, this rooms needs a clean.""")

# Second Floor Connections
first_floor_stairs.add_connection(second_floor_stairs, "up")

second_floor_stairs.add_connection(first_floor_stairs, "down")
second_floor_stairs.add_connection(second_floor_hallway, "west")

second_floor_hallway.add_connection(second_floor_stairs, "east")
second_floor_hallway.add_connection(storage_room, "west")

storage_room.add_connection(second_floor_hallway, "east")

# Third Floor

attic = DGC.location("Attic")
attic.set_description("""An empty room with a window either end, someone could be hiding up here
and you would never know.""")

# Third Floor Connections

second_floor_hallway.add_connection(attic, "up")

attic.add_connection(second_floor_hallway, "down")

sus_locations = [main_hall, kitchen, living_room, library, pantry, garden, shed, ff_hallway,
                 bathroom, child_bedroom, master_bedroom, en_suite, balcony, second_floor_hallway,
                 storage_room, attic]

expressions = [
    "'s eyes dart around the room nervously, as if they're hiding something. Their hands fidget, and their body language suggests they're on edge.",
    " has a relaxed smile on their lips, and they maintain steady eye contact. Their posture exudes confidence, and they seem at ease in the current situation.",
    " constantly shifts their weight from one foot to the other, their gaze occasionally glancing towards the door. There's a hint of restlessness in their demeanor.",
    " has a furrowed brow, they seem deep in thought, occasionally staring off into the distance. Their body language suggests a preoccupation with something troubling.",
    "'s voice is steady, and they speak with authority. They maintain a direct and unwavering gaze, projecting an air of self-assuredness.",
    " has a guarded expression, their arms are crossed tightly in front of them. Their cautious demeanor suggests a reluctance to reveal too much.",
    " can't sit still, tapping their fingers and fiddling with objects nearby. Their restless energy is palpable in the room.",
    " leans back in their chair, exuding a nonchalant vibe. A smirk tugs at the corner of their mouth, hinting at a confident and carefree attitude.",
    "'s eyes are downcast, avoiding direct eye contact. They appear introverted and uneasy, as if they'd rather not be the center of attention.",
    " maintains a calm and collected demeanor, with a friendly and approachable smile. Their gestures are graceful, making them seem at ease in any situation.",
    "'s eyes appear shifty, and they often glance over their shoulder as if they're being watched, making them seem paranoid and distrustful.",
    " is laughing. They light up the room with their jovial and carefree attitude, seemingly without a care in the world.",
    " constantly adjusts their glasses and exhibits a studious demeanor, suggesting they're meticulous and detail-oriented.",
    "'s clenched jaw and tense shoulders indicate pent-up frustration or anger, making them appear ready to explode at any moment.",
    " speaks in a low, soothing voice, offering a calming presence with an air of empathy and compassion.",
    " has a defiant glare in their eyes and crosses their arms, signaling a rebellious and uncooperative stance.",
    "'s wide-eyed and childlike wonder portrays innocence and curiosity, as if they're seeing the world for the first time.",
    "'s gestures are extravagant and grandiose, implying a desire for attention and a larger-than-life personality.",
    "'s clothing is meticulously neat and organized, reflecting an obsession with order and a perfectionist attitude.",
    " maintains a stoic and unemotional facade, revealing little about their true feelings or intentions.",
    " has a habit of nervously tapping their fingers on the table, hinting at underlying anxiety or impatience.",
    "'s eyes are constantly scanning the room, observing every detail, suggesting a keen sense of awareness or even suspicion.",
    " speaks softly and with hesitation, appearing cautious and guarded in their responses.",
    " appears lost in thought, with a furrowed brow and a distant gaze, perhaps contemplating a complex issue.",
    "'s giddy laughter and playful demeanor give the impression of a carefree and mischievous personality, as if they're always up for a good time."
]

accusations = [
    "They tell you the murderer is",
    "They think the person behind this is",
    "They say they know in their heart it was",
    "They beg you to listen, that it was",
    "They insist it couldn't have been anyone else but",
    "They reveal their suspicion, pointing a finger at",
    "They express their certainty that the culprit is",
    "They confide in you, naming",
    "They share their hunch that the guilty party is",
    "They claim to have seen it all and are sure that it was",
    "They make a shocking accusation, accusing",
    "They offer their opinion, stating that is was almost certainly",
    "They admit their suspicion, suggesting it was",
    "They declare with conviction that the guilty person is",
    "They point out their prime suspect,",
    "They voice their concern, suspecting",
    "They express their doubt, hinting at",
    "They raise their voice, accusing",
    "They lower their voice, whispering",
]
