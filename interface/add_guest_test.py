import unittest
import os, sys
try:
    from mac.sign_request import SignRequests
except ImportError:
    from .mac.sign_request import SignRequests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class AddGuessTest(unittest.TestCase):
    """添加嘉宾"""

    def setUp(self):
        self.url = "api/add_guest/"

    def tearDown(self):
        print(self.result)

    def test_add_guest_all_null(self):
        """参数为空"""
        data = {'eid': '', 'realname': '', 'phone': ''}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_guest_eid_null(self):
        """eid=901 查询为空"""
        data = {'eid': 901, 'realname': 'tom', 'phone': 13711001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id null')

    def test_add_guest_status_close(self):
        """eid=2 状态未开启"""
        data = {'eid': 3, 'realname': 'tom', 'phone': 13711001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event status is not available')

    def test_add_guest_limit_full(self):
        """eid=2 发布会人数已满"""
        data = {'eid': 2, 'realname': 'tom', 'phone': 13711001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'event number is full')

    def test_add_guest_time_start(self):
        """eid=4 发布会已开始"""
        data = {'eid': 4, 'realname': 'tom', 'phone': 13711001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'event has started')

    def test_add_guest_phone_repeat(self):
        """phone=13800113001 手机号重复"""
        data = {'eid': 1, 'realname': 'tom', 'phone': 13511001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'the event guest phone number repeat')

    def test_add_guest_success(self):
        """添加成功"""
        data = {'eid': 1, 'realname': 'tom', 'phone': 13511001199}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add guest success')


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()



