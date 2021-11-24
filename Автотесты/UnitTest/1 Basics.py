'''
Тесты создаются внутри выдуманного класса, который наследуется от unittest.TestCase.

Сами тесты располагаются в методах этого класса. Можно располагать тестирование функции в один метод, а разные кейсы
(например даем разные переменные) класть внутрь этого метода:


lass TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


Название метода должно начинаться с test_ иначе тест не будет выполнен, unittest просто пропустит его.
В терминале, пройденный тест указывается как точка, количество тестов = количество методов, а не количество кейсов.
Тесты идут в рандомном порядке. Проваленный тест указывается не как точка, а как F (..F... = 2 теста ок, 1 F, 3 ок)


В кейсах используются разные методы assert:

assertEqual(a, b) = a == b
assertNotEqual(a, b) = a != b
assertTrue(x) = bool(x) is True
assertFalse(x) = bool(x) is False
assertIs(a, b) = a is b
assertIsNot(a, b) = a is not b
assertIsNone(x) = x is None
assertIsNotNone(x) = x is not None
assertIn(a, b) = a in b
assertNotIn(a, b) = a not in b
assertIsInstance(a, b) = isinstance(a, b)
assertNotIsInstance(a, b) = not isinstance(a, b)


Еще есть assertRaises, которое проверяет, что было поднято какое-то исключение. Используется так (2 способа):

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

        self.assertRaises(ValueError, calc.divide, 10, 0)

В первом контекстным менеджером, тут указывается тип исключения, в теле вызывается сама функция как обычно.
Во втором аргументами передается:
тип исключения
имя функции, которую надо вызвать (без скобок, не вызываем, только имя)
аргументы для вызываемой функции
'''