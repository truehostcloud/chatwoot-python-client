# chatwoot_client.ReportsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_conversation_metrics**](ReportsApi.md#get_account_conversation_metrics) | **GET** /api/v2/accounts/{account_id}/reports/conversations | Account Conversation Metrics
[**get_agent_conversation_metrics**](ReportsApi.md#get_agent_conversation_metrics) | **GET** /api/v2/accounts/{account_id}/reports/conversations/ | Agent Conversation Metrics
[**list_all_conversation_statistics**](ReportsApi.md#list_all_conversation_statistics) | **GET** /api/v2/accounts/{account_id}/reports | Get Account reports
[**list_all_conversation_statistics_summary**](ReportsApi.md#list_all_conversation_statistics_summary) | **GET** /api/v2/accounts/{account_id}/reports/summary | Get Account reports summary

# **get_account_conversation_metrics**
> InlineResponse2007 get_account_conversation_metrics(account_id, type)

Account Conversation Metrics

Get conversation metrics for Account

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
api_instance = chatwoot_client.ReportsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
type = 'type_example' # str | Type of report

try:
    # Account Conversation Metrics
    api_response = api_instance.get_account_conversation_metrics(account_id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_account_conversation_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **type** | **str**| Type of report | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_conversation_metrics**
> list[AgentConversationMetrics] get_agent_conversation_metrics(account_id, type, user_id=user_id)

Agent Conversation Metrics

Get conversation metrics for Agent

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
api_instance = chatwoot_client.ReportsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
type = 'type_example' # str | Type of report
user_id = 'user_id_example' # str | The numeric ID of the user (optional)

try:
    # Agent Conversation Metrics
    api_response = api_instance.get_agent_conversation_metrics(account_id, type, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_agent_conversation_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **type** | **str**| Type of report | 
 **user_id** | **str**| The numeric ID of the user | [optional] 

### Return type

[**list[AgentConversationMetrics]**](AgentConversationMetrics.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_conversation_statistics**
> list[InlineResponse2006] list_all_conversation_statistics(account_id, metric, type, id=id, since=since, until=until)

Get Account reports

Get Account reports for a specific type, metric and date range

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
api_instance = chatwoot_client.ReportsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
metric = 'metric_example' # str | The type of metric
type = 'type_example' # str | Type of report
id = 'id_example' # str | The Id of specific object in case of agent/inbox/label (optional)
since = 'since_example' # str | The timestamp from where report should start. (optional)
until = 'until_example' # str | The timestamp from where report should stop. (optional)

try:
    # Get Account reports
    api_response = api_instance.list_all_conversation_statistics(account_id, metric, type, id=id, since=since, until=until)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->list_all_conversation_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **metric** | **str**| The type of metric | 
 **type** | **str**| Type of report | 
 **id** | **str**| The Id of specific object in case of agent/inbox/label | [optional] 
 **since** | **str**| The timestamp from where report should start. | [optional] 
 **until** | **str**| The timestamp from where report should stop. | [optional] 

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_conversation_statistics_summary**
> AccountSummary list_all_conversation_statistics_summary(account_id, type, id=id, since=since, until=until)

Get Account reports summary

Get Account reports summary for a specific type and date range

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
api_instance = chatwoot_client.ReportsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
type = 'type_example' # str | Type of report
id = 'id_example' # str | The Id of specific object in case of agent/inbox/label (optional)
since = 'since_example' # str | The timestamp from where report should start. (optional)
until = 'until_example' # str | The timestamp from where report should stop. (optional)

try:
    # Get Account reports summary
    api_response = api_instance.list_all_conversation_statistics_summary(account_id, type, id=id, since=since, until=until)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->list_all_conversation_statistics_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **type** | **str**| Type of report | 
 **id** | **str**| The Id of specific object in case of agent/inbox/label | [optional] 
 **since** | **str**| The timestamp from where report should start. | [optional] 
 **until** | **str**| The timestamp from where report should stop. | [optional] 

### Return type

[**AccountSummary**](AccountSummary.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

