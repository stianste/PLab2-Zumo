from motors import Motors
from zumo_button import ZumoButton

def Start():
	ZumoButton().wait_for_press();
	m = Motors();
	m.forward(dur=100);

Start();