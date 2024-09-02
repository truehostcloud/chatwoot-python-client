# chatwoot_client.AccountUsersApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_account_user**](AccountUsersApi.md#create_an_account_user) | **POST** /platform/api/v1/accounts/{account_id}/account_users | Create an Account User
[**delete_an_account_user**](AccountUsersApi.md#delete_an_account_user) | **DELETE** /platform/api/v1/accounts/{account_id}/account_users | Delete an Account User
[**list_all_account_users**](AccountUsersApi.md#list_all_account_users) | **GET** /platform/api/v1/accounts/{account_id}/account_users | List all Account Users

# **create_an_account_user**
> InlineResponse200 create_an_account_user(body, account_id)

Create an Account User

Create an Account User

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AccountUsersApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdAccountUsersBody() # AccountIdAccountUsersBody | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create an Account User
    api_response = api_instance.create_an_account_user(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUsersApi->create_an_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdAccountUsersBody**](AccountIdAccountUsersBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_account_user**
> delete_an_account_user(body, account_id)

Delete an Account User

Delete an Account User

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AccountUsersApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdAccountUsersBody1() # AccountIdAccountUsersBody1 | 
account_id = 56 # int | The numeric ID of the account

try:
    # Delete an Account User
    api_instance.delete_an_account_user(body, account_id)
except ApiException as e:
    print("Exception when calling AccountUsersApi->delete_an_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdAccountUsersBody1**](AccountIdAccountUsersBody1.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

void (empty response body)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_account_users**
> list[InlineResponse200] list_all_account_users(account_id)

List all Account Users

List all account users

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AccountUsersApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all Account Users
    api_response = api_instance.list_all_account_users(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountUsersApi->list_all_account_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

