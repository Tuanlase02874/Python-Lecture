from fly import FlyWithWings
from fly import FlyNoWay
from quack import Quack
from quack import Squeak
from quack import MuteQuack


class Duck(object):
    '''Duck super class'''
    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def display(self):
        raise NotImplementedError("abstract display")

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print "All ducks float, even decoys."


class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.set_fly_behavior(FlyWithWings())
        self.set_quack_behavior(Quack())

    def display(self):
        print "green"


class RedheadDuck(Duck):
    def __init__(self):
        super(RedheadDuck, self).__init__()
        self.set_fly_behavior(FlyWithWings())
        self.set_quack_behavior(Quack())

    def display(self):
        print "red"


class RubberDuck(Duck):
    def __init__(self):
        super(RubberDuck, self).__init__()
        self.set_fly_behavior(FlyNoWay())
        self.set_quack_behavior(Squeak())

    def display(self):
        print "rubber"