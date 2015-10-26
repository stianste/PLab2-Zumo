from ultrasonic import *

class Test_dogde():
	def __init__(self):
		self.priority = 1;
		self.ultrasonic = Ultrasonic();
	
	def get_suggestion(self):
		speed_value = 0;
		turn_value = 0.0;
		distance = self.ultrasonic.update();
		print("distance: " + str(distance));
		
		if(distance<13):
			speed_value = -(5/distance);
		elif(distance>15 and distance<30):
			speed_value =(float((distance)/30)); 
		
		return speed_value, turn_value;

		