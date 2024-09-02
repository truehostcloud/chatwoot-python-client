# chatwoot_client.IntegrationsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_integration_hook**](IntegrationsApi.md#create_an_integration_hook) | **POST** /api/v1/accounts/{account_id}/integrations/hooks | Create an integration hook
[**delete_an_integration_hook**](IntegrationsApi.md#delete_an_integration_hook) | **DELETE** /api/v1/accounts/{account_id}/integrations/hooks/{hook_id} | Delete an Integration Hook
[**get_details_of_all_integrations**](IntegrationsApi.md#get_details_of_all_integrations) | **GET** /api/v1/accounts/{account_id}/integrations/apps | List all the Integrations
[**update_an_integrations_hook**](IntegrationsApi.md#update_an_integrations_hook) | **PATCH** /api/v1/accounts/{account_id}/integrations/hooks/{hook_id} | Update an Integration Hook

# **create_an_integration_hook**
> IntegrationsHook create_an_integration_hook(body, account_id)

Create an integration hook

Create an integration hook

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
api_instance = chatwoot_client.IntegrationsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.IntegrationsHookCreatePayload() # IntegrationsHookCreatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create an integration hook
    api_response = api_instance.create_an_integration_hook(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->create_an_integration_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationsHookCreatePayload**](IntegrationsHookCreatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**IntegrationsHook**](IntegrationsHook.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_integration_hook**
> delete_an_integration_hook(account_id, hook_id)

Delete an Integration Hook

Delete an Integration Hook

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
api_instance = chatwoot_client.IntegrationsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
hook_id = 56 # int | The numeric ID of the integration hook

try:
    # Delete an Integration Hook
    api_instance.delete_an_integration_hook(account_id, hook_id)
except ApiException as e:
    print("Exception when calling IntegrationsApi->delete_an_integration_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **hook_id** | **int**| The numeric ID of the integration hook | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_all_integrations**
> list[IntegrationsApp] get_details_of_all_integrations(account_id)

List all the Integrations

Get the details of all Integrations available for the account

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
api_instance = chatwoot_client.IntegrationsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all the Integrations
    api_response = api_instance.get_details_of_all_integrations(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->get_details_of_all_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[IntegrationsApp]**](IntegrationsApp.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_integrations_hook**
> IntegrationsHook update_an_integrations_hook(body, account_id, hook_id)

Update an Integration Hook

Update an Integration Hook

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
api_instance = chatwoot_client.IntegrationsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.IntegrationsHookUpdatePayload() # IntegrationsHookUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
hook_id = 56 # int | The numeric ID of the integration hook

try:
    # Update an Integration Hook
    api_response = api_instance.update_an_integrations_hook(body, account_id, hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->update_an_integrations_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntegrationsHookUpdatePayload**](IntegrationsHookUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **hook_id** | **int**| The numeric ID of the integration hook | 

### Return type

[**IntegrationsHook**](IntegrationsHook.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

