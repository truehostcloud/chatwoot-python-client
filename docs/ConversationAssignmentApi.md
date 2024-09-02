# chatwoot_client.ConversationAssignmentApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_a_conversation**](ConversationAssignmentApi.md#assign_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/assignments | Assign Conversation

# **assign_a_conversation**
> User assign_a_conversation(body, account_id, conversation_id)

Assign Conversation

Assign a conversation to an agent or a team

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
api_instance = chatwoot_client.ConversationAssignmentApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ConversationIdAssignmentsBody() # ConversationIdAssignmentsBody | 
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Assign Conversation
    api_response = api_instance.assign_a_conversation(body, account_id, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationAssignmentApi->assign_a_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConversationIdAssignmentsBody**](ConversationIdAssignmentsBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**User**](User.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

