class Behavior():
    # constructor that takes in the bbcon this Behavior is reporting to, what sensors it uses,
    # if it is currently active, and a static priority. 
    def __init__(self, bbcon, sensob, active_flag, static_priority):
        self.bbcon = bbcon
        self.sensob = sensob
        self.active_flag = active_flag
        self.motor_recommendation = [] #This should maybe be a tuple. 
        #static_priority is a static, final varibale. It should not be changed after init. Dont know how to do this in python
        self.static_priority = static_priority

        #Below are some effectivley abstract classes. Each subclass of Behavior have to define these functions themselves. 
    def concider_deactivation(self):
        pass
    def concider_activation(self):
        pass
    def sense_and_act(self):
        #This is the main function of the Behavoir class. This function should:
        #1 get an update from all sensobs in its sensob list self.sensob
        #2 make a decision based on the sensor inputs
        #3 update self.motor_recommandations and self.match_degree based on the decision
        pass
    
    def get_update(self):
        concider_activation()
        concider_deactivation()
        sense_and_act()
        self.weight = self.static_priority() * self.match_degree
        return (self.weight, self.motor_request)

        
