import unittest

from create_kit_name_kit_test import TestClass


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClass)
    unittest.TextTestRunner().run(suite)
