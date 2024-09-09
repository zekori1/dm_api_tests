
from restclient.client import Restclient


class AccountApi(Restclient):

    def post_v1_account(
            self,
            json_data
            ):
        """
        Register new user
        :param json_data:
        :return:
        """
        response = self.post(
            path=f'/v1/account',
            json=json_data
        )
        return response

    def put_v1_account_token(
            self,
            token
            ):
        """
        Activate registered user
        :param token:
        :return:
        """
        headers = {
            'accept': 'text/plain',
        }
        response = self.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        return response