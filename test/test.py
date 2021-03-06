import unittest
import src.clicker

VALUE = 100
PARAM = [(100, 100), "text", 100, 100, (100, 100), 100]
PARAM_CURRENCY = [(100, 100), "text", (100, 100), 100]


class SimpleUpgradeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.upgrade_cpc = UpgradeCPC(*PARAM)
        self.upgrade_cps = UpgradeCPS(*PARAM)
        self.currency = CurrencyButton(*PARAM_CURRENCY)
        self.exchange = Currency()

    def test_click(self):
        self.assertEqual(self.upgrade_cpc.click(0, 0), (0, 0))
        self.assertEqual(self.upgrade_cpc.click(0, VALUE), (VALUE, 0))

    def test_auto_click(self):
        self.assertEqual(self.upgrade_cps.click(0, 0), (0, 0))
        self.assertEqual(self.upgrade_cps.click(0, VALUE), (VALUE, 0))

    def test_check_if_available(self):
        self.assertFalse(self.upgrade_cps.check_if_available(0))
        self.assertFalse(self.upgrade_cpc.check_if_available(0))
        self.assertTrue(self.upgrade_cps.check_if_available(VALUE))
        self.assertTrue(self.upgrade_cpc.check_if_available(VALUE))

    def test_currency(self):
        self.assertEqual(self.currency.click(0, VALUE), (VALUE * self.exchange.get_exchange_rate(), 0))


if __name__ == '__main__':
    unittest.main()
