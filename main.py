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
		
		if(turn_value>0):
			m.left(turn_value);
		else:
			m.forward(0.1);

Start();