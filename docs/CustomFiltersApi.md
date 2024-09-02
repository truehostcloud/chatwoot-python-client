# chatwoot_client.CustomFiltersApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_custom_filter**](CustomFiltersApi.md#create_a_custom_filter) | **POST** /api/v1/accounts/{account_id}/custom_filters | Create a custom filter
[**delete_a_custom_filter**](CustomFiltersApi.md#delete_a_custom_filter) | **DELETE** /api/v1/accounts/{account_id}/custom_filters/{custom_filter_id} | Delete a custom filter
[**get_details_of_a_single_custom_filter**](CustomFiltersApi.md#get_details_of_a_single_custom_filter) | **GET** /api/v1/accounts/{account_id}/custom_filters/{custom_filter_id} | Get a custom filter details
[**list_all_filters**](CustomFiltersApi.md#list_all_filters) | **GET** /api/v1/accounts/{account_id}/custom_filters | List all custom filters
[**update_a_custom_filter**](CustomFiltersApi.md#update_a_custom_filter) | **PATCH** /api/v1/accounts/{account_id}/custom_filters/{custom_filter_id} | Update a custom filter

# **create_a_custom_filter**
> CustomFilter create_a_custom_filter(body, account_id, filter_type=filter_type)

Create a custom filter

Create a custom filter in the account

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
api_instance = chatwoot_client.CustomFiltersApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.CustomFilterCreateUpdatePayload() # CustomFilterCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
filter_type = 'filter_type_example' # str | The type of custom filter (optional)

try:
    # Create a custom filter
    api_response = api_instance.create_a_custom_filter(body, account_id, filter_type=filter_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFiltersApi->create_a_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomFilterCreateUpdatePayload**](CustomFilterCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **filter_type** | **str**| The type of custom filter | [optional] 

### Return type

[**CustomFilter**](CustomFilter.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_custom_filter**
> delete_a_custom_filter(account_id, custom_filter_id)

Delete a custom filter

Delete a custom filter from the account

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
api_instance = chatwoot_client.CustomFiltersApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
custom_filter_id = 56 # int | The numeric ID of the custom filter

try:
    # Delete a custom filter
    api_instance.delete_a_custom_filter(account_id, custom_filter_id)
except ApiException as e:
    print("Exception when calling CustomFiltersApi->delete_a_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **custom_filter_id** | **int**| The numeric ID of the custom filter | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_single_custom_filter**
> CustomFilter get_details_of_a_single_custom_filter(account_id, custom_filter_id)

Get a custom filter details

Get the details of a custom filter in the account

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
api_instance = chatwoot_client.CustomFiltersApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
custom_filter_id = 56 # int | The numeric ID of the custom filter

try:
    # Get a custom filter details
    api_response = api_instance.get_details_of_a_single_custom_filter(account_id, custom_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFiltersApi->get_details_of_a_single_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **custom_filter_id** | **int**| The numeric ID of the custom filter | 

### Return type

[**CustomFilter**](CustomFilter.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_filters**
> list[CustomFilter] list_all_filters(account_id, filter_type=filter_type)

List all custom filters

List all custom filters in a category of a user

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
api_instance = chatwoot_client.CustomFiltersApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
filter_type = 'filter_type_example' # str | The type of custom filter (optional)

try:
    # List all custom filters
    api_response = api_instance.list_all_filters(account_id, filter_type=filter_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFiltersApi->list_all_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **filter_type** | **str**| The type of custom filter | [optional] 

### Return type

[**list[CustomFilter]**](CustomFilter.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_custom_filter**
> CustomFilter update_a_custom_filter(body, account_id, custom_filter_id)

Update a custom filter

Update a custom filter's attributes

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
api_instance = chatwoot_client.CustomFiltersApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.CustomFilterCreateUpdatePayload() # CustomFilterCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
custom_filter_id = 56 # int | The numeric ID of the custom filter

try:
    # Update a custom filter
    api_response = api_instance.update_a_custom_filter(body, account_id, custom_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFiltersApi->update_a_custom_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomFilterCreateUpdatePayload**](CustomFilterCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **custom_filter_id** | **int**| The numeric ID of the custom filter | 

### Return type

[**CustomFilter**](CustomFilter.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

