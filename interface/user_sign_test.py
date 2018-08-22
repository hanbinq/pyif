import unittest
import os, sys
try:
    from mac.sign_request import SignRequests
except ImportError:
    from .mac.sign_request import SignRequests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data


class UserSignTest(unittest.TestCase):
    """用户签到"""

    def setUp(self):
        self.url = "api/user_sign/"

    def tearDown(self):
        print(self.result)

    def test_user_sign_all_null(self):
        """参数为空"""
        data = {'eid': '', 'phone': ''}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_user_sign_eid_error(self):
        """eid=901 查询结果不存在"""
        data = {'eid': 901, 'phone': 13711001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id null')

    def test_user_sign_status_close(self):
        """eid=3 发布会状态关闭"""
        data = {'eid': 3, 'phone': 13711001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event status is not available')

    def test_user_sign_time_start(self):
        """eid=4 发布会已开始"""
        data = {'eid': 4, 'phone': 13711001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertEqual(self.result['message'], 'event has started')

    def test_user_sign_phone_error(self):
        """phone=10100001111 手机号不存在"""
        data = {'eid': 1, 'phone': 10100001111}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10025)
        self.assertEqual(self.result['message'], 'user phone null')

    def test_user_sign_eid_phone_error(self):
        """eid=1, phone=13511001102 手机号与发布会不匹配"""
        data = {'eid': 1, 'phone': 13511001102}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10026)
        self.assertEqual(self.result['message'], 'user did not participate in the conference')

    def test_user_sign_has_sign_in(self):
        """已签到"""
        data = {'eid': 1, 'phone': 13511001101}
        r = SignRequests().post(self.url,data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10027)
        self.assertEqual(self.result['message'], 'user has sign in')

    def test_user_sign_success(self):
        """签到成功"""
        data = {'eid': 1, 'phone': 13511001100}
        r = SignRequests().post(self.url, data)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'sign success')


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()





