# chatwoot_client.CSATSurveyPageApi

All URIs are relative to *https://app.chatwoot.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_csat_survey_page**](CSATSurveyPageApi.md#get_csat_survey_page) | **GET** /survey/responses/{conversation_uuid} | Get CSAT survey page

# **get_csat_survey_page**
> get_csat_survey_page(conversation_uuid)

Get CSAT survey page

You can redirect the client to this URL, instead of implementing the CSAT survey component yourself.

### Example
```python
from __future__ import print_function
import time
import chatwoot_client
from chatwoot_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = chatwoot_client.CSATSurveyPageApi()
conversation_uuid = 56 # int | The uuid of the conversation

try:
    # Get CSAT survey page
    api_instance.get_csat_survey_page(conversation_uuid)
except ApiException as e:
    print("Exception when calling CSATSurveyPageApi->get_csat_survey_page: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_uuid** | **int**| The uuid of the conversation | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

