#!/usr/bin/python3
"""Test Base Model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model_creation():
        my_model = BaseModel()
        my_model.name = "Test Model"
        self.assertEqual(my_model.name, "Test Model")


if __name__ == "__main__":
    unittest.main()
