import json


from app.utils.testing import ApiTestCase


class UserApiTest(ApiTestCase):

    user_data = {
        'email': 'something@email.com',
        'password': '123456',
    }

    def test_registration(self):
        response = self.app.post('/api/v1/user', data=self.user_data)
        data = json.loads(response.data)

        assert data['id'] == 1
        assert len(data['token']) > 10
