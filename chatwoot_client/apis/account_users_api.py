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


class AccountUsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_an_account_user(self, body, account_id, **kwargs):  # noqa: E501
        """Create an Account User  # noqa: E501

        Create an Account User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_an_account_user(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountIdAccountUsersBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_an_account_user_with_http_info(body, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_an_account_user_with_http_info(body, account_id, **kwargs)  # noqa: E501
            return data

    def create_an_account_user_with_http_info(self, body, account_id, **kwargs):  # noqa: E501
        """Create an Account User  # noqa: E501

        Create an Account User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_an_account_user_with_http_info(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountIdAccountUsersBody body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: InlineResponse200
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
                    " to method create_an_account_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_an_account_user`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_an_account_user`")  # noqa: E501

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
        auth_settings = ['platformAppApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/platform/api/v1/accounts/{account_id}/account_users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_an_account_user(self, body, account_id, **kwargs):  # noqa: E501
        """Delete an Account User  # noqa: E501

        Delete an Account User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_an_account_user(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountIdAccountUsersBody1 body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_an_account_user_with_http_info(body, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_an_account_user_with_http_info(body, account_id, **kwargs)  # noqa: E501
            return data

    def delete_an_account_user_with_http_info(self, body, account_id, **kwargs):  # noqa: E501
        """Delete an Account User  # noqa: E501

        Delete an Account User  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_an_account_user_with_http_info(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountIdAccountUsersBody1 body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: None
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
                    " to method delete_an_account_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_an_account_user`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_an_account_user`")  # noqa: E501

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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['platformAppApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/platform/api/v1/accounts/{account_id}/account_users', 'DELETE',
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

    def list_all_account_users(self, account_id, **kwargs):  # noqa: E501
        """List all Account Users  # noqa: E501

        List all account users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_account_users(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_account_users_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_all_account_users_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def list_all_account_users_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """List all Account Users  # noqa: E501

        List all account users  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_account_users_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :return: list[InlineResponse200]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_all_account_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_all_account_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['platformAppApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/platform/api/v1/accounts/{account_id}/account_users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse200]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
