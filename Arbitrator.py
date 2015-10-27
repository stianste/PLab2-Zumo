
class Arbitrator():
    def __init__(self):
        self.motor_recs = [] #instansiates a min queue of motor_recommendations

    def add_mr(self, motor_rec):

        self.motor_recs.append(motor_rec)

    def choose_action(self):
        #gets the motor_rec with highest priority, returns it and empties the queueue 
        val = max(self.motor_recs)
        self.motor_recs = []
        return val
