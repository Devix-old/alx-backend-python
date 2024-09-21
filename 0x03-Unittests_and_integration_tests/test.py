from utils import get_json
import unittest
from unittest.mock import patch, Mock


class TestGetJson(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_json(self, mock_get):
        mock_response = Mock()
        response_dict = {'name': 'Mohamed', 'email': 'med.elgh@example.com'}
        mock_response.json.return_value = response_dict
        mock_get.return_value = mock_response
        result = get_json('example.com')
        print(result)

if __name__ == '__main__':
    unittest.main()
