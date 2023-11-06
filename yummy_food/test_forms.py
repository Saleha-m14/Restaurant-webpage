from django.test import TestCase
from .forms import TableBookingForm


class TestTableBookingForm(TestCase):

    def test_name_field_is_required(self):
        form = TableBookingForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required')
