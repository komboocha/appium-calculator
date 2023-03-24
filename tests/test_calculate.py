class TestCalculator:

    def test_add_values(self, calculate_screen):
        calculate_screen.add_values()

        assert calculate_screen.get_result() == '3'

    def test_multiply_values(self, calculate_screen):
        calculate_screen.multiply_values()

        assert calculate_screen.get_result() == '6'

    def test_division_values(self, calculate_screen):
        calculate_screen.divide_values()

        assert calculate_screen.get_result() == '1.5'

    def test_subtract_values(self, calculate_screen):
        calculate_screen.subtract_values()

        assert calculate_screen.get_result() == "−1"

    def test_sinus_function(self, calculate_screen):
        calculate_screen.sinus_method(90)
        assert calculate_screen.get_result() == "1"

    def test_calculate_root(self, calculate_screen):
        calculate_screen.calculate_root(4)
        assert calculate_screen.get_result() == "2"


