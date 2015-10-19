from motors import Motors
from zumo_button import ZumoButton
from time import sleep

def Start():
	ZumoButton().wait_for_press();
	sleep(3);
	m = Motors();
	i = 0;
	while(not ZumoButton().button_pressed()):
		i+=1;
		m.forward(dur=0.5);
		if(i>10):
			m.stop();	
	m.stop();

Start();