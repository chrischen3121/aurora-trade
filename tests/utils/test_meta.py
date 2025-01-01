#!/usr/bin/env python
from artrade.utils import meta


class TestSingleton:
    def test_one_class(self):
        class Singleton(metaclass=meta.Singleton):
            pass

        obj1 = Singleton()
        obj2 = Singleton()
        assert id(obj1) == id(obj2)

    def test_two_classes(self):
        class Singleton1(metaclass=meta.Singleton):
            pass

        class Singleton2(metaclass=meta.Singleton):
            pass

        obj1 = Singleton1()
        obj2 = Singleton2()
        assert id(obj1) != id(obj2)

    def test_with_args(self):
        class Singleton(metaclass=meta.Singleton):
            def __init__(self, a, b=1):
                self.a = a
                self.b = b

        obj1 = Singleton(2, 4)
        obj2 = Singleton(3, 6)  # new args will not be valid
        assert id(obj1) == id(obj2)
        assert obj1.a == 2
        assert obj1.b == 4
        assert obj2.a == 2

    def test_with_kwargs(self):
        class Singleton(metaclass=meta.Singleton):
            def __init__(self, a, b=1):
                self.a = a
                self.b = b

        obj1 = Singleton(2, b=4)
        obj2 = Singleton(3, b=6)  # new args will not be valid
        assert id(obj1) == id(obj2)
        assert obj2.a == 2
        assert obj2.b == 4

    def test_garbage_collection(self):
        class Singleton(metaclass=meta.Singleton):
            def __init__(self, a, b=1):
                self.a = a
                self.b = b

        obj1 = Singleton(2, 4)
        obj1_id = id(obj1)
        del obj1
        obj2 = Singleton(3, 5)
        assert obj1_id == id(obj2)
        assert obj2.a == 2
