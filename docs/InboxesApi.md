# chatwoot_client.InboxesApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_agent_to_inbox**](InboxesApi.md#add_new_agent_to_inbox) | **POST** /api/v1/accounts/{account_id}/inbox_members | Add a New Agent
[**delete_agent_in_inbox**](InboxesApi.md#delete_agent_in_inbox) | **DELETE** /api/v1/accounts/{account_id}/inbox_members | Remove an Agent from Inbox
[**get_inbox**](InboxesApi.md#get_inbox) | **GET** /api/v1/accounts/{account_id}/inboxes/{id}/ | Get an inbox
[**get_inbox_agent_bot**](InboxesApi.md#get_inbox_agent_bot) | **GET** /api/v1/accounts/{account_id}/inboxes/{id}/agent_bot | Show Inbox Agent Bot
[**get_inbox_members**](InboxesApi.md#get_inbox_members) | **GET** /api/v1/accounts/{account_id}/inbox_members/{inbox_id} | List Agents in Inbox
[**inbox_creation**](InboxesApi.md#inbox_creation) | **POST** /api/v1/accounts/{account_id}/inboxes/ | Create an inbox
[**list_all_inboxes**](InboxesApi.md#list_all_inboxes) | **GET** /api/v1/accounts/{account_id}/inboxes | List all inboxes
[**update_agent_bot**](InboxesApi.md#update_agent_bot) | **POST** /api/v1/accounts/{account_id}/inboxes/{id}/set_agent_bot | Add or remove agent bot
[**update_agents_in_inbox**](InboxesApi.md#update_agents_in_inbox) | **PATCH** /api/v1/accounts/{account_id}/inbox_members | Update Agents in Inbox
[**update_inbox**](InboxesApi.md#update_inbox) | **PATCH** /api/v1/accounts/{account_id}/inboxes/{id} | Update Inbox

# **add_new_agent_to_inbox**
> list[Agent] add_new_agent_to_inbox(body, account_id)

Add a New Agent

Add a new Agent to Inbox

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdInboxMembersBody() # AccountIdInboxMembersBody | 
account_id = 56 # int | The numeric ID of the account

try:
    # Add a New Agent
    api_response = api_instance.add_new_agent_to_inbox(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->add_new_agent_to_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdInboxMembersBody**](AccountIdInboxMembersBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_in_inbox**
> delete_agent_in_inbox(body, account_id)

Remove an Agent from Inbox

Remove an Agent from Inbox

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdInboxMembersBody1() # AccountIdInboxMembersBody1 | 
account_id = 56 # int | The numeric ID of the account

try:
    # Remove an Agent from Inbox
    api_instance.delete_agent_in_inbox(body, account_id)
except ApiException as e:
    print("Exception when calling InboxesApi->delete_agent_in_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdInboxMembersBody1**](AccountIdInboxMembersBody1.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox**
> Inbox get_inbox(account_id, id)

Get an inbox

Get an inbox available in the current account

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | ID of the inbox

try:
    # Get an inbox
    api_response = api_instance.get_inbox(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->get_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| ID of the inbox | 

### Return type

[**Inbox**](Inbox.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_agent_bot**
> AgentBot get_inbox_agent_bot(account_id, id)

Show Inbox Agent Bot

See if an agent bot is associated to the Inbox

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | ID of the inbox

try:
    # Show Inbox Agent Bot
    api_response = api_instance.get_inbox_agent_bot(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->get_inbox_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| ID of the inbox | 

### Return type

[**AgentBot**](AgentBot.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbox_members**
> list[Agent] get_inbox_members(account_id, inbox_id)

List Agents in Inbox

Get Details of Agents in an Inbox

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
inbox_id = 56 # int | The ID of the Inbox

try:
    # List Agents in Inbox
    api_response = api_instance.get_inbox_members(account_id, inbox_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->get_inbox_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **inbox_id** | **int**| The ID of the Inbox | 

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inbox_creation**
> Inbox inbox_creation(body, account_id)

Create an inbox

You can create more than one website inbox in each account

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdInboxesBody() # AccountIdInboxesBody | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create an inbox
    api_response = api_instance.inbox_creation(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->inbox_creation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdInboxesBody**](AccountIdInboxesBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**Inbox**](Inbox.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_inboxes**
> list[Inbox] list_all_inboxes(account_id)

List all inboxes

List all inboxes available in the current account

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all inboxes
    api_response = api_instance.list_all_inboxes(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->list_all_inboxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[Inbox]**](Inbox.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_bot**
> update_agent_bot(body, account_id, id)

Add or remove agent bot

To add an agent bot pass agent_bot id, to remove agent bot from an inbox pass null

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.IdSetAgentBotBody() # IdSetAgentBotBody | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | ID of the inbox

try:
    # Add or remove agent bot
    api_instance.update_agent_bot(body, account_id, id)
except ApiException as e:
    print("Exception when calling InboxesApi->update_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdSetAgentBotBody**](IdSetAgentBotBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| ID of the inbox | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agents_in_inbox**
> list[Agent] update_agents_in_inbox(body, account_id)

Update Agents in Inbox

All agents except the one passed in params will be removed

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdInboxMembersBody2() # AccountIdInboxMembersBody2 | 
account_id = 56 # int | The numeric ID of the account

try:
    # Update Agents in Inbox
    api_response = api_instance.update_agents_in_inbox(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->update_agents_in_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdInboxMembersBody2**](AccountIdInboxMembersBody2.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbox**
> Inbox update_inbox(body, account_id, id)

Update Inbox

Add avatar and disable auto assignment for an inbox

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
api_instance = chatwoot_client.InboxesApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.InboxesIdBody() # InboxesIdBody | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | ID of the inbox

try:
    # Update Inbox
    api_response = api_instance.update_inbox(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxesApi->update_inbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InboxesIdBody**](InboxesIdBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| ID of the inbox | 

### Return type

[**Inbox**](Inbox.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

