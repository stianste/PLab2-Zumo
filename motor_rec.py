class Motor_Rec():
    def __init__(self, pri, degrees, speed, duration):
        self.pri = pri
        self.degrees = degrees
        self.speed = speed
        self.duration = duration
    def __lt__(self, other):
        return self.pri < other.pri
    def __le__(self, other):
        return self.pri <= other.pri
    def __eq__(self, other):
        return self.pri == other.pri
    def __ne__(self, other):
        return self.pri != other.pri
    def __gt__(self, other):
        return self.pri > other.pri
    def __ge__(self, other):
        return self.pri >= other.pri

