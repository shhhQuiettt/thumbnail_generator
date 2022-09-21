from django.test import TestCase
from .models import Thumbnail, _get_original_image_path, _get_thumbnail_image_path
from django.contrib.auth import get_user_model
import unittest

# Create your tests here.


class ModelHelpersTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            email="qwer@qwer.com", password="password"
        )

        class MockImage:
            owner = cls.user

        cls.mock_image_instance = MockImage()

        class ThumbnailSizeMock:
            height = 200

        class MockThumbnail:
            original_img = cls.mock_image_instance
            size = ThumbnailSizeMock()

        cls.mock_thumbnail_instance = MockThumbnail()

    def test_get_original_image_path(self):
        filename = "kitty.png"

        expected_path = f"user_{self.user.pk}/kitty/original.png"
        actual_path = _get_original_image_path(self.mock_image_instance, filename)

        self.assertEqual(expected_path, actual_path)

    @unittest.skip("Mock better")
    def test_get_thumbnail_image_path(self):
        filename = "asdfasdfasfd.png"

        expected_path = f"user_{self.user.pk}/kitty/200px.png"
        actual_path = _get_thumbnail_image_path(self.mock_thumbnail_instance, filename)

        self.assertEqual(expected_path, actual_path)
