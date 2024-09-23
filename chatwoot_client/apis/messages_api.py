# coding: utf-8

"""
    Chatwoot

    This is the API documentation for Chatwoot server.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@chatwoot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from chatwoot_client.api_client import ApiClient


class MessagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_a_new_message_in_a_conversation(self, body, account_id, conversation_id, **kwargs):  # noqa: E501
        """Create New Message  # noqa: E501

        Create a new message in the conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_a_new_message_in_a_conversation(body, account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationMessageCreate body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_a_new_message_in_a_conversation_with_http_info(body, account_id, conversation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_a_new_message_in_a_conversation_with_http_info(body, account_id, conversation_id, **kwargs)  # noqa: E501
            return data

    def create_a_new_message_in_a_conversation_with_http_info(self, body, account_id, conversation_id, **kwargs):  # noqa: E501
        """Create New Message  # noqa: E501

        Create a new message in the conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_a_new_message_in_a_conversation_with_http_info(body, account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationMessageCreate body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'conversation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_a_new_message_in_a_conversation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_a_new_message_in_a_conversation`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_a_new_message_in_a_conversation`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params or
                params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `create_a_new_message_in_a_conversation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'conversation_id' in params:
            path_params['conversation_id'] = params['conversation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['agentBotApiKey', 'userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_a_message(self, account_id, conversation_id, message_id, **kwargs):  # noqa: E501
        """Delete a message  # noqa: E501

        Delete a message and it's attachments from the conversation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_a_message(account_id, conversation_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :param int message_id: The numeric ID of the message (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_a_message_with_http_info(account_id, conversation_id, message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_a_message_with_http_info(account_id, conversation_id, message_id, **kwargs)  # noqa: E501
            return data

    def delete_a_message_with_http_info(self, account_id, conversation_id, message_id, **kwargs):  # noqa: E501
        """Delete a message  # noqa: E501

        Delete a message and it's attachments from the conversation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_a_message_with_http_info(account_id, conversation_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :param int message_id: The numeric ID of the message (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'conversation_id', 'message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_a_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_a_message`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params or
                params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `delete_a_message`")  # noqa: E501
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `delete_a_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'conversation_id' in params:
            path_params['conversation_id'] = params['conversation_id']  # noqa: E501
        if 'message_id' in params:
            path_params['message_id'] = params['message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages/{message_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_all_messages(self, account_id, conversation_id, **kwargs):  # noqa: E501
        """Get messages  # noqa: E501

        List all messages of a conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_messages(account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: MessageList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_messages_with_http_info(account_id, conversation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_all_messages_with_http_info(account_id, conversation_id, **kwargs)  # noqa: E501
            return data

    def list_all_messages_with_http_info(self, account_id, conversation_id, **kwargs):  # noqa: E501
        """Get messages  # noqa: E501

        List all messages of a conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_messages_with_http_info(account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: MessageList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'conversation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_all_messages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_all_messages`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params or
                params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `list_all_messages`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'conversation_id' in params:
            path_params['conversation_id'] = params['conversation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
