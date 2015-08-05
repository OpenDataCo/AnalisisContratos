from test_helper import *
from transformations import *

class TestCleaner(unittest.TestCase):

  def test_clean_identification_with_id_type(self):
    result = cleanIdentificacion("c.c 123456")
    expected = { "numero": 123456, "tipo":"cc" }
    self.assertEqual(expected, result)

  def test_clean_identification_without_id_type(self):
    result = cleanIdentificacion(" 123456")
    expected = { "numero": 123456, "tipo":"" }
    self.assertEqual(expected, result)
