# chatwoot_client.WebhooksApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_webhook**](WebhooksApi.md#create_a_webhook) | **POST** /api/v1/accounts/{account_id}/webhooks | Add a webhook
[**delete_a_webhook**](WebhooksApi.md#delete_a_webhook) | **DELETE** /api/v1/accounts/{account_id}/webhooks/{webhook_id} | Delete a webhook
[**list_all_webhooks**](WebhooksApi.md#list_all_webhooks) | **GET** /api/v1/accounts/{account_id}/webhooks | List all webhooks
[**update_a_webhook**](WebhooksApi.md#update_a_webhook) | **PATCH** /api/v1/accounts/{account_id}/webhooks/{webhook_id} | Update a webhook object

# **create_a_webhook**
> Webhook create_a_webhook(body, account_id)

Add a webhook

Add a webhook subscription to the account

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.WebhooksApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.WebhookCreateUpdatePayload() # WebhookCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Add a webhook
    api_response = api_instance.create_a_webhook(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_a_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookCreateUpdatePayload**](WebhookCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_webhook**
> delete_a_webhook(account_id, webhook_id)

Delete a webhook

Delete a webhook from the account

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.WebhooksApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
webhook_id = 56 # int | The numeric ID of the webhook

try:
    # Delete a webhook
    api_instance.delete_a_webhook(account_id, webhook_id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_a_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **webhook_id** | **int**| The numeric ID of the webhook | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_webhooks**
> list[Webhook] list_all_webhooks(account_id)

List all webhooks

List all webhooks in the account

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.WebhooksApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all webhooks
    api_response = api_instance.list_all_webhooks(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_all_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[Webhook]**](Webhook.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_webhook**
> Webhook update_a_webhook(body, account_id, webhook_id)

Update a webhook object

Update a webhook object in the account

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.WebhooksApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.WebhookCreateUpdatePayload() # WebhookCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
webhook_id = 56 # int | The numeric ID of the webhook

try:
    # Update a webhook object
    api_response = api_instance.update_a_webhook(body, account_id, webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_a_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookCreateUpdatePayload**](WebhookCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **webhook_id** | **int**| The numeric ID of the webhook | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

