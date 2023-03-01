import unittest
from Classes import Car, ElectricCar

class TestCarClass(unittest.TestCase):
    """Test cases for the Car Class"""
    
    def setUp(self) -> None:
        self.test_car = Car("TEST_MAKE", "TEST_MODEL", 2077, "TEST_COLOR")
        self.test_car2 = Car("TEST_MAKE2", "TEST_MODEL2", 2077)

    def test_car_init(self):
        """Test if the Car class is being created correctly"""

        # test make's
        self.assertEqual('test_make', self.test_car.make)
        self.assertEqual('test_make2', self.test_car2.make)

        # models
        self.assertEqual('test_model', self.test_car.model)
        self.assertEqual('test_model2', self.test_car2.model)

        # year
        self.assertEqual(2077, self.test_car.year)
        self.assertEqual(2077, self.test_car2.year)

        # color, test for none case
        self.assertEqual("test_color", self.test_car.color)
        self.assertEqual("white", self.test_car2.color)

        # new cars, odometer should be 0
        self.assertEqual(0, self.test_car.odometer)
        self.assertEqual(0, self.test_car2.odometer)

class TestElectricCar(unittest.TestCase):
    """Test cases for the ElectricCar class"""
    def setUp(self):
        self.test_car = Car("TEST", "TEST", 0)
        self.test_ec = ElectricCar("TEST", "TEST", 0)

    def test_noise_check(self):
        """test if cars and electric cars sound different"""

        self.assertNotEqual(self.test_car.go_fast_noises(), self.test_ec.go_fast_noises())

if __name__ == '__main__':
    unittest.main()