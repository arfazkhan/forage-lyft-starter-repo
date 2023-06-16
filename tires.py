class Tires:
    def __init__(self, tread_depth):
        self.tread_depth = tread_depth

    def is_due_for_service(self):
        return self.tread_depth <= 2

