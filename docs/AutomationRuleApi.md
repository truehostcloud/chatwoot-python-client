# chatwoot_client.AutomationRuleApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_automation_rule_to_account**](AutomationRuleApi.md#add_new_automation_rule_to_account) | **POST** /api/v1/accounts/{account_id}/automation_rules | Add a new automation rule
[**delete_automation_rule_from_account**](AutomationRuleApi.md#delete_automation_rule_from_account) | **DELETE** /api/v1/accounts/{account_id}/automation_rules/{id} | Remove a automation rule from account
[**get_account_automation_rule**](AutomationRuleApi.md#get_account_automation_rule) | **GET** /api/v1/accounts/{account_id}/automation_rules | List all automation rules in an account
[**get_details_of_a_single_automation_rule**](AutomationRuleApi.md#get_details_of_a_single_automation_rule) | **GET** /api/v1/accounts/{account_id}/automation_rules/{id} | Get a automation rule details
[**update_automation_rule_in_account**](AutomationRuleApi.md#update_automation_rule_in_account) | **PATCH** /api/v1/accounts/{account_id}/automation_rules/{id} | Update automation rule in Account

# **add_new_automation_rule_to_account**
> AutomationRule add_new_automation_rule_to_account(body, account_id)

Add a new automation rule

Add a new automation rule to account

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
api_instance = chatwoot_client.AutomationRuleApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AutomationRuleCreateUpdatePayload() # AutomationRuleCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Add a new automation rule
    api_response = api_instance.add_new_automation_rule_to_account(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationRuleApi->add_new_automation_rule_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutomationRuleCreateUpdatePayload**](AutomationRuleCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**AutomationRule**](AutomationRule.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_automation_rule_from_account**
> delete_automation_rule_from_account(account_id, id)

Remove a automation rule from account

Remove a automation rule from account

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
api_instance = chatwoot_client.AutomationRuleApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the automation rule to be deleted

try:
    # Remove a automation rule from account
    api_instance.delete_automation_rule_from_account(account_id, id)
except ApiException as e:
    print("Exception when calling AutomationRuleApi->delete_automation_rule_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the automation rule to be deleted | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_automation_rule**
> list[AutomationRule] get_account_automation_rule(account_id, page=page)

List all automation rules in an account

Get details of automation rules in an Account

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
api_instance = chatwoot_client.AutomationRuleApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
page = 1 # int | The page parameter (optional) (default to 1)

try:
    # List all automation rules in an account
    api_response = api_instance.get_account_automation_rule(account_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationRuleApi->get_account_automation_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **page** | **int**| The page parameter | [optional] [default to 1]

### Return type

[**list[AutomationRule]**](AutomationRule.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_single_automation_rule**
> AutomationRule get_details_of_a_single_automation_rule(account_id, id)

Get a automation rule details

Get the details of a automation rule in the account

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
api_instance = chatwoot_client.AutomationRuleApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the automation rule to be updated.

try:
    # Get a automation rule details
    api_response = api_instance.get_details_of_a_single_automation_rule(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationRuleApi->get_details_of_a_single_automation_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the automation rule to be updated. | 

### Return type

[**AutomationRule**](AutomationRule.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_automation_rule_in_account**
> AutomationRule update_automation_rule_in_account(body, account_id, id)

Update automation rule in Account

Update a automation rule in account

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
api_instance = chatwoot_client.AutomationRuleApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AutomationRuleCreateUpdatePayload() # AutomationRuleCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the automation rule to be updated.

try:
    # Update automation rule in Account
    api_response = api_instance.update_automation_rule_in_account(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutomationRuleApi->update_automation_rule_in_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutomationRuleCreateUpdatePayload**](AutomationRuleCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **int**| The ID of the automation rule to be updated. | 

### Return type

[**AutomationRule**](AutomationRule.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

