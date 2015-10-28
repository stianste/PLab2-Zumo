class Behavior():
    # constructor that takes in the bbcon this Behavior is reporting to, what sensors it uses,
    # if it is currently active, and a static priority. 
    def __init__(self, sensobs, active_flag, static_priority):
        self.sensobs = sensobs
        self.active_flag = active_flag
        self.motor_recommendation = [] # List of possible motor recommendations ? Can be implemented differently for each behavior
        # static_priority is a static, final varibale. It should not be changed after init. Dont know how to do this in python
        self.static_priority = static_priority

        # Below are some effectivley abstract classes. Each subclass of Behavior have to define these functions themselves. 
    def _update_flag(self):
     	# REMEMBER TO DO THIS
        raise Exception('_update_flag was not implemented in class Behavior')
    def _sense_and_act(self):
        #This is the main function of the Behavoir class. This function should:
        #1 get an update from all sensobs in its sensob list self.sensob
        #2 make a decision based on the sensor inputs
        #3 update self.motor_recommandations and self.match_degree based on the decision
        return


    def get_update(self):
        self._sense_and_act()
        self.weight = self.static_priority * self.match_degree
        return (self.weight, self.motor_request)
