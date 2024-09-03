# chatwoot-python-client
This is the API documentation for Chatwoot server.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0.5
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/truehostcloud/chatwoot-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/truehostcloud/chatwoot-python-client.git`)

Then import the package:
```python
import chatwoot_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import chatwoot_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AgentBotCreateUpdatePayload() # AgentBotCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account

try:
    # Create an Agent Bot
    api_response = api_instance.create_an_account_agent_bot(body, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->create_an_account_agent_bot: %s\n" % e)

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agentbot to be updated

try:
    # Delete an AgentBot
    api_instance.delete_an_account_agent_bot(account_id, id)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->delete_an_account_agent_bot: %s\n" % e)

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agentbot to be updated

try:
    # Get an agent bot details
    api_response = api_instance.get_details_of_a_single_account_agent_bot(account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->get_details_of_a_single_account_agent_bot: %s\n" % e)

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
account_id = 56 # int | The numeric ID of the account

try:
    # List all AgentBots
    api_response = api_instance.list_all_account_agent_bots(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->list_all_account_agent_bots: %s\n" % e)

# Configure API key authorization: userApiKey
configuration = chatwoot_client.Configuration()
configuration.api_key['api_access_token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_access_token'] = 'Bearer'

# create an instance of the API class
api_instance = chatwoot_client.AccountAgentBotsApi(chatwoot_client.ApiClient(configuration))
body = chatwoot_client.AgentBotCreateUpdatePayload() # AgentBotCreateUpdatePayload | 
account_id = 56 # int | The numeric ID of the account
id = 56 # int | The ID of the agentbot to be updated

try:
    # Update an agent bot
    api_response = api_instance.update_an_account_agent_bot(body, account_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountAgentBotsApi->update_an_account_agent_bot: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.chatwoot.com/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountAgentBotsApi* | [**create_an_account_agent_bot**](docs/AccountAgentBotsApi.md#create_an_account_agent_bot) | **POST** /api/v1/accounts/{account_id}/agent_bots | Create an Agent Bot
*AccountAgentBotsApi* | [**delete_an_account_agent_bot**](docs/AccountAgentBotsApi.md#delete_an_account_agent_bot) | **DELETE** /api/v1/accounts/{account_id}/agent_bots/{id} | Delete an AgentBot
*AccountAgentBotsApi* | [**get_details_of_a_single_account_agent_bot**](docs/AccountAgentBotsApi.md#get_details_of_a_single_account_agent_bot) | **GET** /api/v1/accounts/{account_id}/agent_bots/{id} | Get an agent bot details
*AccountAgentBotsApi* | [**list_all_account_agent_bots**](docs/AccountAgentBotsApi.md#list_all_account_agent_bots) | **GET** /api/v1/accounts/{account_id}/agent_bots | List all AgentBots
*AccountAgentBotsApi* | [**update_an_account_agent_bot**](docs/AccountAgentBotsApi.md#update_an_account_agent_bot) | **PATCH** /api/v1/accounts/{account_id}/agent_bots/{id} | Update an agent bot
*AccountUsersApi* | [**create_an_account_user**](docs/AccountUsersApi.md#create_an_account_user) | **POST** /platform/api/v1/accounts/{account_id}/account_users | Create an Account User
*AccountUsersApi* | [**delete_an_account_user**](docs/AccountUsersApi.md#delete_an_account_user) | **DELETE** /platform/api/v1/accounts/{account_id}/account_users | Delete an Account User
*AccountUsersApi* | [**list_all_account_users**](docs/AccountUsersApi.md#list_all_account_users) | **GET** /platform/api/v1/accounts/{account_id}/account_users | List all Account Users
*AccountsApi* | [**create_an_account**](docs/AccountsApi.md#create_an_account) | **POST** /platform/api/v1/accounts | Create an Account
*AccountsApi* | [**delete_an_account**](docs/AccountsApi.md#delete_an_account) | **DELETE** /platform/api/v1/accounts/{account_id} | Delete an Account
*AccountsApi* | [**get_details_of_an_account**](docs/AccountsApi.md#get_details_of_an_account) | **GET** /platform/api/v1/accounts/{account_id} | Get an account details
*AccountsApi* | [**update_an_account**](docs/AccountsApi.md#update_an_account) | **PATCH** /platform/api/v1/accounts/{account_id} | Update an account
*AgentBotsApi* | [**create_an_agent_bot**](docs/AgentBotsApi.md#create_an_agent_bot) | **POST** /platform/api/v1/agent_bots | Create an Agent Bot
*AgentBotsApi* | [**delete_an_agent_bot**](docs/AgentBotsApi.md#delete_an_agent_bot) | **DELETE** /platform/api/v1/agent_bots/{id} | Delete an AgentBot
*AgentBotsApi* | [**get_details_of_a_single_agent_bot**](docs/AgentBotsApi.md#get_details_of_a_single_agent_bot) | **GET** /platform/api/v1/agent_bots/{id} | Get an agent bot details
*AgentBotsApi* | [**list_all_agent_bots**](docs/AgentBotsApi.md#list_all_agent_bots) | **GET** /platform/api/v1/agent_bots | List all AgentBots
*AgentBotsApi* | [**update_an_agent_bot**](docs/AgentBotsApi.md#update_an_agent_bot) | **PATCH** /platform/api/v1/agent_bots/{id} | Update an agent bot
*AgentsApi* | [**add_new_agent_to_account**](docs/AgentsApi.md#add_new_agent_to_account) | **POST** /api/v1/accounts/{account_id}/agents | Add a New Agent
*AgentsApi* | [**delete_agent_from_account**](docs/AgentsApi.md#delete_agent_from_account) | **DELETE** /api/v1/accounts/{account_id}/agents/{id} | Remove an Agent from Account
*AgentsApi* | [**get_account_agents**](docs/AgentsApi.md#get_account_agents) | **GET** /api/v1/accounts/{account_id}/agents | List Agents in Account
*AgentsApi* | [**update_agent_in_account**](docs/AgentsApi.md#update_agent_in_account) | **PATCH** /api/v1/accounts/{account_id}/agents/{id} | Update Agent in Account
*AutomationRuleApi* | [**add_new_automation_rule_to_account**](docs/AutomationRuleApi.md#add_new_automation_rule_to_account) | **POST** /api/v1/accounts/{account_id}/automation_rules | Add a new automation rule
*AutomationRuleApi* | [**delete_automation_rule_from_account**](docs/AutomationRuleApi.md#delete_automation_rule_from_account) | **DELETE** /api/v1/accounts/{account_id}/automation_rules/{id} | Remove a automation rule from account
*AutomationRuleApi* | [**get_account_automation_rule**](docs/AutomationRuleApi.md#get_account_automation_rule) | **GET** /api/v1/accounts/{account_id}/automation_rules | List all automation rules in an account
*AutomationRuleApi* | [**get_details_of_a_single_automation_rule**](docs/AutomationRuleApi.md#get_details_of_a_single_automation_rule) | **GET** /api/v1/accounts/{account_id}/automation_rules/{id} | Get a automation rule details
*AutomationRuleApi* | [**update_automation_rule_in_account**](docs/AutomationRuleApi.md#update_automation_rule_in_account) | **PATCH** /api/v1/accounts/{account_id}/automation_rules/{id} | Update automation rule in Account
*CSATSurveyPageApi* | [**get_csat_survey_page**](docs/CSATSurveyPageApi.md#get_csat_survey_page) | **GET** /survey/responses/{conversation_uuid} | Get CSAT survey page
*CannedResponseApi* | [**update_canned_response_in_account**](docs/CannedResponseApi.md#update_canned_response_in_account) | **PATCH** /api/v1/accounts/{account_id}/canned_responses/{id} | Update Canned Response in Account
*CannedResponsesApi* | [**add_new_canned_response_to_account**](docs/CannedResponsesApi.md#add_new_canned_response_to_account) | **POST** /api/v1/accounts/{account_id}/canned_responses | Add a New Canned Response
*CannedResponsesApi* | [**delete_canned_response_from_account**](docs/CannedResponsesApi.md#delete_canned_response_from_account) | **DELETE** /api/v1/accounts/{account_id}/canned_responses/{id} | Remove a Canned Response from Account
*CannedResponsesApi* | [**get_account_canned_response**](docs/CannedResponsesApi.md#get_account_canned_response) | **GET** /api/v1/accounts/{account_id}/canned_responses | List all Canned Responses in an Account
*ContactApi* | [**contact_inbox_creation**](docs/ContactApi.md#contact_inbox_creation) | **POST** /api/v1/accounts/{account_id}/contacts/{id}/contact_inboxes | Create contact inbox
*ContactApi* | [**contactable_inboxes_get**](docs/ContactApi.md#contactable_inboxes_get) | **GET** /api/v1/accounts/{account_id}/contacts/{id}/contactable_inboxes | Get Contactable Inboxes
*ContactsApi* | [**contact_conversations**](docs/ContactsApi.md#contact_conversations) | **GET** /api/v1/accounts/{account_id}/contacts/{id}/conversations | Contact Conversations
*ContactsApi* | [**contact_create**](docs/ContactsApi.md#contact_create) | **POST** /api/v1/accounts/{account_id}/contacts | Create Contact
*ContactsApi* | [**contact_delete**](docs/ContactsApi.md#contact_delete) | **DELETE** /api/v1/accounts/{account_id}/contacts/{id} | Delete Contact
*ContactsApi* | [**contact_details**](docs/ContactsApi.md#contact_details) | **GET** /api/v1/accounts/{account_id}/contacts/{id} | Show Contact
*ContactsApi* | [**contact_filter**](docs/ContactsApi.md#contact_filter) | **POST** /api/v1/accounts/{account_id}/contacts/filter | Contact Filter
*ContactsApi* | [**contact_list**](docs/ContactsApi.md#contact_list) | **GET** /api/v1/accounts/{account_id}/contacts | List Contacts
*ContactsApi* | [**contact_search**](docs/ContactsApi.md#contact_search) | **GET** /api/v1/accounts/{account_id}/contacts/search | Search Contacts
*ContactsApi* | [**contact_update**](docs/ContactsApi.md#contact_update) | **PUT** /api/v1/accounts/{account_id}/contacts/{id} | Update Contact
*ContactsAPIApi* | [**create_a_contact**](docs/ContactsAPIApi.md#create_a_contact) | **POST** /public/api/v1/inboxes/{inbox_identifier}/contacts | Create a contact
*ContactsAPIApi* | [**get_details_of_a_contact**](docs/ContactsAPIApi.md#get_details_of_a_contact) | **GET** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier} | Get a contact
*ContactsAPIApi* | [**update_a_contact**](docs/ContactsAPIApi.md#update_a_contact) | **PATCH** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier} | Update a contact
*ConversationAssignmentApi* | [**assign_a_conversation**](docs/ConversationAssignmentApi.md#assign_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/assignments | Assign Conversation
*ConversationLabelsApi* | [**conversation_add_labels**](docs/ConversationLabelsApi.md#conversation_add_labels) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/labels | Add Labels
*ConversationLabelsApi* | [**list_all_labels_of_a_conversation**](docs/ConversationLabelsApi.md#list_all_labels_of_a_conversation) | **GET** /api/v1/accounts/{account_id}/conversations/{conversation_id}/labels | List Labels
*ConversationsApi* | [**conversation_filter**](docs/ConversationsApi.md#conversation_filter) | **POST** /api/v1/accounts/{account_id}/conversations/filter | Conversations Filter
*ConversationsApi* | [**conversation_list**](docs/ConversationsApi.md#conversation_list) | **GET** /api/v1/accounts/{account_id}/conversations | Conversations List
*ConversationsApi* | [**conversation_list_meta**](docs/ConversationsApi.md#conversation_list_meta) | **GET** /api/v1/accounts/{account_id}/conversations/meta | Get Conversation Counts
*ConversationsApi* | [**get_details_of_a_conversation**](docs/ConversationsApi.md#get_details_of_a_conversation) | **GET** /api/v1/accounts/{account_id}/conversations/{conversation_id} | Conversation Details
*ConversationsApi* | [**new_conversation**](docs/ConversationsApi.md#new_conversation) | **POST** /api/v1/accounts/{account_id}/conversations | Create New Conversation
*ConversationsApi* | [**toggle_priority_of_a_conversation**](docs/ConversationsApi.md#toggle_priority_of_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_priority | Toggle Priority
*ConversationsApi* | [**toggle_status_of_a_conversation**](docs/ConversationsApi.md#toggle_status_of_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/toggle_status | Toggle Status
*ConversationsAPIApi* | [**create_a_conversation**](docs/ConversationsAPIApi.md#create_a_conversation) | **POST** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations | Create a conversation
*ConversationsAPIApi* | [**list_all_contact_conversations**](docs/ConversationsAPIApi.md#list_all_contact_conversations) | **GET** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations | List all conversations
*CustomAttributesApi* | [**add_new_custom_attribute_to_account**](docs/CustomAttributesApi.md#add_new_custom_attribute_to_account) | **POST** /api/v1/accounts/{account_id}/custom_attribute_definitions | Add a new custom attribute
*CustomAttributesApi* | [**delete_custom_attribute_from_account**](docs/CustomAttributesApi.md#delete_custom_attribute_from_account) | **DELETE** /api/v1/accounts/{account_id}/custom_attribute_definitions/{id} | Remove a custom attribute from account
*CustomAttributesApi* | [**get_account_custom_attribute**](docs/CustomAttributesApi.md#get_account_custom_attribute) | **GET** /api/v1/accounts/{account_id}/custom_attribute_definitions | List all custom attributes in an account
*CustomAttributesApi* | [**get_details_of_a_single_custom_attribute**](docs/CustomAttributesApi.md#get_details_of_a_single_custom_attribute) | **GET** /api/v1/accounts/{account_id}/custom_attribute_definitions/{id} | Get a custom attribute details
*CustomAttributesApi* | [**update_custom_attribute_in_account**](docs/CustomAttributesApi.md#update_custom_attribute_in_account) | **PATCH** /api/v1/accounts/{account_id}/custom_attribute_definitions/{id} | Update custom attribute in Account
*CustomFiltersApi* | [**create_a_custom_filter**](docs/CustomFiltersApi.md#create_a_custom_filter) | **POST** /api/v1/accounts/{account_id}/custom_filters | Create a custom filter
*CustomFiltersApi* | [**delete_a_custom_filter**](docs/CustomFiltersApi.md#delete_a_custom_filter) | **DELETE** /api/v1/accounts/{account_id}/custom_filters/{custom_filter_id} | Delete a custom filter
*CustomFiltersApi* | [**get_details_of_a_single_custom_filter**](docs/CustomFiltersApi.md#get_details_of_a_single_custom_filter) | **GET** /api/v1/accounts/{account_id}/custom_filters/{custom_filter_id} | Get a custom filter details
*CustomFiltersApi* | [**list_all_filters**](docs/CustomFiltersApi.md#list_all_filters) | **GET** /api/v1/accounts/{account_id}/custom_filters | List all custom filters
*CustomFiltersApi* | [**update_a_custom_filter**](docs/CustomFiltersApi.md#update_a_custom_filter) | **PATCH** /api/v1/accounts/{account_id}/custom_filters/{custom_filter_id} | Update a custom filter
*HelpCenterApi* | [**add_new_article_to_account**](docs/HelpCenterApi.md#add_new_article_to_account) | **POST** /api/v1/accounts/{account_id}/portals/{portal_id}/articles | Add a new article
*HelpCenterApi* | [**add_new_category_to_account**](docs/HelpCenterApi.md#add_new_category_to_account) | **POST** /api/v1/accounts/{account_id}/portals/{portal_id}/categories | Add a new category
*HelpCenterApi* | [**add_new_portal_to_account**](docs/HelpCenterApi.md#add_new_portal_to_account) | **POST** /api/v1/accounts/{account_id}/portals | Add a new portal
*HelpCenterApi* | [**get_portal**](docs/HelpCenterApi.md#get_portal) | **GET** /api/v1/accounts/{account_id}/portals | List all portals in an account
*HelpCenterApi* | [**update_new_portal_to_account**](docs/HelpCenterApi.md#update_new_portal_to_account) | **PATCH** /api/v1/accounts/{account_id}/portals | update a new portal
*InboxAPIApi* | [**get_details_of_a_inbox**](docs/InboxAPIApi.md#get_details_of_a_inbox) | **GET** /public/api/v1/inboxes/{inbox_identifier} | Inbox details
*InboxesApi* | [**add_new_agent_to_inbox**](docs/InboxesApi.md#add_new_agent_to_inbox) | **POST** /api/v1/accounts/{account_id}/inbox_members | Add a New Agent
*InboxesApi* | [**delete_agent_in_inbox**](docs/InboxesApi.md#delete_agent_in_inbox) | **DELETE** /api/v1/accounts/{account_id}/inbox_members | Remove an Agent from Inbox
*InboxesApi* | [**get_inbox**](docs/InboxesApi.md#get_inbox) | **GET** /api/v1/accounts/{account_id}/inboxes/{id}/ | Get an inbox
*InboxesApi* | [**get_inbox_agent_bot**](docs/InboxesApi.md#get_inbox_agent_bot) | **GET** /api/v1/accounts/{account_id}/inboxes/{id}/agent_bot | Show Inbox Agent Bot
*InboxesApi* | [**get_inbox_members**](docs/InboxesApi.md#get_inbox_members) | **GET** /api/v1/accounts/{account_id}/inbox_members/{inbox_id} | List Agents in Inbox
*InboxesApi* | [**inbox_creation**](docs/InboxesApi.md#inbox_creation) | **POST** /api/v1/accounts/{account_id}/inboxes/ | Create an inbox
*InboxesApi* | [**list_all_inboxes**](docs/InboxesApi.md#list_all_inboxes) | **GET** /api/v1/accounts/{account_id}/inboxes | List all inboxes
*InboxesApi* | [**update_agent_bot**](docs/InboxesApi.md#update_agent_bot) | **POST** /api/v1/accounts/{account_id}/inboxes/{id}/set_agent_bot | Add or remove agent bot
*InboxesApi* | [**update_agents_in_inbox**](docs/InboxesApi.md#update_agents_in_inbox) | **PATCH** /api/v1/accounts/{account_id}/inbox_members | Update Agents in Inbox
*InboxesApi* | [**update_inbox**](docs/InboxesApi.md#update_inbox) | **PATCH** /api/v1/accounts/{account_id}/inboxes/{id} | Update Inbox
*IntegrationsApi* | [**create_an_integration_hook**](docs/IntegrationsApi.md#create_an_integration_hook) | **POST** /api/v1/accounts/{account_id}/integrations/hooks | Create an integration hook
*IntegrationsApi* | [**delete_an_integration_hook**](docs/IntegrationsApi.md#delete_an_integration_hook) | **DELETE** /api/v1/accounts/{account_id}/integrations/hooks/{hook_id} | Delete an Integration Hook
*IntegrationsApi* | [**get_details_of_all_integrations**](docs/IntegrationsApi.md#get_details_of_all_integrations) | **GET** /api/v1/accounts/{account_id}/integrations/apps | List all the Integrations
*IntegrationsApi* | [**update_an_integrations_hook**](docs/IntegrationsApi.md#update_an_integrations_hook) | **PATCH** /api/v1/accounts/{account_id}/integrations/hooks/{hook_id} | Update an Integration Hook
*MessagesApi* | [**create_a_new_message_in_a_conversation**](docs/MessagesApi.md#create_a_new_message_in_a_conversation) | **POST** /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages | Create New Message
*MessagesApi* | [**delete_a_message**](docs/MessagesApi.md#delete_a_message) | **DELETE** /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages/{message_id} | Delete a message
*MessagesApi* | [**list_all_messages**](docs/MessagesApi.md#list_all_messages) | **GET** /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages | Get messages
*MessagesAPIApi* | [**create_a_message**](docs/MessagesAPIApi.md#create_a_message) | **POST** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages | Create a message
*MessagesAPIApi* | [**list_all_converation_messages**](docs/MessagesAPIApi.md#list_all_converation_messages) | **GET** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages | List all messages
*MessagesAPIApi* | [**update_a_message**](docs/MessagesAPIApi.md#update_a_message) | **PATCH** /public/api/v1/inboxes/{inbox_identifier}/contacts/{contact_identifier}/conversations/{conversation_id}/messages/{message_id} | Update a message
*ProfileApi* | [**fetch_profile**](docs/ProfileApi.md#fetch_profile) | **GET** /api/v1/profile | Fetch user profile
*ReportsApi* | [**get_account_conversation_metrics**](docs/ReportsApi.md#get_account_conversation_metrics) | **GET** /api/v2/accounts/{account_id}/reports/conversations | Account Conversation Metrics
*ReportsApi* | [**get_agent_conversation_metrics**](docs/ReportsApi.md#get_agent_conversation_metrics) | **GET** /api/v2/accounts/{account_id}/reports/conversations/ | Agent Conversation Metrics
*ReportsApi* | [**list_all_conversation_statistics**](docs/ReportsApi.md#list_all_conversation_statistics) | **GET** /api/v2/accounts/{account_id}/reports | Get Account reports
*ReportsApi* | [**list_all_conversation_statistics_summary**](docs/ReportsApi.md#list_all_conversation_statistics_summary) | **GET** /api/v2/accounts/{account_id}/reports/summary | Get Account reports summary
*TeamsApi* | [**add_new_agent_to_team**](docs/TeamsApi.md#add_new_agent_to_team) | **POST** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | Add a New Agent
*TeamsApi* | [**create_a_team**](docs/TeamsApi.md#create_a_team) | **POST** /api/v1/accounts/{account_id}/teams | Create a team
*TeamsApi* | [**delete_a_team**](docs/TeamsApi.md#delete_a_team) | **DELETE** /api/v1/accounts/{account_id}/teams/{team_id} | Delete a team
*TeamsApi* | [**delete_agent_in_team**](docs/TeamsApi.md#delete_agent_in_team) | **DELETE** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | Remove an Agent from Team
*TeamsApi* | [**get_details_of_a_single_team**](docs/TeamsApi.md#get_details_of_a_single_team) | **GET** /api/v1/accounts/{account_id}/teams/{team_id} | Get a team details
*TeamsApi* | [**get_team_members**](docs/TeamsApi.md#get_team_members) | **GET** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | List Agents in Team
*TeamsApi* | [**list_all_teams**](docs/TeamsApi.md#list_all_teams) | **GET** /api/v1/accounts/{account_id}/teams | List all teams
*TeamsApi* | [**update_a_team**](docs/TeamsApi.md#update_a_team) | **PATCH** /api/v1/accounts/{account_id}/teams/{team_id} | Update a team
*TeamsApi* | [**update_agents_in_team**](docs/TeamsApi.md#update_agents_in_team) | **PATCH** /api/v1/accounts/{account_id}/teams/{team_id}/team_members | Update Agents in Team
*UsersApi* | [**create_a_user**](docs/UsersApi.md#create_a_user) | **POST** /platform/api/v1/users | Create a User
*UsersApi* | [**delete_a_user**](docs/UsersApi.md#delete_a_user) | **DELETE** /platform/api/v1/users/{id} | Delete a User
*UsersApi* | [**get_details_of_a_user**](docs/UsersApi.md#get_details_of_a_user) | **GET** /platform/api/v1/users/{id} | Get an user details
*UsersApi* | [**get_sso_url_of_a_user**](docs/UsersApi.md#get_sso_url_of_a_user) | **GET** /platform/api/v1/users/{id}/login | Get User SSO Link
*UsersApi* | [**update_a_user**](docs/UsersApi.md#update_a_user) | **PATCH** /platform/api/v1/users/{id} | Update a user
*WebhooksApi* | [**create_a_webhook**](docs/WebhooksApi.md#create_a_webhook) | **POST** /api/v1/accounts/{account_id}/webhooks | Add a webhook
*WebhooksApi* | [**delete_a_webhook**](docs/WebhooksApi.md#delete_a_webhook) | **DELETE** /api/v1/accounts/{account_id}/webhooks/{webhook_id} | Delete a webhook
*WebhooksApi* | [**list_all_webhooks**](docs/WebhooksApi.md#list_all_webhooks) | **GET** /api/v1/accounts/{account_id}/webhooks | List all webhooks
*WebhooksApi* | [**update_a_webhook**](docs/WebhooksApi.md#update_a_webhook) | **PATCH** /api/v1/accounts/{account_id}/webhooks/{webhook_id} | Update a webhook object

## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountCreateUpdatePayload](docs/AccountCreateUpdatePayload.md)
 - [AccountIdAccountUsersBody](docs/AccountIdAccountUsersBody.md)
 - [AccountIdAccountUsersBody1](docs/AccountIdAccountUsersBody1.md)
 - [AccountIdAgentsBody](docs/AccountIdAgentsBody.md)
 - [AccountIdConversationsBody](docs/AccountIdConversationsBody.md)
 - [AccountIdInboxMembersBody](docs/AccountIdInboxMembersBody.md)
 - [AccountIdInboxMembersBody1](docs/AccountIdInboxMembersBody1.md)
 - [AccountIdInboxMembersBody2](docs/AccountIdInboxMembersBody2.md)
 - [AccountIdInboxesBody](docs/AccountIdInboxesBody.md)
 - [AccountSummary](docs/AccountSummary.md)
 - [AccountSummaryPrevious](docs/AccountSummaryPrevious.md)
 - [Agent](docs/Agent.md)
 - [AgentBot](docs/AgentBot.md)
 - [AgentBotCreateUpdatePayload](docs/AgentBotCreateUpdatePayload.md)
 - [AgentConversationMetrics](docs/AgentConversationMetrics.md)
 - [AgentConversationMetricsMetric](docs/AgentConversationMetricsMetric.md)
 - [AgentsIdBody](docs/AgentsIdBody.md)
 - [AllOfconversationFilterListPayloadItems](docs/AllOfconversationFilterListPayloadItems.md)
 - [AllOfconversationListDataPayloadItems](docs/AllOfconversationListDataPayloadItems.md)
 - [Apiv1accountsaccountIdcontactsfilterPayload](docs/Apiv1accountsaccountIdcontactsfilterPayload.md)
 - [Apiv1accountsaccountIdconversationsMessage](docs/Apiv1accountsaccountIdconversationsMessage.md)
 - [Apiv1accountsaccountIdconversationsMessageTemplateParams](docs/Apiv1accountsaccountIdconversationsMessageTemplateParams.md)
 - [Apiv1accountsaccountIdinboxesChannel](docs/Apiv1accountsaccountIdinboxesChannel.md)
 - [Apiv1accountsaccountIdinboxesidChannel](docs/Apiv1accountsaccountIdinboxesidChannel.md)
 - [Article](docs/Article.md)
 - [ArticleCreateUpdatePayload](docs/ArticleCreateUpdatePayload.md)
 - [AutomationRule](docs/AutomationRule.md)
 - [AutomationRuleCreateUpdatePayload](docs/AutomationRuleCreateUpdatePayload.md)
 - [BadRequestError](docs/BadRequestError.md)
 - [CannedResponse](docs/CannedResponse.md)
 - [CannedResponseCreateUpdatePayload](docs/CannedResponseCreateUpdatePayload.md)
 - [Category](docs/Category.md)
 - [CategoryCreateUpdatePayload](docs/CategoryCreateUpdatePayload.md)
 - [Contact](docs/Contact.md)
 - [ContactBase](docs/ContactBase.md)
 - [ContactConversations](docs/ContactConversations.md)
 - [ContactCreate](docs/ContactCreate.md)
 - [ContactInboxes](docs/ContactInboxes.md)
 - [ContactList](docs/ContactList.md)
 - [ContactPayload](docs/ContactPayload.md)
 - [ContactPayloadContact](docs/ContactPayloadContact.md)
 - [ContactUpdate](docs/ContactUpdate.md)
 - [ContactableInboxes](docs/ContactableInboxes.md)
 - [ContactsFilterBody](docs/ContactsFilterBody.md)
 - [Conversation](docs/Conversation.md)
 - [ConversationFilterList](docs/ConversationFilterList.md)
 - [ConversationIdAssignmentsBody](docs/ConversationIdAssignmentsBody.md)
 - [ConversationIdLabelsBody](docs/ConversationIdLabelsBody.md)
 - [ConversationIdTogglePriorityBody](docs/ConversationIdTogglePriorityBody.md)
 - [ConversationIdToggleStatusBody](docs/ConversationIdToggleStatusBody.md)
 - [ConversationLabels](docs/ConversationLabels.md)
 - [ConversationList](docs/ConversationList.md)
 - [ConversationListData](docs/ConversationListData.md)
 - [ConversationListDataMeta](docs/ConversationListDataMeta.md)
 - [ConversationMessageCreate](docs/ConversationMessageCreate.md)
 - [ConversationShow](docs/ConversationShow.md)
 - [ConversationShowMeta](docs/ConversationShowMeta.md)
 - [ConversationShowMetaSender](docs/ConversationShowMetaSender.md)
 - [ConversationStatusToggle](docs/ConversationStatusToggle.md)
 - [ConversationStatusTogglePayload](docs/ConversationStatusTogglePayload.md)
 - [ConversationsFilterBody](docs/ConversationsFilterBody.md)
 - [CustomAttribute](docs/CustomAttribute.md)
 - [CustomAttributeCreateUpdatePayload](docs/CustomAttributeCreateUpdatePayload.md)
 - [CustomFilter](docs/CustomFilter.md)
 - [CustomFilterCreateUpdatePayload](docs/CustomFilterCreateUpdatePayload.md)
 - [ExtendedContact](docs/ExtendedContact.md)
 - [GenericId](docs/GenericId.md)
 - [IdContactInboxesBody](docs/IdContactInboxesBody.md)
 - [IdSetAgentBotBody](docs/IdSetAgentBotBody.md)
 - [Inbox](docs/Inbox.md)
 - [InboxesIdBody](docs/InboxesIdBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [IntegrationsApp](docs/IntegrationsApp.md)
 - [IntegrationsHook](docs/IntegrationsHook.md)
 - [IntegrationsHookCreatePayload](docs/IntegrationsHookCreatePayload.md)
 - [IntegrationsHookUpdatePayload](docs/IntegrationsHookUpdatePayload.md)
 - [Message](docs/Message.md)
 - [PlatformAccount](docs/PlatformAccount.md)
 - [Portal](docs/Portal.md)
 - [PortalCreateUpdatePayload](docs/PortalCreateUpdatePayload.md)
 - [PublicContact](docs/PublicContact.md)
 - [PublicContactCreateUpdatePayload](docs/PublicContactCreateUpdatePayload.md)
 - [PublicConversation](docs/PublicConversation.md)
 - [PublicConversationCreatePayload](docs/PublicConversationCreatePayload.md)
 - [PublicInbox](docs/PublicInbox.md)
 - [PublicInboxWorkingHours](docs/PublicInboxWorkingHours.md)
 - [PublicMessage](docs/PublicMessage.md)
 - [PublicMessageCreatePayload](docs/PublicMessageCreatePayload.md)
 - [PublicMessageUpdatePayload](docs/PublicMessageUpdatePayload.md)
 - [RequestError](docs/RequestError.md)
 - [Team](docs/Team.md)
 - [TeamCreateUpdatePayload](docs/TeamCreateUpdatePayload.md)
 - [TeamIdTeamMembersBody](docs/TeamIdTeamMembersBody.md)
 - [TeamIdTeamMembersBody1](docs/TeamIdTeamMembersBody1.md)
 - [TeamIdTeamMembersBody2](docs/TeamIdTeamMembersBody2.md)
 - [User](docs/User.md)
 - [UserCreateUpdatePayload](docs/UserCreateUpdatePayload.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookCreateUpdatePayload](docs/WebhookCreateUpdatePayload.md)

## Documentation For Authorization


## agentBotApiKey

- **Type**: API key
- **API key parameter name**: api_access_token
- **Location**: HTTP header

## platformAppApiKey

- **Type**: API key
- **API key parameter name**: api_access_token
- **Location**: HTTP header

## userApiKey

- **Type**: API key
- **API key parameter name**: api_access_token
- **Location**: HTTP header


## Author

hello@chatwoot.com
