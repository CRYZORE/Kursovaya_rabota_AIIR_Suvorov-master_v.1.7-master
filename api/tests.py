from rest_framework.test import APITestCase


class ReplacerTests(APITestCase):
    def test_api(self):
        # url = reverse('replacer', args='abc')
        url = 'https://127.0.0.1:8000/api/s'
        response = self.client.get(url)
        self.assertEqual(response.data, {
            "first_operand": "s",
            "result": "s",
            "operation": "replace"
        })
