class TireService:
    def __init__(self, tread_depth_threshold):
        self.tread_depth_threshold = tread_depth_threshold

    def is_due_for_service(self, tires):
        return tires.tread_depth <= self.tread_depth_threshold

