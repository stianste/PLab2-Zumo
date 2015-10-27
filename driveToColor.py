from Behavior import Behavior
from camera import Camera
from motor_rec import Motor_Rec
from imager2 import Imager

class driveToColor(Behavior):
    def __init__(self, sensobs, static_pri):
        super().__init__(sensobs, True, static_pri)

    def _concider_deactivation(self):
      return

    def _concider_activation(self):
      return

    def _determine_angle(self, img):
      h = img.ymax
      half = h//2
      w = img.xmax
      img = img.crop((0,half,w,half+1)) # Img is now a one-pixel tall image, same width
      # The plan is to find the first blue pixel and the last one, then finding the center of this. Lastly, drive towards it
      first = 0
      last = w
      for i in range(w):
        rgb = img.get_pixel(i,0) # If this one is above 100 we can assume it is blue for now
        if rgb[2] > rgb[0] and rgb[2] > rgb[0] and first == 0:
          first = i
        if rgb[2] > rgb[0] and rgb[2] > rgb[0]:
          last = i

      center = w // 2
      center_blue = (first+last)//2

      if center_blue > center:
        return (((center_blue-center)/center) * 26.75)
      else: # center_blue < center
        return (-((center-center_blue)/center) * 26.75)

    def _sense_and_act(self):
        img = Imager(image=self.sensob['camera'].get_value(), mode='RGB') # Get the image from the camera sensob, the value should be updated from the bbcon
        return self._determine_angle(img)



    def get_update(self): # The bbcon asks every nth second for an update, checking if the active-flag has changed
      angle = round(self._sense_and_act())
      print(angle)
      if abs(angle) < 5:
        return Motor_Rec(0, 0, 0, 2)
      else:
        return Motor_Rec(10, angle, 2, 2)