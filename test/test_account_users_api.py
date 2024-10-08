# coding: utf-8

"""
    Chatwoot

    This is the API documentation for Chatwoot server.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@chatwoot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import chatwoot_client
from chatwoot_client.apis.account_users_api import AccountUsersApi  # noqa: E501
from chatwoot_client.rest import ApiException


class TestAccountUsersApi(unittest.TestCase):
    """AccountUsersApi unit test stubs"""

    def setUp(self):
        self.api = AccountUsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_an_account_user(self):
        """Test case for create_an_account_user

        Create an Account User  # noqa: E501
        """
        pass

    def test_delete_an_account_user(self):
        """Test case for delete_an_account_user

        Delete an Account User  # noqa: E501
        """
        pass

    def test_list_all_account_users(self):
        """Test case for list_all_account_users

        List all Account Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
