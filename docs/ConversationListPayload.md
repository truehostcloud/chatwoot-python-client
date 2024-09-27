# ConversationListPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ConversationListPayloadMeta**](ConversationListPayloadMeta.md) |  | [optional] 
**id** | **int** | ID of the conversation | [optional] 
**messages** | [**list[Message]**](Message.md) |  | [optional] 
**account_id** | **int** | Account Id | [optional] 
**inbox_id** | **int** | ID of the inbox | [optional] 
**status** | **str** | The status of the conversation | [optional] 
**timestamp** | **int** | The time at which conversation was created | [optional] 
**created_at** | **int** | The time at which conversation was created | [optional] 
**first_reply_created_at** | **int** | The time at which the first reply was created by the agent | [optional] 
**contact_last_seen_at** | **int** | The time at which the contact was last seen | [optional] 
**agent_last_seen_at** | **int** | The time at which the agent was last seen | [optional] 
**last_activity_at** | **int** | The time at which the last activity happened in the conversation | [optional] 
**last_non_activity_message** | [**Message**](Message.md) |  | [optional] 
**unread_count** | **int** | The number of unread messages | [optional] 
**additional_attributes** | **object** | The object containing additional attributes related to the conversation | [optional] 
**custom_attributes** | **object** | The object to save custom attributes for conversation, accepts custom attributes key and value | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

