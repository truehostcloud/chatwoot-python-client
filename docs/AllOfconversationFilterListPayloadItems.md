# AllOfconversationFilterListPayloadItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID of the conversation | [optional] 
**messages** | [**list[Message]**](Message.md) |  | [optional] 
**account_id** | **float** | Account Id | [optional] 
**inbox_id** | **float** | ID of the inbox | [optional] 
**status** | **str** | The status of the conversation | [optional] 
**timestamp** | **str** | The time at which conversation was created | [optional] 
**contact_last_seen_at** | **str** |  | [optional] 
**agent_last_seen_at** | **str** |  | [optional] 
**last_activity_at** | **float** | The time at which the last activity happened in the conversation | [optional] 
**last_non_activity_message** | [**Message**](Message.md) |  | [optional] 
**unread_count** | **float** | The number of unread messages | [optional] 
**additional_attributes** | **object** | The object containing additional attributes related to the conversation | [optional] 
**custom_attributes** | **object** | The object to save custom attributes for conversation, accepts custom attributes key and value | [optional] 
**meta** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

