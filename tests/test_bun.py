from praktikum.bun import Bun


class TestBun:
    # Тестирование метода get_name()
    def test_get_correct_name(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        # Проверяем, что метод возвращает правильное название булки
        assert bun.get_name() == 'Флюоресцентная булка R2-D3'

    # Тестирование метода get_price()
    def test_get_correct_price(self):
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        # Проверяем, что метод возвращает правильную цену булки
        assert bun.get_price() == 988
