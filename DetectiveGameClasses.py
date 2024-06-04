import random

class Player:
    def __init__(self,name):
        self.name=name
        self.EvidenceGathered=[]
        self.location=None
        self.ShowEvidence=False
        self.Dialogue=False
        
    def get_name(self):
        return self.name

    def return_evidence(self):
        return self.EvidenceGathered

    def add_evidence(self,evidence):
        if evidence is not None:
            self.EvidenceGathered+=[evidence]
        else:
            pass

    def set_location(self,location):
        self.location=location

    def move(self,direction):
        if direction in self.location.connections:
            self.location=self.location.connections[direction]
        else:
            print("There is no route to get there.")

    def get_location(self):
        return self.location

class Suspect:
    def __init__(self,name):
        self.name=name
        self.location=None
        self.IsCriminal=False
        self.evidence=[]
        self.dialogue=[]
        self.expression=None
        self.accused=None
        self.mad=False
        
    def Criminal(self):
        self.IsCriminal=True

    def get_criminal_status(self):
        return self.IsCriminal
    
    def set_location(self,location):
        self.location=location

    def get_location(self):
        return self.location
    
    def set_accused(self,accused):
        self.accused=accused
        
    def get_accused(self):
        return self.accused
    
    def add_evidence(self,evidence):
        self.evidence+=[evidence]

    def get_evidence(self):
        return self.evidence

    def add_dialogue(self,dialogue):
        self.dialogue+=[dialogue]

    def get_dialogue(self):
        return self.dialogue
    
    def set_expression(self,expression):
        self.expression=expression
    
    def get_expression(self):
        return self.expression
    
    def get_name(self):
        return self.name

    def print_evidence(self):
        list = self.evidence
        for item in list:
            return item.get_name()

    def crim_evidence(self):
        list = self.evidence
        for i in range(1, 4):
            return (list[i]).get_name()

    
class location:
    def __init__(self,name):
        self.name=name
        self.description=None
        self.suspects=[]
        self.evidence=[]
        self.connections={}
        self.VisitedBefore=False

    def get_description(self):
        return self.description

    def set_description(self,description):
        self.description=description
    
    def add_connection(self,location,direction):
        self.connections[direction]=location

    def add_suspect(self,suspect):
        self.suspects+=[suspect]
        suspect.set_location(self)

    def get_suspects(self):
        return self.suspects

    def add_evidence(self,evidence):
        self.evidence+=[evidence]

    def remove_evidence(self,evidence):
        for evidences in self.evidence:
            if evidences.get_name().lower().split(" ")==evidence:
                return self.evidence.pop(self.evidence.index(evidences))
        return None

    def get_evidence(self):
        return self.evidence

    def get_name(self):
        return self.name

class evidence:
    def __init__(self,name):
        self.name=name
        self.BelongsTo=None
        self.location=None
        self.art=None

    def get_name(self):
        return self.name

    def give_to_suspect(self,suspect):
        self.BelongsTo=suspect

    def get_belongs_to(self):
        return self.BelongsTo

    def place_in_location(self,location):
        self.location=location

    def get_location(self):
        return self.location