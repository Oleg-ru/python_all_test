class Meckaniks:
    def __init__(self, name, model, **kwargs):
        self.name = name
        self.model = model
        if 'passenger' in kwargs:
            self.passenger = kwargs['passenger']
        else:
            self.passenger = 1

    def getInfo(self):
        print('name ', self.name, 'model ', self.model, 'etc ', self.passenger)


class Car(Meckaniks):
    def __init__(self,name, model, **kwargs):
        super().__init__(name, model, **kwargs)

        if 'full_track' in kwargs:
            self.full_track = kwargs['full_track']
        else:
            self.full_track = False


class Plane(Meckaniks):
    def __init__(self, name, model, **kwargs):
        super().__init__(name, model, **kwargs)

        if 'max_height' in kwargs:
            self.max_height = kwargs['max_height']

        else:
            self.max_height = 5000


plane = Plane('mig', 12, passenger=1, max_height=10000)
plane.getInfo()
print(plane.__dict__)
car = Car('Lada', 112, passenger=4, full_track=True)
car.getInfo()
print(car.__dict__)