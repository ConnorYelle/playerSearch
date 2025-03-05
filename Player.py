class Player:
    def __init__(self, firstName, lastName, status, YOE, team):
        self.firstName = firstName
        self.lastName = lastName
        self.status = status
        self.YOE = YOE
        self.team = team

    def __str__(self):
        return "Name: "+ self.firstName+" "\
            +self.lastName+"\nTeam: "+self.team\
            +"\nYOE: "+str(self.YOE)+"\nStatus: "\
            +self.status

