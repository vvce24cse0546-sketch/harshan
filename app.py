import unittest
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(20,20),40)

  def test_subtract(self):
    self.assertEqual(subtract(20,10),10)

  def test_multiply(self):
    self.assertEqual(multiply(20,20),40)
