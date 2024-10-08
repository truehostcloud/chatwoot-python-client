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


class ConversationsAPIApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_a_conversation(self, body, inbox_identifier, contact_identifier, **kwargs):  # noqa: E501
        """Create a conversation  # noqa: E501

        Create a conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_a_conversation(body, inbox_identifier, contact_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicConversationCreatePayload body: (required)
        :param str inbox_identifier: The identifier obtained from API inbox channel (required)
        :param str contact_identifier: The source id of contact obtained on contact create (required)
        :return: PublicConversation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_a_conversation_with_http_info(body, inbox_identifier, contact_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.create_a_conversation_with_http_info(body, inbox_identifier, contact_identifier, **kwargs)  # noqa: E501
            return data

    def create_a_conversation_with_http_info(self, body, inbox_identifier, contact_identifier, **kwargs):  # noqa: E501
        """Create a conversation  # noqa: E501

        Create a conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_a_conversation_with_http_info(body, inbox_identifier, contact_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PublicConversationCreatePayload body: (required)
        :param str inbox_identifier: The identifier obtained from API inbox channel (required)
        :param str contact_identifier: The source id of contact obtained on contact create (required)
        :return: PublicConversation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'inbox_identifier', 'contact_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_a_conversation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_a_conversation`")  # noqa: E501
        # verify the required parameter 'inbox_identifier' is set
        if ('inbox_identifier' not in params or
                params['inbox_identifier'] is None):
            raise ValueError("Missing the required parameter `inbox_identifier` when calling `create_a_conversation`")  # noqa: E501
        # verify the required parameter 'contact_identifier' is set
        if ('contact_identifier' not in params or
                params['contact_identifier'] is None):
            raise ValueError("Missing the required parameter `contact_identifier` when calling `create_a_conversation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inbox_identifier' in params:
            path_params['inbox_identifier'] = params['inbox_identifier']  # noqa: E501
        if 'contact_identifier' in params:
            path_params['contact_identifier'] = params['contact_identifier']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicConversation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_all_contact_conversations(self, inbox_identifier, contact_identifier, **kwargs):  # noqa: E501
        """List all conversations  # noqa: E501

        List all conversations for the contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_contact_conversations(inbox_identifier, contact_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inbox_identifier: The identifier obtained from API inbox channel (required)
        :param str contact_identifier: The source id of contact obtained on contact create (required)
        :return: list[PublicConversation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_contact_conversations_with_http_info(inbox_identifier, contact_identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.list_all_contact_conversations_with_http_info(inbox_identifier, contact_identifier, **kwargs)  # noqa: E501
            return data

    def list_all_contact_conversations_with_http_info(self, inbox_identifier, contact_identifier, **kwargs):  # noqa: E501
        """List all conversations  # noqa: E501

        List all conversations for the contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_contact_conversations_with_http_info(inbox_identifier, contact_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str inbox_identifier: The identifier obtained from API inbox channel (required)
        :param str contact_identifier: The source id of contact obtained on contact create (required)
        :return: list[PublicConversation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['inbox_identifier', 'contact_identifier']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_all_contact_conversations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'inbox_identifier' is set
        if ('inbox_identifier' not in params or
                params['inbox_identifier'] is None):
            raise ValueError("Missing the required parameter `inbox_identifier` when calling `list_all_contact_conversations`")  # noqa: E501
        # verify the required parameter 'contact_identifier' is set
        if ('contact_identifier' not in params or
                params['contact_identifier'] is None):
            raise ValueError("Missing the required parameter `contact_identifier` when calling `list_all_contact_conversations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'inbox_identifier' in params:
            path_params['inbox_identifier'] = params['inbox_identifier']  # noqa: E501
        if 'contact_identifier' in params:
            path_params['contact_identifier'] = params['contact_identifier']  # noqa: E501

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
            '/public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PublicConversation]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
