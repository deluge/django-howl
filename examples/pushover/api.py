import logging

import requests
from django.template.loader import render_to_string


logger = logging.getLogger(__name__)


class PushoverException(requests.RequestException):
    pass


class PushoverApi(object):

    def __init__(self, app_token):
        self.app_token = app_token

    def send_message(self, params):
        params.update({'token': self.app_token})

        try:
            response = requests.post('https://api.pushover.net/1/messages.json', params=params)
            return response
        except requests.RequestException as exc:
            raise PushoverException(exc, response=exc.response)

    def send_notification(self, recipient, title, template, **context):
        params = {
            'message': render_to_string('pushover/{0}.txt'.format(template), context).strip(),
            'title': title,
            'user': recipient,
        }
        response = self.send_message(params)

        if not response.ok:
            try:
                errors = ', '.join(response.json()['errors'])
            except ValueError:
                errors = 'Unkown error'
            logger.critical(errors)
            raise PushoverException(errors, response=response)

        return True
