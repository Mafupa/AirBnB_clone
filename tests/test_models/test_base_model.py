#!/usr/bin/python3
"""Test Base Model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_base_model_creation(self):
        my_model = BaseModel()
        my_model.name = "Test Model"
        self.assertEqual(my_model.name, "Test Model")

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


if __name__ == "__main__":
    unittest.main()
