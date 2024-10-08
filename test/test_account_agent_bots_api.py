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
from chatwoot_client.apis.account_agent_bots_api import AccountAgentBotsApi  # noqa: E501
from chatwoot_client.rest import ApiException


class TestAccountAgentBotsApi(unittest.TestCase):
    """AccountAgentBotsApi unit test stubs"""

    def setUp(self):
        self.api = AccountAgentBotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_an_account_agent_bot(self):
        """Test case for create_an_account_agent_bot

        Create an Agent Bot  # noqa: E501
        """
        pass

    def test_delete_an_account_agent_bot(self):
        """Test case for delete_an_account_agent_bot

        Delete an AgentBot  # noqa: E501
        """
        pass

    def test_get_details_of_a_single_account_agent_bot(self):
        """Test case for get_details_of_a_single_account_agent_bot

        Get an agent bot details  # noqa: E501
        """
        pass

    def test_list_all_account_agent_bots(self):
        """Test case for list_all_account_agent_bots

        List all AgentBots  # noqa: E501
        """
        pass

    def test_update_an_account_agent_bot(self):
        """Test case for update_an_account_agent_bot

        Update an agent bot  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
