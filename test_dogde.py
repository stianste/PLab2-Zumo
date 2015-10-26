from ultrasonic import *

class Test_dogde():
	def __init__(self):
		self.priority = 1;
		self.ultrasonic = Ultrasonic();
	
	def get_suggestion(self):
		speed_value = 1;
		turn_value = 0.0;
		distance = self.ultrasonic.update();
		print("distance: " + str(distance));
		
		if(distance<10 and distance>0):
			speed_value = -(1/distance);
		elif distance<15:
			speed_value = 0;
		elif(distance<40):
			speed_value =(float((distance)/30)); 
		
		return speed_value, turn_value;

		