import unittest
from vehicle_info import VehicleInfo


class TestVehicleInfo(unittest.TestCase):

    def test_compute_tax_non_electric(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(), 500)

    def test_compute_tax_electric(self):
        v = VehicleInfo("BMW", True, 10000)
        self.assertEqual(v.compute_tax(), 200)

    def test_compute_tax_exemption(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(5000), 250)

    def test_compute_tax_exemption_negative(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertRaises(ValueError, v.compute_tax, -5000)

    def test_compute_tax_exception_high(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(20000), 0)

    def test_can_leave_false(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertFalse(v.can_lease(5000))

    def test_can_lease_true(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertTrue(v.can_lease(15000))

    def test_can_lease_negative_income(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertRaises(ValueError, v.can_lease, -5000)


unittest.main()
