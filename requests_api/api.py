from __future__ import absolute_import, division, print_function, unicode_literals

import decimal
import datetime
import json
import logging
from time import time
from urlparse import urljoin

import requests


logger = logging.getLogger(__name__)

class TestAPI(object):
    API_URL = 'api endpoint url'

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'TestPython/0.1.0',
        }
        self.params = {
            'token': self.api_key,
        }
        self.session = requests.session()
        self.testAPI = TestAPI(self)
        
    def __repr__(self):
        return '<API token: {}>'.format(self.params['key'])

    def call(self, method, url, params=None, data=None):
        
        url = urljoin(self.API_URL, url)
        logger.debug('{} to {}: {} {}'.format(method, url, params, data))
        start = time()

        response = None
        try:
            response = self.session.request(method, url, params=self.params, data=data, headers=self.headers)
            duration = (time() - start) * 1000
        except Exception as e:
            duration = (time() - start) * 1000
            logger.exception('Received {} in {:.2f}ms: {}'.format(e.__class__.__name__, duration, e))
          
        logger.debug('Received {} in {:.2f}ms: {}'.format(response.status_code, duration, response.text))

        return response


class TestAPI(object):
    def __init__(self, api):
        self.api = api

    def testcall(self, method='GET', property_id='', params=None):
        return self.api.call(method, 'test/{}'.format(property_id), params=params)

if __name__ == "__main__":
    api = TestAPI('api key')
    c = TestAPI(api).testcall()
