import unittest
from bill import Bill, SavingBill, NotEnoughMoney


# XUnit, JUnit

class TestBill(unittest.TestCase):

    def setUp(self):
        print('Я выполняюсь до кождого теста')
        self.bill = Bill()

    def tearDown(self):
        print('Я выполняюсь после каждого теста')
        del self.bill

    def test_init(self):
        self.bill = Bill()
        self.assertEqual(self.bill.money, 0)
        self.assertEqual(len(self.bill.history), 0)
        self.assertEqual(self.bill.history, [])
        self.assertFalse(self.bill.history)

    def test_add(self):
        self.bill.add(100)
        self.assertEqual(self.bill.money, 100)

    def test_can_by(self):
        self.bill.add(100)
        self.assertTrue(self.bill.can_by(50))
        self.assertFalse(self.bill.can_by(150))

    def test_buy(self):
        self.bill.add(100)
        self.bill.buy(50, 'test')
        self.assertEqual(self.bill.money, 50, msg='Осталось неверная сумма денег')
        self.assertListEqual(self.bill.history, [('test', 50)])

        # проверка на ошибку
        with self.assertRaises(NotEnoughMoney):
            self.bill.buy(100, 'test')


class TestSavingBill(unittest.TestCase):

    def setUp(self):
        self.bill = SavingBill()


    def test_can_by(self):
        self.assertFalse(self.bill.can_by(50))

    def test_buy(self):
        with self.assertRaises(Exception):
            self.bill.buy(20, 'test')


# for test in self.tests:
# self.setUp()
# test()
# self.tearDown()