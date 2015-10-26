from Queue import PriorityQueue

class Arbitrator():
    def __init__(self):
        self.motor_recs = PriorityQueue() #instansiates a min queue of motor_recommendations
    def add_mr(motor_rec):
        motor_rec.pri = motor_rec.pri*-1 #Since the motor reccomendations queue is
        # a min que, we have to change the values so that it chooses the biggest element. THis inverts the min queue. 
        self.motobs.put(motor_rec)

    def choose_action(self):
        #gets the motor_rec with highest priority, returns it and empties the queueue 
        val = self.motor_recs.get()
        self.motor_recs = PriorityQue()
        return val
