# chatwoot_client.UsersApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_user**](UsersApi.md#create_a_user) | **POST** /platform/api/v1/users | Create a User
[**delete_a_user**](UsersApi.md#delete_a_user) | **DELETE** /platform/api/v1/users/{id} | Delete a User
[**get_details_of_a_user**](UsersApi.md#get_details_of_a_user) | **GET** /platform/api/v1/users/{id} | Get an user details
[**get_sso_url_of_a_user**](UsersApi.md#get_sso_url_of_a_user) | **GET** /platform/api/v1/users/{id}/login | Get User SSO Link
[**update_a_user**](UsersApi.md#update_a_user) | **PATCH** /platform/api/v1/users/{id} | Update a user

# **create_a_user**
> User create_a_user(body)

Create a User

Create a User

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
api_instance = chatwoot_client.UsersApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.UserCreateUpdatePayload() # UserCreateUpdatePayload | 

try:
    # Create a User
    api_response = api_instance.create_a_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_a_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateUpdatePayload**](UserCreateUpdatePayload.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_user**
> delete_a_user(id)

Delete a User

Delete a User

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
api_instance = chatwoot_client.UsersApi(chatwoot_client.ApiClient(configuration))
id = 56 # int | The numeric ID of the user on the platform

try:
    # Delete a User
    api_instance.delete_a_user(id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_a_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the user on the platform | 

### Return type

void (empty response body)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_details_of_a_user**
> User get_details_of_a_user(id)

Get an user details

Get the details of an user

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
api_instance = chatwoot_client.UsersApi(chatwoot_client.ApiClient(configuration))
id = 56 # int | The numeric ID of the user on the platform

try:
    # Get an user details
    api_response = api_instance.get_details_of_a_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_details_of_a_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the user on the platform | 

### Return type

[**User**](User.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sso_url_of_a_user**
> InlineResponse2001 get_sso_url_of_a_user(id)

Get User SSO Link

Get the sso link of a user

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
api_instance = chatwoot_client.UsersApi(chatwoot_client.ApiClient(configuration))
id = 56 # int | The numeric ID of the user on the platform

try:
    # Get User SSO Link
    api_response = api_instance.get_sso_url_of_a_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_sso_url_of_a_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the user on the platform | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_a_user**
> User update_a_user(body, id)

Update a user

Update a user's attributes

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
api_instance = chatwoot_client.UsersApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.UserCreateUpdatePayload() # UserCreateUpdatePayload | 
id = 56 # int | The numeric ID of the user on the platform

try:
    # Update a user
    api_response = api_instance.update_a_user(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_a_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateUpdatePayload**](UserCreateUpdatePayload.md)|  | 
 **id** | **int**| The numeric ID of the user on the platform | 

### Return type

[**User**](User.md)

### Authorization

[platformAppApiKey](../README.md#platformAppApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

