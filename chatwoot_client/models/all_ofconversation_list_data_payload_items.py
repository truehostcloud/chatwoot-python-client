# coding: utf-8

"""
    Chatwoot

    This is the API documentation for Chatwoot server.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@chatwoot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from chatwoot_client.models.generic_id import GenericId  # noqa: F401,E501

class AllOfconversationListDataPayloadItems(GenericId):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'float',
        'messages': 'list[Message]',
        'account_id': 'float',
        'inbox_id': 'float',
        'status': 'str',
        'timestamp': 'str',
        'contact_last_seen_at': 'str',
        'agent_last_seen_at': 'str',
        'last_activity_at': 'float',
        'last_non_activity_message': 'Message',
        'unread_count': 'float',
        'additional_attributes': 'object',
        'custom_attributes': 'object',
        'meta': 'object'
    }
    if hasattr(GenericId, "swagger_types"):
        swagger_types.update(GenericId.swagger_types)

    attribute_map = {
        'id': 'id',
        'messages': 'messages',
        'account_id': 'account_id',
        'inbox_id': 'inbox_id',
        'status': 'status',
        'timestamp': 'timestamp',
        'contact_last_seen_at': 'contact_last_seen_at',
        'agent_last_seen_at': 'agent_last_seen_at',
        'last_activity_at': 'last_activity_at',
        'last_non_activity_message': 'last_non_activity_message',
        'unread_count': 'unread_count',
        'additional_attributes': 'additional_attributes',
        'custom_attributes': 'custom_attributes',
        'meta': 'meta'
    }
    if hasattr(GenericId, "attribute_map"):
        attribute_map.update(GenericId.attribute_map)

    def __init__(self, id=None, messages=None, account_id=None, inbox_id=None, status=None, timestamp=None, contact_last_seen_at=None, agent_last_seen_at=None, last_activity_at=None, last_non_activity_message=None, unread_count=None, additional_attributes=None, custom_attributes=None, meta=None, *args, **kwargs):  # noqa: E501
        """AllOfconversationListDataPayloadItems - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._messages = None
        self._account_id = None
        self._inbox_id = None
        self._status = None
        self._timestamp = None
        self._contact_last_seen_at = None
        self._agent_last_seen_at = None
        self._last_activity_at = None
        self._last_non_activity_message = None
        self._unread_count = None
        self._additional_attributes = None
        self._custom_attributes = None
        self._meta = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if messages is not None:
            self.messages = messages
        if account_id is not None:
            self.account_id = account_id
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if status is not None:
            self.status = status
        if timestamp is not None:
            self.timestamp = timestamp
        if contact_last_seen_at is not None:
            self.contact_last_seen_at = contact_last_seen_at
        if agent_last_seen_at is not None:
            self.agent_last_seen_at = agent_last_seen_at
        if last_activity_at is not None:
            self.last_activity_at = last_activity_at
        if last_non_activity_message is not None:
            self.last_non_activity_message = last_non_activity_message
        if unread_count is not None:
            self.unread_count = unread_count
        if additional_attributes is not None:
            self.additional_attributes = additional_attributes
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if meta is not None:
            self.meta = meta
        GenericId.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this AllOfconversationListDataPayloadItems.  # noqa: E501

        ID of the conversation  # noqa: E501

        :return: The id of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllOfconversationListDataPayloadItems.

        ID of the conversation  # noqa: E501

        :param id: The id of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def messages(self):
        """Gets the messages of this AllOfconversationListDataPayloadItems.  # noqa: E501


        :return: The messages of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this AllOfconversationListDataPayloadItems.


        :param messages: The messages of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: list[Message]
        """

        self._messages = messages

    @property
    def account_id(self):
        """Gets the account_id of this AllOfconversationListDataPayloadItems.  # noqa: E501

        Account Id  # noqa: E501

        :return: The account_id of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: float
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AllOfconversationListDataPayloadItems.

        Account Id  # noqa: E501

        :param account_id: The account_id of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: float
        """

        self._account_id = account_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this AllOfconversationListDataPayloadItems.  # noqa: E501

        ID of the inbox  # noqa: E501

        :return: The inbox_id of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: float
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this AllOfconversationListDataPayloadItems.

        ID of the inbox  # noqa: E501

        :param inbox_id: The inbox_id of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: float
        """

        self._inbox_id = inbox_id

    @property
    def status(self):
        """Gets the status of this AllOfconversationListDataPayloadItems.  # noqa: E501

        The status of the conversation  # noqa: E501

        :return: The status of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AllOfconversationListDataPayloadItems.

        The status of the conversation  # noqa: E501

        :param status: The status of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "resolved", "pending"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def timestamp(self):
        """Gets the timestamp of this AllOfconversationListDataPayloadItems.  # noqa: E501

        The time at which conversation was created  # noqa: E501

        :return: The timestamp of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AllOfconversationListDataPayloadItems.

        The time at which conversation was created  # noqa: E501

        :param timestamp: The timestamp of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def contact_last_seen_at(self):
        """Gets the contact_last_seen_at of this AllOfconversationListDataPayloadItems.  # noqa: E501


        :return: The contact_last_seen_at of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: str
        """
        return self._contact_last_seen_at

    @contact_last_seen_at.setter
    def contact_last_seen_at(self, contact_last_seen_at):
        """Sets the contact_last_seen_at of this AllOfconversationListDataPayloadItems.


        :param contact_last_seen_at: The contact_last_seen_at of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: str
        """

        self._contact_last_seen_at = contact_last_seen_at

    @property
    def agent_last_seen_at(self):
        """Gets the agent_last_seen_at of this AllOfconversationListDataPayloadItems.  # noqa: E501


        :return: The agent_last_seen_at of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: str
        """
        return self._agent_last_seen_at

    @agent_last_seen_at.setter
    def agent_last_seen_at(self, agent_last_seen_at):
        """Sets the agent_last_seen_at of this AllOfconversationListDataPayloadItems.


        :param agent_last_seen_at: The agent_last_seen_at of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: str
        """

        self._agent_last_seen_at = agent_last_seen_at

    @property
    def last_activity_at(self):
        """Gets the last_activity_at of this AllOfconversationListDataPayloadItems.  # noqa: E501

        The time at which the last activity happened in the conversation  # noqa: E501

        :return: The last_activity_at of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: float
        """
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, last_activity_at):
        """Sets the last_activity_at of this AllOfconversationListDataPayloadItems.

        The time at which the last activity happened in the conversation  # noqa: E501

        :param last_activity_at: The last_activity_at of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: float
        """

        self._last_activity_at = last_activity_at

    @property
    def last_non_activity_message(self):
        """Gets the last_non_activity_message of this AllOfconversationListDataPayloadItems.  # noqa: E501


        :return: The last_non_activity_message of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: Message
        """
        return self._last_non_activity_message

    @last_non_activity_message.setter
    def last_non_activity_message(self, last_non_activity_message):
        """Sets the last_non_activity_message of this AllOfconversationListDataPayloadItems.


        :param last_non_activity_message: The last_non_activity_message of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: Message
        """

        self._last_non_activity_message = last_non_activity_message

    @property
    def unread_count(self):
        """Gets the unread_count of this AllOfconversationListDataPayloadItems.  # noqa: E501

        The number of unread messages  # noqa: E501

        :return: The unread_count of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: float
        """
        return self._unread_count

    @unread_count.setter
    def unread_count(self, unread_count):
        """Sets the unread_count of this AllOfconversationListDataPayloadItems.

        The number of unread messages  # noqa: E501

        :param unread_count: The unread_count of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: float
        """

        self._unread_count = unread_count

    @property
    def additional_attributes(self):
        """Gets the additional_attributes of this AllOfconversationListDataPayloadItems.  # noqa: E501

        The object containing additional attributes related to the conversation  # noqa: E501

        :return: The additional_attributes of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: object
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """Sets the additional_attributes of this AllOfconversationListDataPayloadItems.

        The object containing additional attributes related to the conversation  # noqa: E501

        :param additional_attributes: The additional_attributes of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: object
        """

        self._additional_attributes = additional_attributes

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this AllOfconversationListDataPayloadItems.  # noqa: E501

        The object to save custom attributes for conversation, accepts custom attributes key and value  # noqa: E501

        :return: The custom_attributes of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this AllOfconversationListDataPayloadItems.

        The object to save custom attributes for conversation, accepts custom attributes key and value  # noqa: E501

        :param custom_attributes: The custom_attributes of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: object
        """

        self._custom_attributes = custom_attributes

    @property
    def meta(self):
        """Gets the meta of this AllOfconversationListDataPayloadItems.  # noqa: E501


        :return: The meta of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this AllOfconversationListDataPayloadItems.


        :param meta: The meta of this AllOfconversationListDataPayloadItems.  # noqa: E501
        :type: object
        """

        self._meta = meta

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AllOfconversationListDataPayloadItems, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AllOfconversationListDataPayloadItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
