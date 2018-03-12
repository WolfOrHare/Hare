import unittest
from tools import HTMLTestRunner


suite = unittest.TestLoader().discover('testsuites')

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)


