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


class WebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_a_webhook(self, body, account_id, **kwargs):  # noqa: E501
        """Add a webhook  # noqa: E501

        Add a webhook subscription to the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_a_webhook(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebhookCreateUpdatePayload body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: Webhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_a_webhook_with_http_info(body, account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_a_webhook_with_http_info(body, account_id, **kwargs)  # noqa: E501
            return data

    def create_a_webhook_with_http_info(self, body, account_id, **kwargs):  # noqa: E501
        """Add a webhook  # noqa: E501

        Add a webhook subscription to the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_a_webhook_with_http_info(body, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebhookCreateUpdatePayload body: (required)
        :param int account_id: The numeric ID of the account (required)
        :return: Webhook
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
                    " to method create_a_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_a_webhook`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `create_a_webhook`")  # noqa: E501

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
        auth_settings = ['userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/webhooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Webhook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_a_webhook(self, account_id, webhook_id, **kwargs):  # noqa: E501
        """Delete a webhook  # noqa: E501

        Delete a webhook from the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_a_webhook(account_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int webhook_id: The numeric ID of the webhook (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_a_webhook_with_http_info(account_id, webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_a_webhook_with_http_info(account_id, webhook_id, **kwargs)  # noqa: E501
            return data

    def delete_a_webhook_with_http_info(self, account_id, webhook_id, **kwargs):  # noqa: E501
        """Delete a webhook  # noqa: E501

        Delete a webhook from the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_a_webhook_with_http_info(account_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :param int webhook_id: The numeric ID of the webhook (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'webhook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_a_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `delete_a_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params or
                params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `delete_a_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'webhook_id' in params:
            path_params['webhook_id'] = params['webhook_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/webhooks/{webhook_id}', 'DELETE',
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

    def list_all_webhooks(self, account_id, **kwargs):  # noqa: E501
        """List all webhooks  # noqa: E501

        List all webhooks in the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_webhooks(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :return: list[Webhook]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_all_webhooks_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_all_webhooks_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def list_all_webhooks_with_http_info(self, account_id, **kwargs):  # noqa: E501
        """List all webhooks  # noqa: E501

        List all webhooks in the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_webhooks_with_http_info(account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int account_id: The numeric ID of the account (required)
        :return: list[Webhook]
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
                    " to method list_all_webhooks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_all_webhooks`")  # noqa: E501

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
        auth_settings = ['userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/webhooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Webhook]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_a_webhook(self, body, account_id, webhook_id, **kwargs):  # noqa: E501
        """Update a webhook object  # noqa: E501

        Update a webhook object in the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_a_webhook(body, account_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebhookCreateUpdatePayload body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int webhook_id: The numeric ID of the webhook (required)
        :return: Webhook
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_a_webhook_with_http_info(body, account_id, webhook_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_a_webhook_with_http_info(body, account_id, webhook_id, **kwargs)  # noqa: E501
            return data

    def update_a_webhook_with_http_info(self, body, account_id, webhook_id, **kwargs):  # noqa: E501
        """Update a webhook object  # noqa: E501

        Update a webhook object in the account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_a_webhook_with_http_info(body, account_id, webhook_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebhookCreateUpdatePayload body: (required)
        :param int account_id: The numeric ID of the account (required)
        :param int webhook_id: The numeric ID of the webhook (required)
        :return: Webhook
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'webhook_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_a_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_a_webhook`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `update_a_webhook`")  # noqa: E501
        # verify the required parameter 'webhook_id' is set
        if ('webhook_id' not in params or
                params['webhook_id'] is None):
            raise ValueError("Missing the required parameter `webhook_id` when calling `update_a_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['account_id'] = params['account_id']  # noqa: E501
        if 'webhook_id' in params:
            path_params['webhook_id'] = params['webhook_id']  # noqa: E501

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
        auth_settings = ['userApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/accounts/{account_id}/webhooks/{webhook_id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Webhook',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
