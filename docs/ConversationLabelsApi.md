# chatwoot_client.ConversationLabelsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_add_labels**](ConversationLabelsApi.md#conversation_add_labels) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/labels | Add Labels
[**list_all_labels_of_a_conversation**](ConversationLabelsApi.md#list_all_labels_of_a_conversation) | **GET** /api/v1/accounts/{account_id}/conversations/{conversation_id}/labels | List Labels

# **conversation_add_labels**
> ConversationLabels conversation_add_labels(body, account_id, conversation_id)

Add Labels

Add labels to a conversation. Note that this API would overwrite the existing list of labels associated to the conversation.

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
api_instance = chatwoot_client.ConversationLabelsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ConversationIdLabelsBody() # ConversationIdLabelsBody | 
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Add Labels
    api_response = api_instance.conversation_add_labels(body, account_id, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationLabelsApi->conversation_add_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConversationIdLabelsBody**](ConversationIdLabelsBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**ConversationLabels**](ConversationLabels.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_labels_of_a_conversation**
> ConversationLabels list_all_labels_of_a_conversation(account_id, conversation_id)

List Labels

Lists all the labels of a conversation

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
api_instance = chatwoot_client.ConversationLabelsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # List Labels
    api_response = api_instance.list_all_labels_of_a_conversation(account_id, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationLabelsApi->list_all_labels_of_a_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**ConversationLabels**](ConversationLabels.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

