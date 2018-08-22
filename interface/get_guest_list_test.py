import unittest
import os, sys
try:
    from mac.sign_request import SignRequests
except ImportError:
    from .mac.sign_request import SignRequests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class GetGuestListTest(unittest.TestCase):
    """"获得嘉宾列表"""

    def setUp(self):
        self.url = "api/get_guest_list/"

    def tearDown(self):
        print(self.result)

    def test_get_guest_list_eid_null(self):
        """eid 参数为空"""
        payload = {'eid': ''}
        r = SignRequests().get(self.url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'eid cannot be empty')

    def test_get_event_list_eid_error(self):
        """根据 eid 查询结果为空"""
        payload = {'eid': 901}
        r = SignRequests().get(self.base_url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        """根据 eid 查询结果成功"""
        payload = {'eid': 1}
        r = SignRequests().get(self.base_url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['realname'],'alen')
        self.assertEqual(self.result['data'][0]['phone'],'13511001100')

    def test_get_event_list_eid_phone_null(self):
        """根据 eid 和phone 查询结果为空"""
        payload = {'eid': 1, 'phone': '19500002412'}
        r = SignRequests().get(self.base_url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_phone_success(self):
        """根据 eid 和phone 查询结果成功"""
        payload = {'eid': 1, 'phone': '13511001100'}
        r = SignRequests().get(self.base_url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['realname'],'alen')
        self.assertEqual(self.result['data']['phone'],'13511001100')


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()

