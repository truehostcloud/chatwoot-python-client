# chatwoot_client.AgentsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_agent_to_account**](AgentsApi.md#add_new_agent_to_account) | **POST** /api/v1/accounts/{account_id}/agents | Add a New Agent
[**delete_agent_from_account**](AgentsApi.md#delete_agent_from_account) | **DELETE** /api/v1/accounts/{account_id}/agents/{id} | Remove an Agent from Account
[**get_account_agents**](AgentsApi.md#get_account_agents) | **GET** /api/v1/accounts/{account_id}/agents | List Agents in Account
[**update_agent_in_account**](AgentsApi.md#update_agent_in_account) | **PATCH** /api/v1/accounts/{account_id}/agents/{id} | Update Agent in Account

# **add_new_agent_to_account**
> Agent add_new_agent_to_account(body, account_id)

Add a New Agent

Add a new Agent to Account

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
api_instance = chatwoot_client.AgentsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AccountIdAgentsBody() # AccountIdAgentsBody | 
account_id = 56 # int | The numeric ID of the account

try:
    # Add a New Agent
    api_response = api_instance.add_new_agent_to_account(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->add_new_agent_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountIdAgentsBody**](AccountIdAgentsBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**Agent**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_from_account**
> delete_agent_from_account(account_id, id)

Remove an Agent from Account

Remove an Agent from Account

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
api_instance = chatwoot_client.AgentsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agent to be deleted

try:
    # Remove an Agent from Account
    api_instance.delete_agent_from_account(account_id, id)
except ApiException as e:
    print("Exception when calling AgentsApi->delete_agent_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the agent to be deleted | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_agents**
> list[Agent] get_account_agents(account_id)

List Agents in Account

Get Details of Agents in an Account

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
api_instance = chatwoot_client.AgentsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List Agents in Account
    api_response = api_instance.get_account_agents(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->get_account_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_in_account**
> Agent update_agent_in_account(body, account_id, id)

Update Agent in Account

Update an Agent in Account

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
api_instance = chatwoot_client.AgentsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AgentsIdBody() # AgentsIdBody | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agent to be updated.

try:
    # Update Agent in Account
    api_response = api_instance.update_agent_in_account(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->update_agent_in_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentsIdBody**](AgentsIdBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the agent to be updated. | 

### Return type

[**Agent**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

