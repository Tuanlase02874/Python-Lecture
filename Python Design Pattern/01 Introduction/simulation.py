from duck import MallardDuck
from fly import FlyNoWay


if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.set_fly_behavior(FlyNoWay())
    mallard.perform_fly()