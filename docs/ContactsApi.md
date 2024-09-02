# chatwoot_client.ContactsApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contact_conversations**](ContactsApi.md#contact_conversations) | **GET** /api/v1/accounts/{account_id}/contacts/{id}/conversations | Contact Conversations
[**contact_create**](ContactsApi.md#contact_create) | **POST** /api/v1/accounts/{account_id}/contacts | Create Contact
[**contact_delete**](ContactsApi.md#contact_delete) | **DELETE** /api/v1/accounts/{account_id}/contacts/{id} | Delete Contact
[**contact_details**](ContactsApi.md#contact_details) | **GET** /api/v1/accounts/{account_id}/contacts/{id} | Show Contact
[**contact_filter**](ContactsApi.md#contact_filter) | **POST** /api/v1/accounts/{account_id}/contacts/filter | Contact Filter
[**contact_list**](ContactsApi.md#contact_list) | **GET** /api/v1/accounts/{account_id}/contacts | List Contacts
[**contact_search**](ContactsApi.md#contact_search) | **GET** /api/v1/accounts/{account_id}/contacts/search | Search Contacts
[**contact_update**](ContactsApi.md#contact_update) | **PUT** /api/v1/accounts/{account_id}/contacts/{id} | Update Contact

# **contact_conversations**
> ContactConversations contact_conversations(account_id, id)

Contact Conversations

Get conversations associated to that contact

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 1.2 # float | ID of the contact

try:
    # Contact Conversations
    api_response = api_instance.contact_conversations(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **float**| ID of the contact | 

### Return type

[**ContactConversations**](ContactConversations.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_create**
> ExtendedContact contact_create(body, account_id)

Create Contact

Create a new Contact

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ContactCreate() # ContactCreate | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create Contact
    api_response = api_instance.contact_create(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactCreate**](ContactCreate.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**ExtendedContact**](ExtendedContact.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_delete**
> contact_delete(account_id, id)

Delete Contact

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 1.2 # float | ID of the contact

try:
    # Delete Contact
    api_instance.contact_delete(account_id, id)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **float**| ID of the contact | 

### Return type

void (empty response body)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_details**
> ExtendedContact contact_details(account_id, id)

Show Contact

Get a contact belonging to the account using ID

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 1.2 # float | ID of the contact

try:
    # Show Contact
    api_response = api_instance.contact_details(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **float**| ID of the contact | 

### Return type

[**ExtendedContact**](ExtendedContact.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_filter**
> ContactList contact_filter(body, account_id, page=page)

Contact Filter

Filter contacts with custom filter options and pagination

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ContactsFilterBody() # ContactsFilterBody | 
account_id = 56 # int | The numeric ID of the account
page = 56 # int |  (optional)

try:
    # Contact Filter
    api_response = api_instance.contact_filter(body, account_id, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactsFilterBody**](ContactsFilterBody.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **page** | **int**|  | [optional] 

### Return type

[**ContactList**](ContactList.md)

### Authorization

[agentBotApiKey](../README.md#agentBotApiKey), [userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_list**
> ContactList contact_list(account_id, sort=sort, page=page)

List Contacts

Listing all the resolved contacts with pagination (Page size = 15) . Resolved contacts are the ones with a value for identifier, email or phone number

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
sort = 'sort_example' # str | The attribute by which list should be sorted (optional)
page = 1 # int | The page parameter (optional) (default to 1)

try:
    # List Contacts
    api_response = api_instance.contact_list(account_id, sort=sort, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **sort** | **str**| The attribute by which list should be sorted | [optional] 
 **page** | **int**| The page parameter | [optional] [default to 1]

### Return type

[**ContactList**](ContactList.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_search**
> InlineResponse2002 contact_search(account_id, q=q, sort=sort, page=page)

Search Contacts

Search the resolved contacts using a search key, currently supports email search (Page size = 15). Resolved contacts are the ones with a value for identifier, email or phone number

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
q = 'q_example' # str | Search using contact `name`, `identifier`, `email` or `phone number` (optional)
sort = 'sort_example' # str | The attribute by which list should be sorted (optional)
page = 1 # int | The page parameter (optional) (default to 1)

try:
    # Search Contacts
    api_response = api_instance.contact_search(account_id, q=q, sort=sort, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 
 **q** | **str**| Search using contact &#x60;name&#x60;, &#x60;identifier&#x60;, &#x60;email&#x60; or &#x60;phone number&#x60; | [optional] 
 **sort** | **str**| The attribute by which list should be sorted | [optional] 
 **page** | **int**| The page parameter | [optional] [default to 1]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contact_update**
> ContactBase contact_update(body, account_id, id)

Update Contact

Update a contact belonging to the account using ID

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
api_instance = chatwoot_client.ContactsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ContactUpdate() # ContactUpdate | 
account_id = 56 # int | The numeric ID of the account
id = 1.2 # float | ID of the contact

try:
    # Update Contact
    api_response = api_instance.contact_update(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->contact_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ContactUpdate**](ContactUpdate.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **id** | **float**| ID of the contact | 

### Return type

[**ContactBase**](ContactBase.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

