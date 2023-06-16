class Engine:
    def __init__(self, type, mileage, warning_indicator_on):
        self.type = type
        self.mileage = mileage
        self.warning_indicator_on = warning_indicator_on

    def is_due_for_service(self):
        if self.type == "Capulet":
            return self.mileage >= 30000
        elif self.type == "Willoughby":
            return self.mileage >= 60000
        elif self.type == "Sternman":
            return self.warning_indicator_on
        else:
            raise ValueError("Unknown engine type")

    def get_mileage_to_service(self):
        if self.type == "Capulet":
            return 30000 - self.mileage
        elif self.type == "Willoughby":
            return 60000 - self.mileage
        elif self.type == "Sternman":
            return 0
        else:
            raise ValueError("Unknown engine type")

