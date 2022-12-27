import logging
from unittest import TestCase

import requests

from app.config import PORT
from app.module.link_shortner import get_link


class TestShortner(TestCase):

    def test_get_link(self):
        target_pool_name = 'mixru'
        referal_to_project = 'fortuneclock'

        link = get_link(target_pool_name, referal_to_project)
        self.assertIn('bit.ly/', link)

    def test_request_link(self):
        target_pool_name = 'mixru'
        referal_to_project = 'fortuneclock'
        response = None
        while type(response) is not requests.Response:
            try:
                response = requests.get(f'http://localhost:{PORT}/link',
                                   params={'targets_base': target_pool_name, 'project_name': referal_to_project})
            except Exception as err:
                logging.exception(err)
            else:
                self.assertIn('bit.ly/', response.text)
