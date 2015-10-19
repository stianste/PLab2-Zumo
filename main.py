from motors import Motors
from zumo_button import ZumoButton

def Start():
	ZumoButton().wait_for_press();
	m = Motors();
	i = 0;
	while(m.button_pressed()):
		i+=1;
		m.forward(dur=0.5);
		if(i>10):
			m.stop();	
	m.stop();

Start();