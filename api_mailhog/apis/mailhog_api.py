import requests

from restclient.client import Restclient


class MailhogApi(Restclient):

    def get_api_v2_messages(
            self
    ):
        """
        Get users emails
        :return:
        """
        response = self.get(
            path=f'/api/v2/messages?limit=50'
        )
        return response
