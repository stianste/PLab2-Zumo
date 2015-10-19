
class Test_dogde():
	def __test_dogde__(self):
		self.priority = 1;
	
	def get_suggestion(self):
		speed_value = 1;
		turn_value = 0;
		distance = self.ultrasonic.update();
		
		if(distance<15):
			turn_value = 1;
		elif(distance<30):
			turn_value =(15/distance); 
		
		return speed_value, turn_value;