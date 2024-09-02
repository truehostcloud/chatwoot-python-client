# chatwoot_client.AccountsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_account**](AccountsApi.md#create_an_account) | **POST** /platform/api/v1/accounts | Create an Account
[**delete_an_account**](AccountsApi.md#delete_an_account) | **DELETE** /platform/api/v1/accounts/{account_id} | Delete an Account
[**get_details_of_an_account**](AccountsApi.md#get_details_of_an_account) | **GET** /platform/api/v1/accounts/{account_id} | Get an account details
[**update_an_account**](AccountsApi.md#update_an_account) | **PATCH** /platform/api/v1/accounts/{account_id} | Update an account

# **create_an_account**
> PlatformAccount create_an_account(body)

Create an Account

Create an Account

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
api_instance = chatwoot_client.AccountsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountCreateUpdatePayload() # AccountCreateUpdatePayload | 

try:
    # Create an Account
    api_response = api_instance.create_an_account(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_an_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreateUpdatePayload**](AccountCreateUpdatePayload.md)|  | 

### Return type

[**PlatformAccount**](PlatformAccount.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_account**
> delete_an_account(account_id)

Delete an Account

Delete an Account

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
api_instance = chatwoot_client.AccountsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # Delete an Account
    api_instance.delete_an_account(account_id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_an_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

void (empty response body)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_an_account**
> PlatformAccount get_details_of_an_account(account_id)

Get an account details

Get the details of an account

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
api_instance = chatwoot_client.AccountsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # Get an account details
    api_response = api_instance.get_details_of_an_account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_details_of_an_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**PlatformAccount**](PlatformAccount.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_account**
> PlatformAccount update_an_account(body, account_id)

Update an account

Update an account's attributes

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
api_instance = chatwoot_client.AccountsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountCreateUpdatePayload() # AccountCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Update an account
    api_response = api_instance.update_an_account(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->update_an_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountCreateUpdatePayload**](AccountCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**PlatformAccount**](PlatformAccount.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

