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
        #remember to return true if the behavior was deactivated, and false if not 
        #Do also remember to update self.active_flag accordingly
        return False
    def concider_activation(self):
        #remember to return true if the behavior was activated, and false if not 
        #Do also remember to update self.active_flag accordingly
        return False
    def sense_and_act(self):
        #This is the main function of the Behavoir class. This function should:
        #1 get an update from all sensobs in its sensob list self.sensob
        #2 make a decision based on the sensor inputs
        #3 update self.motor_recommandations and self.match_degree based on the decision
        pass
    
    def get_update(self):
        #checks if the Behavior should be active or inactive, and tells the bbcon about its status
        if concider_activation():
            this.bbcon.activate_behavior(self)
        if concider_deactivation():
            this.bbcon.deactivate_behavior(self)
        if not self.active_flag:
            #returns -1 if the Behavior has become inactive during get_update
            #This has to be handeled by the bbcon
            return -1
        sense_and_act()
        self.weight = self.static_priority() * self.match_degree
        return (self.weight, self.motor_request)

        
