from motors import Motors
from zumo_button import ZumoButton
from time import sleep

def Start():
	ZumoButton().wait_for_press();
	sleep(3);
	m = Motors();
	while(not ZumoButton().button_pressed()):
		m.forward(dur=0.1);

Start();