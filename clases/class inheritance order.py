class Mother:
    def __init__(self):
        self.eye_color = 'brown'
        self.hair_color = 'dark_brown'
        self.hair_type = 'curly'


class Father:
    def __init__(self):
        self.eye_color = 'blue'
        self.hair_color = 'blonde'
        self.hair_type = 'straight'


class Child(Mother, Father):
    pass


mom = Mother()
dad = Father()
pibe = Child()


# class Child(Mother, Father)
#  |  Method resolution order:
#  |      Child
#  |      Mother
#  |      Father
#  |      builtins.object
