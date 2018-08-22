import unittest
import os, sys
try:
    from mac.sign_request import SignRequests
except ImportError:
    from .mac.sign_request import SignRequests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class GetEventListTest(unittest.TestCase):
    """ 获得发布会列表 """

    def setUp(self):
        self.url = "api/get_event_list/"

    def tearDown(self):
        print(self.result)

    def test_get_event_list_eid_error(self):
        """eid=901 查询结果为空"""
        payload = {'eid': 901}
        r = SignRequests().get(self.url, payload)
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
        self.assertEqual(self.result['data']['name'], '红米Pro发布会')
        self.assertEqual(self.result['data']['address'], '北京会展中心')

    def test_get_event_list_nam_result_null(self):
        """关键字‘abc’查询"""
        payload = {'name': 'abc'}
        r = SignRequests().get(self.base_url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_name_find(self):
        """关键字‘发布会’模糊查询"""
        payload = {'name': '发布会'}
        r = SignRequests().get(self.base_url, payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['name'], '红米Pro发布会')
        self.assertEqual(self.result['data'][0]['address'], '北京会展中心')


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()

