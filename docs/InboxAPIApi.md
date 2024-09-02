# chatwoot_client.InboxAPIApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_details_of_a_inbox**](InboxAPIApi.md#get_details_of_a_inbox) | **GET** /public/api/v1/inboxes/{inbox_identifier} | Inbox details

# **get_details_of_a_inbox**
> PublicInbox get_details_of_a_inbox(inbox_identifier)

Inbox details

Get the details of an inbox

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.InboxAPIApi()
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel

try:
    # Inbox details
    api_response = api_instance.get_details_of_a_inbox(inbox_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxAPIApi->get_details_of_a_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 

### Return type

[**PublicInbox**](PublicInbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

