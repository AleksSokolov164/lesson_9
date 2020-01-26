import pytest
from persons01 import Person


class TestPerson:

    def test_get_age(self):
        person = Person('Alex',40)
        assert person.get_age() == 'Alex - 40'

    def test_init_(self):
        person = Person('Alex',40)
        assert person.name == 'Alex'
        assert person.age == 40

    def test_set_age(self):
        person = Person('as',20)
        try:
            person.age = -40
        except:
            assert  True
        else:
            assert False
