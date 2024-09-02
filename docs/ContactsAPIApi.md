# chatwoot_client.ContactsAPIApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_contact**](ContactsAPIApi.md#create_a_contact) | **POST** /public/api/v1/inboxes/{inbox_identifier}/contacts | Create a contact
[**get_details_of_a_contact**](ContactsAPIApi.md#get_details_of_a_contact) | **GET** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier} | Get a contact
[**update_a_contact**](ContactsAPIApi.md#update_a_contact) | **PATCH** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier} | Update a contact

# **create_a_contact**
> PublicContact create_a_contact(body, inbox_identifier)

Create a contact

Create a contact

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.ContactsAPIApi()
body = chatwoot_client.PublicContactCreateUpdatePayload() # PublicContactCreateUpdatePayload | 
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel

try:
    # Create a contact
    api_response = api_instance.create_a_contact(body, inbox_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsAPIApi->create_a_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicContactCreateUpdatePayload**](PublicContactCreateUpdatePayload.md)|  | 
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 

### Return type

[**PublicContact**](PublicContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_contact**
> PublicContact get_details_of_a_contact(inbox_identifier, contact_identifier)

Get a contact

Get the details of a contact

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.ContactsAPIApi()
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel
contact_identifier = 'contact_identifier_example' # str | The source id of contact obtained on contact create

try:
    # Get a contact
    api_response = api_instance.get_details_of_a_contact(inbox_identifier, contact_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsAPIApi->get_details_of_a_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 
 **contact_identifier** | **str**| The source id of contact obtained on contact create | 

### Return type

[**PublicContact**](PublicContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_contact**
> PublicContact update_a_contact(body, inbox_identifier, contact_identifier)

Update a contact

Update a contact's attributes

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.ContactsAPIApi()
body = chatwoot_client.PublicContactCreateUpdatePayload() # PublicContactCreateUpdatePayload | 
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel
contact_identifier = 'contact_identifier_example' # str | The source id of contact obtained on contact create

try:
    # Update a contact
    api_response = api_instance.update_a_contact(body, inbox_identifier, contact_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsAPIApi->update_a_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicContactCreateUpdatePayload**](PublicContactCreateUpdatePayload.md)|  | 
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 
 **contact_identifier** | **str**| The source id of contact obtained on contact create | 

### Return type

[**PublicContact**](PublicContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

