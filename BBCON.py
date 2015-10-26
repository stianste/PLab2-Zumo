from time import sleep

class BBCON():

    def __init__(self, behaviors, sensobs, motob):
        #init instance variables from input.
        self.behaviors = set(behaviors)
        self.active_behaviors = self.behaviors
        self.sensobs = sensobs # Dictionary of sensobject, 'camera' -> camera sensobj
        self.arbitrator = arbitrator()
        self.motob = motob

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

    def _update_sensobs(self):
          for ob in self.sensobs:
              ob.update()

    def _update_behaviors(self):
        for behavior in self.behaviors:
            MR = behavior.get_update() # this also toggels the active_flag for the behavior
            if behavior in self.active_behaviors:
                self.arbitrator.add(MR)
                if not behavior.active_flag:
                  self.active_behaviors.remove(behavior)
            else:
              if behavior.active_flag:
                self.active_behaviors.add(behavior)

    def loop(self):
      self._update_sensobs()
      self._update_behaviors()
      MR = self.arbitrator.choose_action()
      self.motob.update(MR)
      sleep(1)

