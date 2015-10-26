from ultrasonic import *

class Test_dogde():
	def __test_dogde__(self):
		self.priority = 1;
	
	def get_suggestion(self):
		speed_value = 1.0;
		turn_value = 0.0;
		distance = self.ultrasonic.update();
		
		if(distance<15):
			speed_value=0;
		elif(distance<50):
			speed_value =(float(1/(distance-15))); 
		
		return speed_value, turn_value;

		