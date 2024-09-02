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
from chatwoot_client.apis.messages_api import MessagesApi  # noqa: E501
from chatwoot_client.rest import ApiException


class TestMessagesApi(unittest.TestCase):
    """MessagesApi unit test stubs"""

    def setUp(self):
        self.api = MessagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_a_new_message_in_a_conversation(self):
        """Test case for create_a_new_message_in_a_conversation

        Create New Message  # noqa: E501
        """
        pass

    def test_delete_a_message(self):
        """Test case for delete_a_message

        Delete a message  # noqa: E501
        """
        pass

    def test_list_all_messages(self):
        """Test case for list_all_messages

        Get messages  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
