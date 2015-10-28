class Motor_Rec():
    def __init__(self, pri, action):
        self.pri = pri
        self.action = action
       
		
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

