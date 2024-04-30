class LengthConverter:
    def __init__(self):
        self.__distance_in_m = 0

    @property
    def meter(self):
        return self.__distance_in_m
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_m = value
    
    @property
    def inch(self):
        return self.__distance_in_m * 39.3701
    
    @inch.setter
    def inch(self, value):
        self.__distance_in_m = value/39.3701

    @property
    def feet(self):
        return self.__distance_in_m * 3.28084
    
    @feet.setter
    def feet(self, value):
        self.__distance_in_m = value/3.28084

