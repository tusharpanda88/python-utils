
class bus1:
    """remove passengers """

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # <1>
        else:
            self.passengers = passengers  #<2>

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)  # <3>

passengers = ['ajit', 'nikhil', 'sam', 'srini', 'jagdish']
print "actual: ",passengers
bus = bus1(passengers)
bus.drop('nikhil')
bus.drop('srini')
print "remaining: ",passengers
