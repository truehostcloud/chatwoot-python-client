# chatwoot_client.AccountAgentBotsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_account_agent_bot**](AccountAgentBotsApi.md#create_an_account_agent_bot) | **POST** /api/v1/accounts/{account_id}/agent_bots | Create an Agent Bot
[**delete_an_account_agent_bot**](AccountAgentBotsApi.md#delete_an_account_agent_bot) | **DELETE** /api/v1/accounts/{account_id}/agent_bots/{id} | Delete an AgentBot
[**get_details_of_a_single_account_agent_bot**](AccountAgentBotsApi.md#get_details_of_a_single_account_agent_bot) | **GET** /api/v1/accounts/{account_id}/agent_bots/{id} | Get an agent bot details
[**list_all_account_agent_bots**](AccountAgentBotsApi.md#list_all_account_agent_bots) | **GET** /api/v1/accounts/{account_id}/agent_bots | List all AgentBots
[**update_an_account_agent_bot**](AccountAgentBotsApi.md#update_an_account_agent_bot) | **PATCH** /api/v1/accounts/{account_id}/agent_bots/{id} | Update an agent bot

# **create_an_account_agent_bot**
> AgentBot create_an_account_agent_bot(body, account_id)

Create an Agent Bot

Create an agent bot in the account

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
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AgentBotCreateUpdatePayload() # AgentBotCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create an Agent Bot
    api_response = api_instance.create_an_account_agent_bot(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->create_an_account_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentBotCreateUpdatePayload**](AgentBotCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**AgentBot**](AgentBot.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_account_agent_bot**
> delete_an_account_agent_bot(account_id, id)

Delete an AgentBot

Delete an AgentBot from the account

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
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agentbot to be updated

try:
    # Delete an AgentBot
    api_instance.delete_an_account_agent_bot(account_id, id)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->delete_an_account_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the agentbot to be updated | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_single_account_agent_bot**
> AgentBot get_details_of_a_single_account_agent_bot(account_id, id)

Get an agent bot details

Get the details of an agent bot in the account

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
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agentbot to be updated

try:
    # Get an agent bot details
    api_response = api_instance.get_details_of_a_single_account_agent_bot(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->get_details_of_a_single_account_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the agentbot to be updated | 

### Return type

[**AgentBot**](AgentBot.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_account_agent_bots**
> list[AgentBot] list_all_account_agent_bots(account_id)

List all AgentBots

List all agent bots available for the current account

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
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all AgentBots
    api_response = api_instance.list_all_account_agent_bots(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->list_all_account_agent_bots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[AgentBot]**](AgentBot.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_account_agent_bot**
> AgentBot update_an_account_agent_bot(body, account_id, id)

Update an agent bot

Update an agent bot's attributes

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
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AgentBotCreateUpdatePayload() # AgentBotCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agentbot to be updated

try:
    # Update an agent bot
    api_response = api_instance.update_an_account_agent_bot(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->update_an_account_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentBotCreateUpdatePayload**](AgentBotCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the agentbot to be updated | 

### Return type

[**AgentBot**](AgentBot.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

