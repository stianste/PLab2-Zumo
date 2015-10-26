from motors import Motors
from zumo_button import ZumoButton
from time import sleep
from test_dogde import Test_dogde

def Start():
	ZumoButton().wait_for_press();
	sleep(3);
	m = Motors();
	d = Test_dogde();
	while(not ZumoButton().button_pressed()):
		speed_value,turn_value = d.get_suggestion();
		
		print("forward" + str(speed_value));
		if speed_value<0:
			m.backward(1);
		else:
			m.forward(speed_value*0.2);
		

Start();