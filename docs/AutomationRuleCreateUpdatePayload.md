# AutomationRuleCreateUpdatePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Rule name | [optional] 
**description** | **str** | The description about the automation and actions | [optional] 
**event_name** | **str** | The event when you want to execute the automation actions | [optional] 
**active** | **bool** | Enable/disable automation rule | [optional] 
**actions** | **list[object]** | Array of actions which you want to perform when condition matches, e.g add label support if message contains content help. | [optional] 
**conditions** | **list[object]** | Array of conditions on which conversation filter would work, e.g message content contains text help. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

