class Engine:
    def start(self):
        print("Engine started")


class Car(Engine):
    pass

car = Car()
car.start()