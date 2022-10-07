
import unittest
import xmlrunner
from main import Test_Class


if __name__ == "__main__":

    test_suit = unittest.TestSuite()
    test_suit.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(Test_Class)
    ])

    with open("/Users/appperfect/Desktop/JATIN/Appium/scripts/report.xml", "w") as report:
        test_runner = xmlrunner.XMLTestRunner(report)
        test_runner.run(test_suit)








