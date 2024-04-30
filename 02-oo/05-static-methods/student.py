class Duration:
    def __init__(self, duration_in_hours):
        self.__duration_in_hours = duration_in_hours

    @property
    def hours(self):
        return self.__duration_in_hours
    
    @property
    def minutes(self):
        return self.__duration_in_hours*60
    
    @property
    def seconds(self):
        return self.__duration_in_hours*3600
    
    @staticmethod
    def from_hours(hours):
        return Duration(hours)
    
    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes/60)
    
    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds/3600)