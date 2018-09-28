import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.req_type = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}

    def test_n2w_test1(self):
        response = self.client.post('/n2w/', {'number': 538}, **self.req_type)

        self.assertEqual(response.status_code, 200)

        res = response.json()['res']
        self.assertEqual(res.strip(), 'five hundred thirty eight')

    def test_n2w_test2(self):
        response = self.client.post('/n2w/', {'number': 2900740315}, **self.req_type)

        self.assertEqual(response.status_code, 200)

        res = response.json()['res']
        self.assertEqual(res.strip(), 'two billion and nine hundred million and seven hundred forty thousand and three hundred fifteen')

    def test_n2w_test3(self):
        response = self.client.post('/n2w/', {'number': 1032760217400}, **self.req_type)

        self.assertEqual(response.status_code, 406)

        self.assertEqual(response.content.decode('utf-8'), 'Please enter less than billion!')

    def test_w2n_test1(self):
        response = self.client.post('/w2n/', {'text': 'five hundred thirty eight'}, **self.req_type)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json()['res'], 538)

    def test_w2n_test2(self):
        response = self.client.post('/w2n/', {'text': 'two billion and nine hundred million and seven hundred forty thousand and three hundred fifteen'},
                                    **self.req_type)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json()['res'], 2900740315)

    def test_w2n_test3(self):
        response = self.client.post('/w2n/', {'text': 'billion billion'}, **self.req_type)

        self.assertEqual(response.status_code, 406)

        # print(response.content)