# chatwoot_client.MessagesApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_new_message_in_a_conversation**](MessagesApi.md#create_a_new_message_in_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages | Create New Message
[**delete_a_message**](MessagesApi.md#delete_a_message) | **DELETE** /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages/{message_id} | Delete a message
[**list_all_messages**](MessagesApi.md#list_all_messages) | **GET** /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages | Get messages

# **create_a_new_message_in_a_conversation**
> InlineResponse2005 create_a_new_message_in_a_conversation(body, account_id, conversation_id)

Create New Message

Create a new message in the conversation

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: agentBotApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'
# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.MessagesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ConversationMessageCreate() # ConversationMessageCreate | 
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Create New Message
    api_response = api_instance.create_a_new_message_in_a_conversation(body, account_id, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->create_a_new_message_in_a_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConversationMessageCreate**](ConversationMessageCreate.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[agentBotApiKey](../README.md#agentBotApiKey), [userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_message**
> delete_a_message(account_id, conversation_id, message_id)

Delete a message

Delete a message and it's attachments from the conversation.

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
api_instance = chatwoot_client.MessagesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation
message_id = 56 # int | The numeric ID of the message

try:
    # Delete a message
    api_instance.delete_a_message(account_id, conversation_id, message_id)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_a_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 
 **message_id** | **int**| The numeric ID of the message | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_messages**
> MessageList list_all_messages(account_id, conversation_id)

Get messages

List all messages of a conversation

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
api_instance = chatwoot_client.MessagesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Get messages
    api_response = api_instance.list_all_messages(account_id, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->list_all_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**MessageList**](MessageList.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

