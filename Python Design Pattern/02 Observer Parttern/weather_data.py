from subject import Subject


class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def register_observer(self, observer):
        '''If need to register observer, just add it to observers list
        '''
        self.observers.append(observer)

    def remove_observer(self, observer):
        '''The same, if observer wants to unregister, we will remove
        him from observer list.'''
        if observer in self.observers:
            self.observers.remove(observer)

    def measurements_changed(self):
        self.set_changed()
        self.notify_observers()  # We do not pass data, means use pull mode

    def set_changed(self):
        self.changed = True

    def notify_observers(self):
        '''We sent statement to every observers. Since all observers
         implement update() method, we know how to notify them.'''
        if self.changed:
            for observer in self.observers:
                observer.update()
            self.changed = False

    def measurements_changes(self):
        '''We need to notify observers when we get measurements from
        Weather-O-Rama company.'''
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        '''We will use this method to test billboard.'''
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

    # Below three are examples of getter methods
    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    # Other methods in WeatherData