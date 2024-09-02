# chatwoot_client.TeamsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_agent_to_team**](TeamsApi.md#add_new_agent_to_team) | **POST** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | Add a New Agent
[**create_a_team**](TeamsApi.md#create_a_team) | **POST** /api/v1/accounts/{account_id}/teams | Create a team
[**delete_a_team**](TeamsApi.md#delete_a_team) | **DELETE** /api/v1/accounts/{account_id}/teams/{team_id} | Delete a team
[**delete_agent_in_team**](TeamsApi.md#delete_agent_in_team) | **DELETE** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | Remove an Agent from Team
[**get_details_of_a_single_team**](TeamsApi.md#get_details_of_a_single_team) | **GET** /api/v1/accounts/{account_id}/teams/{team_id} | Get a team details
[**get_team_members**](TeamsApi.md#get_team_members) | **GET** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | List Agents in Team
[**list_all_teams**](TeamsApi.md#list_all_teams) | **GET** /api/v1/accounts/{account_id}/teams | List all teams
[**update_a_team**](TeamsApi.md#update_a_team) | **PATCH** /api/v1/accounts/{account_id}/teams/{team_id} | Update a team
[**update_agents_in_team**](TeamsApi.md#update_agents_in_team) | **PATCH** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | Update Agents in Team

# **add_new_agent_to_team**
> list[Agent] add_new_agent_to_team(body, account_id, team_id)

Add a New Agent

Add a new Agent to Team

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.TeamIdTeamMembersBody() # TeamIdTeamMembersBody | 
account_id = 56 # int | The numeric ID of the account
team_id = 56 # int | The ID of the team to be updated

try:
    # Add a New Agent
    api_response = api_instance.add_new_agent_to_team(body, account_id, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->add_new_agent_to_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamIdTeamMembersBody**](TeamIdTeamMembersBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **team_id** | **int**| The ID of the team to be updated | 

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_a_team**
> Team create_a_team(body, account_id)

Create a team

Create a team in the account

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.TeamCreateUpdatePayload() # TeamCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create a team
    api_response = api_instance.create_a_team(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_a_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamCreateUpdatePayload**](TeamCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**Team**](Team.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_team**
> delete_a_team(account_id, team_id)

Delete a team

Delete a team from the account

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
team_id = 56 # int | The ID of the team to be updated

try:
    # Delete a team
    api_instance.delete_a_team(account_id, team_id)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_a_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **team_id** | **int**| The ID of the team to be updated | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_in_team**
> delete_agent_in_team(body, account_id, team_id)

Remove an Agent from Team

Remove an Agent from Team

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.TeamIdTeamMembersBody1() # TeamIdTeamMembersBody1 | 
account_id = 56 # int | The numeric ID of the account
team_id = 56 # int | The ID of the team to be updated

try:
    # Remove an Agent from Team
    api_instance.delete_agent_in_team(body, account_id, team_id)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_agent_in_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamIdTeamMembersBody1**](TeamIdTeamMembersBody1.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **team_id** | **int**| The ID of the team to be updated | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_single_team**
> Team get_details_of_a_single_team(account_id, team_id)

Get a team details

Get the details of a team in the account

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
team_id = 56 # int | The ID of the team to be updated

try:
    # Get a team details
    api_response = api_instance.get_details_of_a_single_team(account_id, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_details_of_a_single_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **team_id** | **int**| The ID of the team to be updated | 

### Return type

[**Team**](Team.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_members**
> list[Agent] get_team_members(account_id, team_id)

List Agents in Team

Get Details of Agents in an Team

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
team_id = 56 # int | The ID of the team to be updated

try:
    # List Agents in Team
    api_response = api_instance.get_team_members(account_id, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **team_id** | **int**| The ID of the team to be updated | 

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_teams**
> list[Team] list_all_teams(account_id)

List all teams

List all teams available in the current account

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all teams
    api_response = api_instance.list_all_teams(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->list_all_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[Team]**](Team.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_team**
> Team update_a_team(body, account_id, team_id)

Update a team

Update a team's attributes

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.TeamCreateUpdatePayload() # TeamCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
team_id = 56 # int | The ID of the team to be updated

try:
    # Update a team
    api_response = api_instance.update_a_team(body, account_id, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_a_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamCreateUpdatePayload**](TeamCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **team_id** | **int**| The ID of the team to be updated | 

### Return type

[**Team**](Team.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agents_in_team**
> list[Agent] update_agents_in_team(body, account_id, team_id)

Update Agents in Team

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
api_instance = chatwoot_client.TeamsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.TeamIdTeamMembersBody2() # TeamIdTeamMembersBody2 | 
account_id = 56 # int | The numeric ID of the account
team_id = 56 # int | The ID of the team to be updated

try:
    # Update Agents in Team
    api_response = api_instance.update_agents_in_team(body, account_id, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_agents_in_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamIdTeamMembersBody2**](TeamIdTeamMembersBody2.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **team_id** | **int**| The ID of the team to be updated | 

### Return type

[**list[Agent]**](Agent.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

