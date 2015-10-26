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
		
		if(distance<10):
			return -1,turn_value;
		elif(distance>15 and distance<100):
			speed_value =(float((distance)/100)); 
		
		return speed_value, turn_value;

		