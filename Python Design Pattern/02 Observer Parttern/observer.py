class Observer(object):
    '''Observer interface class'''
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError('abstract Observer')