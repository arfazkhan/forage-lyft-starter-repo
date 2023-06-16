class Battery:
    def __init__(self, type, age):
        self.type = type
        self.age = age

    def is_due_for_service(self):
        if self.type == "Spindler":
            return self.age >= 2
        elif self.type == "Nubbin":
            return self.age >= 4
        else:
            raise ValueError("Unknown battery type")

    def get_age_to_service(self):
        if self.type == "Spindler":
            return 2 - self.age
        elif self.type == "Nubbin":
            return 4 - self.age
        else:
            raise ValueError("Unknown battery type")

