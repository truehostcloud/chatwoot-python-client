# AccountIdConversationsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Conversation source id | 
**inbox_id** | **str** | Id of inbox in which the conversation is created &lt;br/&gt; Allowed Inbox Types: Website, Phone, Api, Email | 
**contact_id** | **str** | Contact Id for which conversation is created | [optional] 
**additional_attributes** | **object** | Lets you specify attributes like browser information | [optional] 
**custom_attributes** | **object** | The object to save custom attributes for conversation, accepts custom attributes key and value | [optional] 
**status** | **str** | Specify the conversation whether it&#x27;s pending, open, closed | [optional] 
**assignee_id** | **str** | Agent Id for assigning a conversation to an agent | [optional] 
**team_id** | **str** | Team Id for assigning a conversation to a team | [optional] 
**message** | [**Apiv1accountsaccountIdconversationsMessage**](Apiv1accountsaccountIdconversationsMessage.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

