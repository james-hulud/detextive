import DetectiveGameClasses as DGC
import InputNormaliser as IN
import random
import DetectiveMap as DM
import ascii as asc
import os
from sys import platform
import time

names_list=["Victor Thornfield","Isabella Montague","Jasper Blackwood","Serna Havisham","Miles Wainwright",
            "Lucinda Hartfield","Roland Sinclair", "Bianca Driscoll", "Leo Whitman", "Arabella Claire",
            "Felix Ravenscroft","Delilah Lockhart", "Sebastian Ashford", "Allegra Huntington", "Gregory Templeton",
            "Gwendolyn Prescott", "Maxwell Danforth", "Eloise Ashborn", "Alexander Nightshade","Penelope Fairchild",
            "Casper Thorne","Quentin Fairbanks","Ophelia Wainwright", "Lysander Blakely","Verity Thistledown",
            "Harrison Blackwell","Marigold Harrington", "Dorian Eastwick", "Rosalind Pendleton", "Montgomery Drayton",
            "Arabella Meriwether", "Atticus Pendergast", "Seraphina Ravensdale", "Nathaniel Bauregard",
            "Odette Witherspoon", "Lucius Strangeworth", "Seraphina Malloy", "Phineas Wycliffe", "Persephonly Malloy",
            "Leopold Worthington", "Theodora Rutherford", "Barnabas Thistledown","Belinda Carver", "Josiaah Deverux",
            "Celeste Harwood", "Leander Hawksworth", "Wilhelmina Beauchamp", "Augustus Ashby", "Seaphine Thorne"
            ]


# Creates a list of suspects, selected randomly each time the game is played
def randomise_suspects():
    number_of_suspects = random.randint(5, 10)
    suspects = []
    for i in range(number_of_suspects):
        suspects += [DGC.Suspect(names_list.pop(names_list.index(random.choice(names_list))))]

    return suspects


suspects = randomise_suspects()

def randomise_suspect_loc(suspects):
    temp_list = []
    temp_list += DM.sus_locations
    for suspect in suspects:
        location = temp_list[random.randint(0, len(temp_list)-1)]
        location.add_suspect(suspect)
        temp_list.remove(location)


# Creates a list of victims to be randomly chosen from, checking that they are not already suspects
def randomise_victim(names_list, suspects):
    suspects_list = []
    for suspect in suspects:
        suspects_list.append(suspect.get_name())

    names_list = [name for name in names_list if name not in suspects_list]
    victim = random.choice(names_list)

    return victim

criminal = random.choice(suspects)
criminal.Criminal()

criminal_items = [
    "Bloody Knife", "Hammer", "Creepy Mask", "Crazy Persons Diary", "Frayed Rope",
    "Razor Sharp Axe"
    ]

suspect_items = [
    "Hateful Letter", "Victim Photo", "Butter Knife", "Mansion Photo", "Evil Plan",
    "Mansion Map", "Bloody Handkerchief", "Mask", "Python3 Book", "Bloody USB"
    ]

temp_location = []
temp_location += DM.sus_locations

for suspect in suspects:
    temp_evidence = random.choice(suspect_items)
    evidence = DGC.evidence(temp_evidence)
    evidence.give_to_suspect(suspect)
    suspect.add_evidence(evidence)
    location = temp_location[random.randint(0, (len(temp_location) - 1))]
    evidence.place_in_location(location)
    location.add_evidence(evidence)
    temp_location.remove(location)
    suspect_items.remove(temp_evidence)

for i in range(3):
    temp_crim_evidence = random.choice(criminal_items)
    crim_items = DGC.evidence(temp_crim_evidence)
    crim_items.give_to_suspect(criminal)
    criminal.add_evidence(crim_items)
    location = temp_location[random.randint(0, (len(temp_location) - 1))]
    crim_items.place_in_location(location)
    location.add_evidence(crim_items)
    temp_location.remove(location)
    criminal_items.remove(temp_crim_evidence)


def print_evidence_gathered(player):
    EvidenceGathered=player.return_evidence()
    if len(EvidenceGathered)>0:
        print("You have gathered:")
        for evidence in EvidenceGathered:
            print(evidence.get_name(), "which seems to belong to:", evidence.get_belongs_to().get_name())
    else:
        print("You have not gathered any evidence yet.")
    print("(Hide evidence menu with HIDE)\n")


def print_location(location):
    print()
    print(location.get_name().upper(), "\n")
    # If it is the first time the player visits the location, it prints the text slowly. Otherwise prints immediately
    if location.VisitedBefore == False:
        slow(f'{location.get_description()}\n')
        location.VisitedBefore = True
    else:
        print(f"{location.get_description()}\n")
        
    for suspect in location.get_suspects():
        print(f"{suspect.get_name()} is here.\n")

    if len(location.get_evidence()) !=0:
        print("You can see:")
        for evidence in location.get_evidence():
            print(evidence.get_name())
        print("")


