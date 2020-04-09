import unittest

import requests


class TestUser(unittest.TestCase):
    # register with user name that already exist
    def test_Registration(self):
        url = 'https://cureona.herokuapp.com/Registration'
        myobj = {'username': 'tal', 'password': '123', 'type': 'customer'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'user name already exist'})

    def test_Login_success(self):
        url = 'https://cureona.herokuapp.com/Login'
        myobj = {'username': 'tal', 'password': '123'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'success', 'type': 'admin'})

    def testLoginFailedWrongPassword(self):
        url = 'https://cureona.herokuapp.com/Login'
        myobj = {'username': 'tal', 'password': '1234'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'failed'})

    def test_Login_Failed_user_not_exist(self):
        url = 'https://cureona.herokuapp.com/Login'
        myobj = {'username': 'asdfasdf', 'password': '1234'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'failed'})

    # ---------------------------------------------------------------------
    # business owner - check tommorow
    def test_Login_Failed_business_owner_not_exist(self):
        url = 'https://cureona.herokuapp.com/Login'
        myobj = {'username': 'asdfasdf', 'password': '1234'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'failed'})

    def test_Login_Failed_business_owner_wrong_password(self):
        url = 'https://cureona.herokuapp.com/Login'
        myobj = {'username': 'michal', 'password': '12344'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'failed'})

    def test_Login_Failed_business_owner_wrong_password2(self):
        url = 'https://cureona.herokuapp.com/Login'
        myobj = {'username': 'tomdamrib', 'password': '112233'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'failed'})

    def test_Login_success_business_owner(self):
        url = 'https://cureona.herokuapp.com/Login'
        myobj = {'username': 'michal', 'password': '12345'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'success', 'type': 'business_owner'})

    def test_Registration_business_owner(self):
        url = 'https://cureona.herokuapp.com/RegisterBusiness'
        myobj = {'username': 'talfi', 'password': '987', 'type':
            'business_owner', 'BusinessName': 'shufersal', 'CompanyId': '15951'}
        response = requests.post(url, data=myobj)
        self.assertEqual(response.json(), {'state': 'user name or cid already exist'})


if __name__ == '__main__':
    unittest.main()
