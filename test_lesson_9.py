import pytest
from lotoClass_lesson9 import Card


class TestCard:

    def test_init(self):
        cardtest = Card('Игрок', True, 1, 15)  # формируем карточку комп
        assert len(cardtest.card) == 3
        assert type(cardtest.card) == type([])
        assert len(cardtest.card[0]) == 9
        assert cardtest.name == 'Игрок'
        assert cardtest.yes_no == True
        assert cardtest.break_game == 1
        assert cardtest.win == 15

    def test_bar_yes_no(self):
        cardtest = Card('Игрок', True, 1, 15)  # формируем карточку комп
        cardtest.bar_yes_no(10)
        if 10 in cardtest.card[0] or 10 in cardtest.card[1] or 10 in cardtest.card[2]:
            assert cardtest.yes_no == True
        else:
            assert cardtest.yes_no == False

    def test_bar_minus_card(self): # в карточке заменяем выпавшее число на Х
        cardtest = Card('Игрок', True, 1, 15)  # формируем карточку комп
        for i in cardtest.card[0]:
            bar = i
            if type(bar) == type(1):
                break
        cardtest.bar_minus_card(bar)
        assert ("X" in cardtest.card[0]) == True



    #     assert person.age == 40
    #
    # def test_set_age(self):
    #     person = Person('as',20)
    #     try:
    #         person.age = -40
    #     except:
    #         assert  True
    #     else:
    #         assert False
