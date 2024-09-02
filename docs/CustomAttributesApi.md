# chatwoot_client.CustomAttributesApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_custom_attribute_to_account**](CustomAttributesApi.md#add_new_custom_attribute_to_account) | **POST** /api/v1/accounts/{account_id}/custom_attribute_definitions | Add a new custom attribute
[**delete_custom_attribute_from_account**](CustomAttributesApi.md#delete_custom_attribute_from_account) | **DELETE** /api/v1/accounts/{account_id}/custom_attribute_definitions/{id} | Remove a custom attribute from account
[**get_account_custom_attribute**](CustomAttributesApi.md#get_account_custom_attribute) | **GET** /api/v1/accounts/{account_id}/custom_attribute_definitions | List all custom attributes in an account
[**get_details_of_a_single_custom_attribute**](CustomAttributesApi.md#get_details_of_a_single_custom_attribute) | **GET** /api/v1/accounts/{account_id}/custom_attribute_definitions/{id} | Get a custom attribute details
[**update_custom_attribute_in_account**](CustomAttributesApi.md#update_custom_attribute_in_account) | **PATCH** /api/v1/accounts/{account_id}/custom_attribute_definitions/{id} | Update custom attribute in Account

# **add_new_custom_attribute_to_account**
> CustomAttribute add_new_custom_attribute_to_account(body, account_id)

Add a new custom attribute

Add a new custom attribute to account

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
api_instance = chatwoot_client.CustomAttributesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.CustomAttributeCreateUpdatePayload() # CustomAttributeCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Add a new custom attribute
    api_response = api_instance.add_new_custom_attribute_to_account(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAttributesApi->add_new_custom_attribute_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomAttributeCreateUpdatePayload**](CustomAttributeCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**CustomAttribute**](CustomAttribute.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_attribute_from_account**
> delete_custom_attribute_from_account(account_id, id)

Remove a custom attribute from account

Remove a custom attribute from account

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
api_instance = chatwoot_client.CustomAttributesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the custom attribute to be deleted

try:
    # Remove a custom attribute from account
    api_instance.delete_custom_attribute_from_account(account_id, id)
except ApiException as e:
    print("Exception when calling CustomAttributesApi->delete_custom_attribute_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the custom attribute to be deleted | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_custom_attribute**
> list[CustomAttribute] get_account_custom_attribute(account_id, attribute_model)

List all custom attributes in an account

Get details of custom attributes in an Account

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
api_instance = chatwoot_client.CustomAttributesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
attribute_model = 'attribute_model_example' # str | conversation_attribute(0)/contact_attribute(1)

try:
    # List all custom attributes in an account
    api_response = api_instance.get_account_custom_attribute(account_id, attribute_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAttributesApi->get_account_custom_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **attribute_model** | **str**| conversation_attribute(0)/contact_attribute(1) | 

### Return type

[**list[CustomAttribute]**](CustomAttribute.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_single_custom_attribute**
> CustomAttribute get_details_of_a_single_custom_attribute(account_id, id)

Get a custom attribute details

Get the details of a custom attribute in the account

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
api_instance = chatwoot_client.CustomAttributesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the custom attribute to be updated.

try:
    # Get a custom attribute details
    api_response = api_instance.get_details_of_a_single_custom_attribute(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAttributesApi->get_details_of_a_single_custom_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the custom attribute to be updated. | 

### Return type

[**CustomAttribute**](CustomAttribute.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_attribute_in_account**
> CustomAttribute update_custom_attribute_in_account(body, account_id, id)

Update custom attribute in Account

Update a custom attribute in account

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
api_instance = chatwoot_client.CustomAttributesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.CustomAttributeCreateUpdatePayload() # CustomAttributeCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the custom attribute to be updated.

try:
    # Update custom attribute in Account
    api_response = api_instance.update_custom_attribute_in_account(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomAttributesApi->update_custom_attribute_in_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomAttributeCreateUpdatePayload**](CustomAttributeCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the custom attribute to be updated. | 

### Return type

[**CustomAttribute**](CustomAttribute.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

