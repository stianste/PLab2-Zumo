class BBCON():

    def __init__(self, behaviors, sensobs, motobs):
        #init instance variables from input.
        self.behaviors = behaviors
        self.active_behaviors = []
        self.sensobs = sensobs 
        self.motobs = motobs 
        self.arbitrator = arbitrator()

    #unnecessary(?) method
    def add_behavior(self, behavior):
        self.behaviors.appen(behavior)
    
    def activate_behavior(self, behavior):
        #activates behavior if it is in behaviors list, and adds it to the active ones. 
        if not behavior in self.behaviors:
            print('Behavior not in behaviors list')
            return
        behavior.active_flag = True
        self.active_behaviors.append(behavior)
    
    def deactivate_behavior(self, behavior):
        #activates behavior if it is in behaviors list, and adds it to the active ones. 
        if not behavior in self.active_behaviors:
            print('Behavior not in behaviors list')
            return
        behavior.active_flag = False
        self.active_behaviors.remove(behavior)
    
