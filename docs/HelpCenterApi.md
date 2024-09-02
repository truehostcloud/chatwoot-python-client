# chatwoot_client.HelpCenterApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_new_article_to_account**](HelpCenterApi.md#add_new_article_to_account) | **POST** /api/v1/accounts/{account_id}/portals/{portal_id}/articles | Add a new article
[**add_new_category_to_account**](HelpCenterApi.md#add_new_category_to_account) | **POST** /api/v1/accounts/{account_id}/portals/{portal_id}/categories | Add a new category
[**add_new_portal_to_account**](HelpCenterApi.md#add_new_portal_to_account) | **POST** /api/v1/accounts/{account_id}/portals | Add a new portal
[**get_portal**](HelpCenterApi.md#get_portal) | **GET** /api/v1/accounts/{account_id}/portals | List all portals in an account
[**update_new_portal_to_account**](HelpCenterApi.md#update_new_portal_to_account) | **PATCH** /api/v1/accounts/{account_id}/portals | update a new portal

# **add_new_article_to_account**
> Article add_new_article_to_account(body, account_id, portal_id)

Add a new article

Add a new article to portal

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
api_instance = chatwoot_client.HelpCenterApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.ArticleCreateUpdatePayload() # ArticleCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
portal_id = 56 # int | The numeric ID of the portal

try:
    # Add a new article
    api_response = api_instance.add_new_article_to_account(body, account_id, portal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelpCenterApi->add_new_article_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArticleCreateUpdatePayload**](ArticleCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **portal_id** | **int**| The numeric ID of the portal | 

### Return type

[**Article**](Article.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_category_to_account**
> Category add_new_category_to_account(body, account_id, portal_id)

Add a new category

Add a new category to portal

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
api_instance = chatwoot_client.HelpCenterApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.CategoryCreateUpdatePayload() # CategoryCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
portal_id = 56 # int | The numeric ID of the portal

try:
    # Add a new category
    api_response = api_instance.add_new_category_to_account(body, account_id, portal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelpCenterApi->add_new_category_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryCreateUpdatePayload**](CategoryCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 
 **portal_id** | **int**| The numeric ID of the portal | 

### Return type

[**Category**](Category.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_portal_to_account**
> Portal add_new_portal_to_account(body, account_id)

Add a new portal

Add a new portal to account

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
api_instance = chatwoot_client.HelpCenterApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.PortalCreateUpdatePayload() # PortalCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Add a new portal
    api_response = api_instance.add_new_portal_to_account(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelpCenterApi->add_new_portal_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalCreateUpdatePayload**](PortalCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**Portal**](Portal.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal**
> list[Portal] get_portal(account_id)

List all portals in an account

Get details of portals in an Account

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
api_instance = chatwoot_client.HelpCenterApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all portals in an account
    api_response = api_instance.get_portal(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelpCenterApi->get_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**list[Portal]**](Portal.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_new_portal_to_account**
> Portal update_new_portal_to_account(body, account_id)

update a new portal

update a new portal to account

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
api_instance = chatwoot_client.HelpCenterApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.PortalCreateUpdatePayload() # PortalCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # update a new portal
    api_response = api_instance.update_new_portal_to_account(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HelpCenterApi->update_new_portal_to_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalCreateUpdatePayload**](PortalCreateUpdatePayload.md)|  | 
 **account_id** | **int**| The numeric ID of the account | 

### Return type

[**Portal**](Portal.md)

### Authorization

[userApiKey](../README.md#userApiKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

