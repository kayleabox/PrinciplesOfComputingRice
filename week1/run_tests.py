import unittest

START_DIR = 'tests'

loader = unittest.TestLoader()
suite = loader.discover(START_DIR)
runner = unittest.TextTestRunner()

runner.run(suite)