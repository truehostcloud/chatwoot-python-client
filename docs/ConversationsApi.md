# chatwoot_client.ConversationsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_filter**](ConversationsApi.md#conversation_filter) | **POST** /api/v1/accounts/{account_id}/conversations/filter | Conversations Filter
[**conversation_list**](ConversationsApi.md#conversation_list) | **GET** /api/v1/accounts/{account_id}/conversations | Conversations List
[**conversation_list_meta**](ConversationsApi.md#conversation_list_meta) | **GET** /api/v1/accounts/{account_id}/conversations/meta | Get Conversation Counts
[**get_details_of_a_conversation**](ConversationsApi.md#get_details_of_a_conversation) | **GET** /api/v1/accounts/{account_id}/conversations/{conversation_id} | Conversation Details
[**new_conversation**](ConversationsApi.md#new_conversation) | **POST** /api/v1/accounts/{account_id}/conversations | Create New Conversation
[**toggle_priority_of_a_conversation**](ConversationsApi.md#toggle_priority_of_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_priority | Toggle Priority
[**toggle_status_of_a_conversation**](ConversationsApi.md#toggle_status_of_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status | Toggle Status

# **conversation_filter**
> ConversationList conversation_filter(body, account_id, page=page)

Conversations Filter

Filter conversations with custom filter options and pagination

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
api_instance = chatwoot_client.ConversationsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ConversationsFilterBody() # ConversationsFilterBody | 
account_id = 56 # int | The numeric ID of the account
page = 56 # int |  (optional)

try:
    # Conversations Filter
    api_response = api_instance.conversation_filter(body, account_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversation_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConversationsFilterBody**](ConversationsFilterBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **page** | **int**|  | [optional] 

### Return type

[**ConversationList**](ConversationList.md)

### Authorization

[agentBotApiKey](../README.md#agentBotApiKey), [userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversation_list**
> ConversationList conversation_list(account_id, assignee_type=assignee_type, status=status, q=q, inbox_id=inbox_id, team_id=team_id, labels=labels, page=page)

Conversations List

List all the conversations with pagination

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
api_instance = chatwoot_client.ConversationsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
assignee_type = 'all' # str | Filter conversations by assignee type. (optional) (default to all)
status = 'open' # str | Filter by conversation status. (optional) (default to open)
q = 'q_example' # str | Filters conversations with messages containing the search term (optional)
inbox_id = 56 # int |  (optional)
team_id = 56 # int |  (optional)
labels = ['labels_example'] # list[str] |  (optional)
page = 1 # int | paginate through conversations (optional) (default to 1)

try:
    # Conversations List
    api_response = api_instance.conversation_list(account_id, assignee_type=assignee_type, status=status, q=q, inbox_id=inbox_id, team_id=team_id, labels=labels, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversation_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **assignee_type** | **str**| Filter conversations by assignee type. | [optional] [default to all]
 **status** | **str**| Filter by conversation status. | [optional] [default to open]
 **q** | **str**| Filters conversations with messages containing the search term | [optional] 
 **inbox_id** | **int**|  | [optional] 
 **team_id** | **int**|  | [optional] 
 **labels** | [**list[str]**](str.md)|  | [optional] 
 **page** | **int**| paginate through conversations | [optional] [default to 1]

### Return type

[**ConversationList**](ConversationList.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversation_list_meta**
> InlineResponse2003 conversation_list_meta(account_id, status=status, q=q, inbox_id=inbox_id, team_id=team_id, labels=labels)

Get Conversation Counts

Get open, unassigned and all Conversation counts

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
api_instance = chatwoot_client.ConversationsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
status = 'open' # str | Filter by conversation status. (optional) (default to open)
q = 'q_example' # str | Filters conversations with messages containing the search term (optional)
inbox_id = 56 # int |  (optional)
team_id = 56 # int |  (optional)
labels = ['labels_example'] # list[str] |  (optional)

try:
    # Get Conversation Counts
    api_response = api_instance.conversation_list_meta(account_id, status=status, q=q, inbox_id=inbox_id, team_id=team_id, labels=labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->conversation_list_meta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **status** | **str**| Filter by conversation status. | [optional] [default to open]
 **q** | **str**| Filters conversations with messages containing the search term | [optional] 
 **inbox_id** | **int**|  | [optional] 
 **team_id** | **int**|  | [optional] 
 **labels** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_conversation**
> ConversationShow get_details_of_a_conversation(account_id, conversation_id)

Conversation Details

Get all details regarding a conversation with all messages in the conversation

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
api_instance = chatwoot_client.ConversationsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Conversation Details
    api_response = api_instance.get_details_of_a_conversation(account_id, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_details_of_a_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**ConversationShow**](ConversationShow.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_conversation**
> InlineResponse2004 new_conversation(body, account_id)

Create New Conversation

Creating a conversation in chatwoot requires a source id.    Learn more about source_id: https://github.com/chatwoot/chatwoot/wiki/Building-on-Top-of-Chatwoot:-Importing-Existing-Contacts-and-Creating-Conversations

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
api_instance = chatwoot_client.ConversationsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdConversationsBody() # AccountIdConversationsBody | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create New Conversation
    api_response = api_instance.new_conversation(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->new_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdConversationsBody**](AccountIdConversationsBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[agentBotApiKey](../README.md#agentBotApiKey), [userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_priority_of_a_conversation**
> toggle_priority_of_a_conversation(body, account_id, conversation_id)

Toggle Priority

Toggles the priority of conversation

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
api_instance = chatwoot_client.ConversationsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ConversationIdTogglePriorityBody() # ConversationIdTogglePriorityBody | 
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Toggle Priority
    api_instance.toggle_priority_of_a_conversation(body, account_id, conversation_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->toggle_priority_of_a_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConversationIdTogglePriorityBody**](ConversationIdTogglePriorityBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

void (empty response body)

### Authorization

[agentBotApiKey](../README.md#agentBotApiKey), [userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_status_of_a_conversation**
> ConversationStatusToggle toggle_status_of_a_conversation(body, account_id, conversation_id)

Toggle Status

Toggles the status of the conversation between open and resolved

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
api_instance = chatwoot_client.ConversationsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ConversationIdToggleStatusBody() # ConversationIdToggleStatusBody | 
account_id = 56 # int | The numeric ID of the account
conversation_id = 56 # int | The numeric ID of the conversation

try:
    # Toggle Status
    api_response = api_instance.toggle_status_of_a_conversation(body, account_id, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->toggle_status_of_a_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConversationIdToggleStatusBody**](ConversationIdToggleStatusBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **conversation_id** | **int**| The numeric ID of the conversation | 

### Return type

[**ConversationStatusToggle**](ConversationStatusToggle.md)

### Authorization

[agentBotApiKey](../README.md#agentBotApiKey), [userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

