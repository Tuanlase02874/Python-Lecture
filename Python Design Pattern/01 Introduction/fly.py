class FlyBehavior(object):
    '''FlyBehavior interface class'''
    def fly(self):
        raise NotImplementedError('abstract FlyBehavior')


class FlyWithWings(FlyBehavior):
    def fly(self):
        print "I'm flying!!"


class FlyNoWay(FlyBehavior):
    def fly(self):
        print "I can't fly"