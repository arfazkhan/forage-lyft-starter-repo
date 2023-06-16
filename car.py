class Car:
    def __init__(self, model, engine, battery, tires):
        self.model = model
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def is_due_for_service(self):
        return self.engine.is_due_for_service() or self.battery.is_due_for_service() or self.tires.is_due_for_service()