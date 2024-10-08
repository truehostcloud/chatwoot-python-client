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


class ConversationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def conversation_filter(self, body, account_id, **kwargs):  # noqa: E501
        """Conversations Filter  # noqa: E501

        Filter conversations with custom filter options and pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.conversation_filter(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationsFilterBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int page:
        :return: ConversationFilterList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.conversation_filter_with_http_info(body, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.conversation_filter_with_http_info(body, account_id, **kwargs)  # noqa: E501
            return data

    def conversation_filter_with_http_info(self, body, account_id, **kwargs):  # noqa: E501
        """Conversations Filter  # noqa: E501

        Filter conversations with custom filter options and pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.conversation_filter_with_http_info(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationsFilterBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int page:
        :return: ConversationFilterList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversation_filter" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `conversation_filter`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `conversation_filter`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

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
            '/api/v1/accounts/{account_id}/conversations/filter', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConversationFilterList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def conversation_list(self, account_id, **kwargs):  # noqa: E501
        """Conversations List  # noqa: E501

        List all the conversations with pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.conversation_list(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param str assignee_type: Filter conversations by assignee type.
        :param str status: Filter by conversation status.
        :param str q: Filters conversations with messages containing the search term
        :param int inbox_id:
        :param int team_id:
        :param list[str] labels:
        :param int page: paginate through conversations
        :param str sort_by: The attribute by which list should be sorted
        :return: ConversationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.conversation_list_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.conversation_list_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def conversation_list_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Conversations List  # noqa: E501

        List all the conversations with pagination  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.conversation_list_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param str assignee_type: Filter conversations by assignee type.
        :param str status: Filter by conversation status.
        :param str q: Filters conversations with messages containing the search term
        :param int inbox_id:
        :param int team_id:
        :param list[str] labels:
        :param int page: paginate through conversations
        :param str sort_by: The attribute by which list should be sorted
        :return: ConversationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'assignee_type', 'status', 'q', 'inbox_id', 'team_id', 'labels', 'page', 'sort_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversation_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `conversation_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

        query_params = []
        if 'assignee_type' in params:
            query_params.append(('assignee_type', params['assignee_type']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'inbox_id' in params:
            query_params.append(('inbox_id', params['inbox_id']))  # noqa: E501
        if 'team_id' in params:
            query_params.append(('team_id', params['team_id']))  # noqa: E501
        if 'labels' in params:
            query_params.append(('labels', params['labels']))  # noqa: E501
            collection_formats['labels'] = 'csv'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501

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
            '/api/v1/accounts/{account_id}/conversations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConversationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def conversation_list_meta(self, account_id, **kwargs):  # noqa: E501
        """Get Conversation Counts  # noqa: E501

        Get open, unassigned and all Conversation counts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.conversation_list_meta(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param str status: Filter by conversation status.
        :param str q: Filters conversations with messages containing the search term
        :param int inbox_id:
        :param int team_id:
        :param list[str] labels:
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.conversation_list_meta_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.conversation_list_meta_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def conversation_list_meta_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """Get Conversation Counts  # noqa: E501

        Get open, unassigned and all Conversation counts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.conversation_list_meta_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param str status: Filter by conversation status.
        :param str q: Filters conversations with messages containing the search term
        :param int inbox_id:
        :param int team_id:
        :param list[str] labels:
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'status', 'q', 'inbox_id', 'team_id', 'labels']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method conversation_list_meta" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `conversation_list_meta`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

        query_params = []
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'inbox_id' in params:
            query_params.append(('inbox_id', params['inbox_id']))  # noqa: E501
        if 'team_id' in params:
            query_params.append(('team_id', params['team_id']))  # noqa: E501
        if 'labels' in params:
            query_params.append(('labels', params['labels']))  # noqa: E501
            collection_formats['labels'] = 'csv'  # noqa: E501

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
            '/api/v1/accounts/{account_id}/conversations/meta', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_details_of_a_conversation(self, account_id, conversation_id, **kwargs):  # noqa: E501
        """Conversation Details  # noqa: E501

        Get all details regarding a conversation with all messages in the conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details_of_a_conversation(account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: ConversationShow
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_details_of_a_conversation_with_http_info(account_id, conversation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_details_of_a_conversation_with_http_info(account_id, conversation_id, **kwargs)  # noqa: E501
            return data

    def get_details_of_a_conversation_with_http_info(self, account_id, conversation_id, **kwargs):  # noqa: E501
        """Conversation Details  # noqa: E501

        Get all details regarding a conversation with all messages in the conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_details_of_a_conversation_with_http_info(account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: ConversationShow
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
                    " to method get_details_of_a_conversation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `get_details_of_a_conversation`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params or
                params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `get_details_of_a_conversation`")  # noqa: E501

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
            '/api/v1/accounts/{account_id}/conversations/{conversation_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConversationShow',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def new_conversation(self, body, account_id, **kwargs):  # noqa: E501
        """Create New Conversation  # noqa: E501

        Creating a conversation in chatwoot requires a source id.    Learn more about source_id: https://github.com/chatwoot/chatwoot/wiki/Building-on-Top-of-Chatwoot:-Importing-Existing-Contacts-and-Creating-Conversations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_conversation(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountIdConversationsBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.new_conversation_with_http_info(body, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.new_conversation_with_http_info(body, account_id, **kwargs)  # noqa: E501
            return data

    def new_conversation_with_http_info(self, body, account_id, **kwargs):  # noqa: E501
        """Create New Conversation  # noqa: E501

        Creating a conversation in chatwoot requires a source id.    Learn more about source_id: https://github.com/chatwoot/chatwoot/wiki/Building-on-Top-of-Chatwoot:-Importing-Existing-Contacts-and-Creating-Conversations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.new_conversation_with_http_info(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountIdConversationsBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method new_conversation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `new_conversation`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `new_conversation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

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
            '/api/v1/accounts/{account_id}/conversations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def toggle_priority_of_a_conversation(self, body, account_id, conversation_id, **kwargs):  # noqa: E501
        """Toggle Priority  # noqa: E501

        Toggles the priority of conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_priority_of_a_conversation(body, account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationIdTogglePriorityBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.toggle_priority_of_a_conversation_with_http_info(body, account_id, conversation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.toggle_priority_of_a_conversation_with_http_info(body, account_id, conversation_id, **kwargs)  # noqa: E501
            return data

    def toggle_priority_of_a_conversation_with_http_info(self, body, account_id, conversation_id, **kwargs):  # noqa: E501
        """Toggle Priority  # noqa: E501

        Toggles the priority of conversation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_priority_of_a_conversation_with_http_info(body, account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationIdTogglePriorityBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: None
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
                    " to method toggle_priority_of_a_conversation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `toggle_priority_of_a_conversation`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `toggle_priority_of_a_conversation`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params or
                params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `toggle_priority_of_a_conversation`")  # noqa: E501

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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['agentBotApiKey', 'userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_priority', 'POST',
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

    def toggle_status_of_a_conversation(self, body, account_id, conversation_id, **kwargs):  # noqa: E501
        """Toggle Status  # noqa: E501

        Toggles the status of the conversation between open and resolved  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_status_of_a_conversation(body, account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationIdToggleStatusBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: ConversationStatusToggle
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.toggle_status_of_a_conversation_with_http_info(body, account_id, conversation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.toggle_status_of_a_conversation_with_http_info(body, account_id, conversation_id, **kwargs)  # noqa: E501
            return data

    def toggle_status_of_a_conversation_with_http_info(self, body, account_id, conversation_id, **kwargs):  # noqa: E501
        """Toggle Status  # noqa: E501

        Toggles the status of the conversation between open and resolved  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.toggle_status_of_a_conversation_with_http_info(body, account_id, conversation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConversationIdToggleStatusBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int conversation_id: The numeric ID of the conversation (required)
        :return: ConversationStatusToggle
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
                    " to method toggle_status_of_a_conversation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `toggle_status_of_a_conversation`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `toggle_status_of_a_conversation`")  # noqa: E501
        # verify the required parameter 'conversation_id' is set
        if ('conversation_id' not in params or
                params['conversation_id'] is None):
            raise ValueError("Missing the required parameter `conversation_id` when calling `toggle_status_of_a_conversation`")  # noqa: E501

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
            '/api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConversationStatusToggle',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
