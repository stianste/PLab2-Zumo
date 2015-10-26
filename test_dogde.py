from ultrasonic import *

class Test_dogde():
	def __init__(self):
		self.priority = 1;
		self.ultrasonic = Ultrasonic();
	
	def get_suggestion(self):
		speed_value = 1.0;
		turn_value = 0.0;
		distance = self.ultrasonic.update();
		print("distance: " + str(distance));
		
		if(distance<15):
			speed_value=0;
		elif(distance<50):
			speed_value =(float(1/(distance-15))); 
		
		return speed_value, turn_value;

		