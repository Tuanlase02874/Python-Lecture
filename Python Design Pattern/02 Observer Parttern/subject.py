class Subject(object):
    '''Subject interface class'''
    def register_observer(self, observer):
        raise NotImplementedError('abstract Subject')

    def remove_observer(self, observer):
        raise NotImplementedError('abstract Subject')

    def notify_observers(self):
        raise NotImplementedError('abstract Subject')