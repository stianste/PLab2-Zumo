from Behavior import Behavior
from motor_rec import Motor_Rec

class Derp(Behavior):
  def __init__(self, static_priority):
    super([], True, static_priority)
    self.forward = True

  def get_update(self):
    self.forward = !self.forward
    if self.forward:
      return Motor_Rec(10, 0, 1, 2)
    else:
      return Motor_Rec(10, 0, -1, 2)
