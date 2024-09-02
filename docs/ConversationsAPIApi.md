# chatwoot_client.ConversationsAPIApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_conversation**](ConversationsAPIApi.md#create_a_conversation) | **POST** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations | Create a conversation
[**list_all_contact_conversations**](ConversationsAPIApi.md#list_all_contact_conversations) | **GET** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations | List all conversations

# **create_a_conversation**
> PublicConversation create_a_conversation(body, inbox_identifier, contact_identifier)

Create a conversation

Create a conversation

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.ConversationsAPIApi()
body = chatwoot_client.PublicConversationCreatePayload() # PublicConversationCreatePayload | 
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel
contact_identifier = 'contact_identifier_example' # str | The source id of contact obtained on contact create

try:
    # Create a conversation
    api_response = api_instance.create_a_conversation(body, inbox_identifier, contact_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsAPIApi->create_a_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicConversationCreatePayload**](PublicConversationCreatePayload.md)|  | 
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 
 **contact_identifier** | **str**| The source id of contact obtained on contact create | 

### Return type

[**PublicConversation**](PublicConversation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_contact_conversations**
> list[PublicConversation] list_all_contact_conversations(inbox_identifier, contact_identifier)

List all conversations

List all conversations for the contact

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
api_instance = chatwoot_client.ConversationsAPIApi(chatwoot_client.ApiClient(configuration))
inbox_identifier = 'inbox_identifier_example' # str | The identifier obtained from API inbox channel
contact_identifier = 'contact_identifier_example' # str | The source id of contact obtained on contact create

try:
    # List all conversations
    api_response = api_instance.list_all_contact_conversations(inbox_identifier, contact_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsAPIApi->list_all_contact_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbox_identifier** | **str**| The identifier obtained from API inbox channel | 
 **contact_identifier** | **str**| The source id of contact obtained on contact create | 

### Return type

[**list[PublicConversation]**](PublicConversation.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

