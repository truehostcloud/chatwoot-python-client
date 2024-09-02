# chatwoot_client.ContactApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_inbox_creation**](ContactApi.md#contact_inbox_creation) | **POST** /api/v1/accounts/{account_id}/contacts/{id}/contact_inboxes | Create contact inbox
[**contactable_inboxes_get**](ContactApi.md#contactable_inboxes_get) | **GET** /api/v1/accounts/{account_id}/contacts/{id}/contactable_inboxes | Get Contactable Inboxes

# **contact_inbox_creation**
> ContactInboxes contact_inbox_creation(body, account_id, id)

Create contact inbox

Create a contact inbox record for an inbox

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
api_instance = chatwoot_client.ContactApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.IdContactInboxesBody() # IdContactInboxesBody | 
account_id = 56 # int | The numeric ID of the account
id = 1.2 # float | ID of the contact

try:
    # Create contact inbox
    api_response = api_instance.contact_inbox_creation(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contact_inbox_creation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdContactInboxesBody**](IdContactInboxesBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **float**| ID of the contact | 

### Return type

[**ContactInboxes**](ContactInboxes.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contactable_inboxes_get**
> ContactableInboxes contactable_inboxes_get(account_id, id)

Get Contactable Inboxes

Get List of contactable Inboxes

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
api_instance = chatwoot_client.ContactApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 1.2 # float | ID of the contact

try:
    # Get Contactable Inboxes
    api_response = api_instance.contactable_inboxes_get(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->contactable_inboxes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **float**| ID of the contact | 

### Return type

[**ContactableInboxes**](ContactableInboxes.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

