# chatwoot_client.AgentBotsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_agent_bot**](AgentBotsApi.md#create_an_agent_bot) | **POST** /platform/api/v1/agent_bots | Create an Agent Bot
[**delete_an_agent_bot**](AgentBotsApi.md#delete_an_agent_bot) | **DELETE** /platform/api/v1/agent_bots/{id} | Delete an AgentBot
[**get_details_of_a_single_agent_bot**](AgentBotsApi.md#get_details_of_a_single_agent_bot) | **GET** /platform/api/v1/agent_bots/{id} | Get an agent bot details
[**list_all_agent_bots**](AgentBotsApi.md#list_all_agent_bots) | **GET** /platform/api/v1/agent_bots | List all AgentBots
[**update_an_agent_bot**](AgentBotsApi.md#update_an_agent_bot) | **PATCH** /platform/api/v1/agent_bots/{id} | Update an agent bot

# **create_an_agent_bot**
> AgentBot create_an_agent_bot(body)

Create an Agent Bot

Create an agent bot

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AgentBotsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AgentBotCreateUpdatePayload() # AgentBotCreateUpdatePayload | 

try:
    # Create an Agent Bot
    api_response = api_instance.create_an_agent_bot(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentBotsApi->create_an_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentBotCreateUpdatePayload**](AgentBotCreateUpdatePayload.md)|  | 

### Return type

[**AgentBot**](AgentBot.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_agent_bot**
> delete_an_agent_bot(id)

Delete an AgentBot

Delete an AgentBot

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AgentBotsApi(chatwoot_client.ApiClient(configuration))
id = 56 # int | The ID of the agentbot to be updated

try:
    # Delete an AgentBot
    api_instance.delete_an_agent_bot(id)
except ApiException as e:
    print("Exception when calling AgentBotsApi->delete_an_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the agentbot to be updated | 

### Return type

void (empty response body)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_single_agent_bot**
> AgentBot get_details_of_a_single_agent_bot(id)

Get an agent bot details

Get the details of an agent bot

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AgentBotsApi(chatwoot_client.ApiClient(configuration))
id = 56 # int | The ID of the agentbot to be updated

try:
    # Get an agent bot details
    api_response = api_instance.get_details_of_a_single_agent_bot(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentBotsApi->get_details_of_a_single_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the agentbot to be updated | 

### Return type

[**AgentBot**](AgentBot.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_agent_bots**
> list[AgentBot] list_all_agent_bots()

List all AgentBots

List all agent bots available

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AgentBotsApi(chatwoot_client.ApiClient(configuration))

try:
    # List all AgentBots
    api_response = api_instance.list_all_agent_bots()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentBotsApi->list_all_agent_bots: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AgentBot]**](AgentBot.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_agent_bot**
> AgentBot update_an_agent_bot(body, id)

Update an agent bot

Update an agent bot's attributes

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: platformAppApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AgentBotsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AgentBotCreateUpdatePayload() # AgentBotCreateUpdatePayload | 
id = 56 # int | The ID of the agentbot to be updated

try:
    # Update an agent bot
    api_response = api_instance.update_an_agent_bot(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentBotsApi->update_an_agent_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentBotCreateUpdatePayload**](AgentBotCreateUpdatePayload.md)|  | 
 **id** | **int**| The ID of the agentbot to be updated | 

### Return type

[**AgentBot**](AgentBot.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

