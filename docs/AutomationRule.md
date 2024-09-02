# AutomationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** | Automation Rule event, on which we call the actions(conversation_created, conversation_updated, message_created) | [optional] 
**name** | **str** | The name of the rule | [optional] 
**description** | **str** | Description to give more context about the rule | [optional] 
**active** | **bool** | Enable/disable automation rule | [optional] 
**actions** | **list[object]** | Array of actions which we perform when condition matches | [optional] 
**conditions** | **list[object]** | Array of conditions on which conversation/message filter would work | [optional] 
**account_id** | **int** | Account Id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

