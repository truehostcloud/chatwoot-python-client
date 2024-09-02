# chatwoot_client.ProfileApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_profile**](ProfileApi.md#fetch_profile) | **GET** /api/v1/profile | Fetch user profile

# **fetch_profile**
> User fetch_profile()

Fetch user profile

Get the user profile details

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
api_instance = chatwoot_client.ProfileApi(chatwoot_client.ApiClient(configuration))

try:
    # Fetch user profile
    api_response = api_instance.fetch_profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->fetch_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

