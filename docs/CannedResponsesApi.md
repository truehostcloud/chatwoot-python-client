# chatwoot_client.CannedResponsesApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_canned_response_to_account**](CannedResponsesApi.md#add_new_canned_response_to_account) | **POST** /api/v1/accounts/{account_id}/canned_responses | Add a New Canned Response
[**delete_canned_response_from_account**](CannedResponsesApi.md#delete_canned_response_from_account) | **DELETE** /api/v1/accounts/{account_id}/canned_responses/{id} | Remove a Canned Response from Account
[**get_account_canned_response**](CannedResponsesApi.md#get_account_canned_response) | **GET** /api/v1/accounts/{account_id}/canned_responses | List all Canned Responses in an Account

# **add_new_canned_response_to_account**
> CannedResponse add_new_canned_response_to_account(body, account_id)

Add a New Canned Response

Add a new Canned Response to Account

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
api_instance = chatwoot_client.CannedResponsesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.CannedResponseCreateUpdatePayload() # CannedResponseCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Add a New Canned Response
    api_response = api_instance.add_new_canned_response_to_account(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CannedResponsesApi->add_new_canned_response_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CannedResponseCreateUpdatePayload**](CannedResponseCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**CannedResponse**](CannedResponse.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_canned_response_from_account**
> delete_canned_response_from_account(account_id, id)

Remove a Canned Response from Account

Remove a Canned Response from Account

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
api_instance = chatwoot_client.CannedResponsesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the canned response to be deleted

try:
    # Remove a Canned Response from Account
    api_instance.delete_canned_response_from_account(account_id, id)
except ApiException as e:
    print("Exception when calling CannedResponsesApi->delete_canned_response_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the canned response to be deleted | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_canned_response**
> list[CannedResponse] get_account_canned_response(account_id)

List all Canned Responses in an Account

Get Details of Canned Responses in an Account

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
api_instance = chatwoot_client.CannedResponsesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all Canned Responses in an Account
    api_response = api_instance.get_account_canned_response(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CannedResponsesApi->get_account_canned_response: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[CannedResponse]**](CannedResponse.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

