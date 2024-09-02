# chatwoot_client.CannedResponseApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_canned_response_in_account**](CannedResponseApi.md#update_canned_response_in_account) | **PATCH** /api/v1/accounts/{account_id}/canned_responses/{id} | Update Canned Response in Account

# **update_canned_response_in_account**
> CannedResponse update_canned_response_in_account(body, account_id, id)

Update Canned Response in Account

Update a Canned Response in Account

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
api_instance = chatwoot_client.CannedResponseApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.CannedResponseCreateUpdatePayload() # CannedResponseCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the canned response to be updated.

try:
    # Update Canned Response in Account
    api_response = api_instance.update_canned_response_in_account(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CannedResponseApi->update_canned_response_in_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CannedResponseCreateUpdatePayload**](CannedResponseCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the canned response to be updated. | 

### Return type

[**CannedResponse**](CannedResponse.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

