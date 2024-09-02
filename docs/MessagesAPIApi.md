# chatwoot_client.MessagesAPIApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_message**](MessagesAPIApi.md#create_a_message) | **POST** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages | Create a message
[**list_all_converation_messages**](MessagesAPIApi.md#list_all_converation_messages) | **GET** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages | List all messages
[**update_a_message**](MessagesAPIApi.md#update_a_message) | **PATCH** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages/{message_id} | Update a message

# **create_a_message**
> PublicMessage create_a_message(body, inbox_identifier, contact_identifier, conversation_id)

Create a message

Create a message

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.MessagesAPIApi()
body = chatwoot_client.PublicMessageCreatePayload() # PublicMessageCreatePayload | 
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel
contact_identifier = 'contact_identifier_example' # str | The source id of contact obtained on contact create
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Create a message
    api_response = api_instance.create_a_message(body, inbox_identifier, contact_identifier, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesAPIApi->create_a_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicMessageCreatePayload**](PublicMessageCreatePayload.md)|  | 
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 
 **contact_identifier** | **str**| The source id of contact obtained on contact create | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**PublicMessage**](PublicMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_converation_messages**
> list[PublicMessage] list_all_converation_messages(inbox_identifier, contact_identifier, conversation_id)

List all messages

List all messages in the conversation

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
api_instance = chatwoot_client.MessagesAPIApi(chatwoot_client.ApiClient(configuration))
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel
contact_identifier = 'contact_identifier_example' # str | The source id of contact obtained on contact create
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # List all messages
    api_response = api_instance.list_all_converation_messages(inbox_identifier, contact_identifier, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesAPIApi->list_all_converation_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 
 **contact_identifier** | **str**| The source id of contact obtained on contact create | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**list[PublicMessage]**](PublicMessage.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_message**
> PublicMessage update_a_message(body, inbox_identifier, contact_identifier, conversation_id, message_id)

Update a message

Update a message

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.MessagesAPIApi()
body = chatwoot_client.PublicMessageUpdatePayload() # PublicMessageUpdatePayload | 
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel
contact_identifier = 'contact_identifier_example' # str | The source id of contact obtained on contact create
conversation_id = 56 # int | The numeric ID of the conversation
message_id = 56 # int | The numeric ID of the message

try:
    # Update a message
    api_response = api_instance.update_a_message(body, inbox_identifier, contact_identifier, conversation_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesAPIApi->update_a_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicMessageUpdatePayload**](PublicMessageUpdatePayload.md)|  | 
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 
 **contact_identifier** | **str**| The source id of contact obtained on contact create | 
 **conversation_id** | **int**| The numeric ID of the conversation | 
 **message_id** | **int**| The numeric ID of the message | 

### Return type

[**PublicMessage**](PublicMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