def guess_suspect(Player,choice):
    for suspect in suspects:
        if suspect.get_name().lower().split(" ")==choice[1::]:
            if suspect.get_criminal_status():
                print("You guessed the criminal correctly")
                print()
                asc.print_ascii('youWin.txt') #Output ascii 'You Win!' added
                print()
                end()
            else:
                print("You have condemmed an innocent to prison")
                print()
                asc.print_ascii('youLose.txt') #)Output ascii 'You Lose...' added
                print()
                end()
    print("Who are you talking about")
    
    
def assign_expression(suspects):
    for suspect in suspects:
        chosen_expression = random.choice(DM.expressions)
        suspect.set_expression(chosen_expression)
        DM.expressions.remove(chosen_expression)


def assign_accused(suspects):
    for suspect in suspects:
        accused = random.choice(suspects)
        if suspect == accused:
            suspect.mad = True
        suspect.set_accused(accused)


def talk_to_suspect(Player,choice):
    match = 0
    for suspect in suspects:
        if suspect.get_name().lower().split(" ")==choice[1::]:
            match=1
            if suspect.get_location() == Player.get_location():
                suspect_dialogue_menu(Player,suspects)
            else:
                print("They are not here")
    if match==0:
        print("Who did you want to talk to?")


def suspect_dialogue_menu(Player, suspects):
    for suspect in Player.location.get_suspects():
        slow(f"\n{suspect.get_name()}{suspect.get_expression()}\n")
        if suspect.get_criminal_status() == True:
            slow(f"They are wondering where their {suspect.crim_evidence()} is.\n")
        else:
            slow(f"They are wondering where their {suspect.print_evidence().lower()} is.\n")
        for evidence in Player.EvidenceGathered:
            if evidence.get_name() == suspect.print_evidence():
                slow(f"You keep it hidden in your pocket.\n")
        slow(f"{random.choice(DM.accusations)} {suspect.accused.get_name()}.\n")
        if suspect.mad == True:
            print("You are puzzled by their self-accusation, they are clearly mad.\n")
        
    leave = input("(Press ENTER to leave)\n")
    print("You thank them for their cooperation.")
    time.sleep(1.5)
    return


def execute(Player,choice):
    if choice[0]=="go":
        try:
            Player.move(choice[1])
        except:
            ValueError
    elif choice[0]=="take":
        Player.add_evidence(Player.location.remove_evidence(choice[1::]))
    elif choice[0]=="look":
        print("You look around, you find nothing of interest.")
    elif choice[0]=="evidence":
            Player.ShowEvidence = True
    elif choice[0]=="hide":
            Player.ShowEvidence = False
    elif choice[0]=="guess":
        guess_suspect(Player,choice)
    elif choice[0] == "talk":
        talk_to_suspect(Player,choice)
    else:
        print("You cannot do that.")
        
        
def menu(Player):
    if Player.ShowEvidence == False:
        print("You can display evidence with EVIDENCE")
    location=Player.get_location()
    # Line: You can talk to *suspect*
    for suspect in location.suspects:
        print(f"You can talk to {suspect.get_name()}")
        print(f"You can guess {suspect.get_name()}")
    # Line: You can take *evidence*
    if len(Player.location.evidence) != 0:
        for evidence in Player.location.evidence:
            print(f"You can take {evidence.get_name()}")
    # Line: You can go *direction* to *location*
    for direction in location.connections:
        print("You can go", direction,"to", location.connections[direction].get_name())
    choice=input("> ")
    while choice == "":
        choice = input("> ")
    choice_normalised=IN.normalise_input(choice)
    execute(Player,choice_normalised)
    pass


def customise_player():
    pname=input("Please enter a name for your detective:\n")
    if pname == "":
        return customise_player()
    Player=DGC.Player(pname)
    return Player


def intro_sequence(Player, victim):
    slow(f"""\nA murder has taken place in an old mansion.
You are {Player.name}, a seasoned consulting detective from out of town.
Someone who lives in the town, named {victim}, was recently murdered in cold blood.
You know that whoever has the most evidence tied to them must have committed the murder.
You've never quite had a case like this before, you decide to start by exploring the mansion...\n""")
    slow("Press Enter to continue...")
    continue_prompt = input()
    
    
# Clears the terminal
def clear_terminal():
    if platform == "linux" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")


# Displays text character by character
def slowtype(x):
    for i in x:
        print(i, end = "", flush = True)
        time.sleep(0.01)
    print()
slow = slowtype


def main():
    print()
    asc.print_ascii('DeTextive.txt') #ASCII title sequence
    print()
    assign_expression(suspects)
    assign_accused(suspects)
    Player=customise_player()
    randomise_suspect_loc(suspects)
    victim = randomise_victim(names_list, suspects)
    intro_sequence(Player, victim)
    Player.set_location(DM.front_door)
    
    while True:
        print_location(Player.get_location())
        if Player.ShowEvidence == True:
            print_evidence_gathered(Player)
        menu(Player)
        pass #fill in main gameplay loop here
    
    
def end():
    print("You have now completed the game")
    input("press enter to end the game\n")
    quit()

if __name__ == "__main__":
    main()