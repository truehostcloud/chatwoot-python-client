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

class InlineResponse2005(GenericId):
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
        'content': 'str',
        'content_type': 'str',
        'content_attributes': 'object',
        'message_type': 'int',
        'created_at': 'int',
        'private': 'bool',
        'attachment': 'object',
        'sender': 'object',
        'conversation_id': 'int'
    }
    if hasattr(GenericId, "swagger_types"):
        swagger_types.update(GenericId.swagger_types)

    attribute_map = {
        'content': 'content',
        'content_type': 'content_type',
        'content_attributes': 'content_attributes',
        'message_type': 'message_type',
        'created_at': 'created_at',
        'private': 'private',
        'attachment': 'attachment',
        'sender': 'sender',
        'conversation_id': 'conversation_id'
    }
    if hasattr(GenericId, "attribute_map"):
        attribute_map.update(GenericId.attribute_map)

    def __init__(self, content=None, content_type=None, content_attributes=None, message_type=None, created_at=None, private=None, attachment=None, sender=None, conversation_id=None, *args, **kwargs):  # noqa: E501
        """InlineResponse2005 - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._content_type = None
        self._content_attributes = None
        self._message_type = None
        self._created_at = None
        self._private = None
        self._attachment = None
        self._sender = None
        self._conversation_id = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if content_type is not None:
            self.content_type = content_type
        if content_attributes is not None:
            self.content_attributes = content_attributes
        if message_type is not None:
            self.message_type = message_type
        if created_at is not None:
            self.created_at = created_at
        if private is not None:
            self.private = private
        if attachment is not None:
            self.attachment = attachment
        if sender is not None:
            self.sender = sender
        if conversation_id is not None:
            self.conversation_id = conversation_id
        GenericId.__init__(self, *args, **kwargs)

    @property
    def content(self):
        """Gets the content of this InlineResponse2005.  # noqa: E501

        The text content of the message  # noqa: E501

        :return: The content of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this InlineResponse2005.

        The text content of the message  # noqa: E501

        :param content: The content of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_type(self):
        """Gets the content_type of this InlineResponse2005.  # noqa: E501

        The type of the template message  # noqa: E501

        :return: The content_type of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this InlineResponse2005.

        The type of the template message  # noqa: E501

        :param content_type: The content_type of this InlineResponse2005.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "input_select", "cards", "form", "input_csat", "incoming_email"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def content_attributes(self):
        """Gets the content_attributes of this InlineResponse2005.  # noqa: E501

        The content attributes for each content_type  # noqa: E501

        :return: The content_attributes of this InlineResponse2005.  # noqa: E501
        :rtype: object
        """
        return self._content_attributes

    @content_attributes.setter
    def content_attributes(self, content_attributes):
        """Sets the content_attributes of this InlineResponse2005.

        The content attributes for each content_type  # noqa: E501

        :param content_attributes: The content_attributes of this InlineResponse2005.  # noqa: E501
        :type: object
        """

        self._content_attributes = content_attributes

    @property
    def message_type(self):
        """Gets the message_type of this InlineResponse2005.  # noqa: E501

        The type of the message  # noqa: E501

        :return: The message_type of this InlineResponse2005.  # noqa: E501
        :rtype: int
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this InlineResponse2005.

        The type of the message  # noqa: E501

        :param message_type: The message_type of this InlineResponse2005.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3]  # noqa: E501
        if message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2005.  # noqa: E501

        The time at which message was created  # noqa: E501

        :return: The created_at of this InlineResponse2005.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2005.

        The time at which message was created  # noqa: E501

        :param created_at: The created_at of this InlineResponse2005.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def private(self):
        """Gets the private of this InlineResponse2005.  # noqa: E501

        The flags which shows whether the message is private or not  # noqa: E501

        :return: The private of this InlineResponse2005.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this InlineResponse2005.

        The flags which shows whether the message is private or not  # noqa: E501

        :param private: The private of this InlineResponse2005.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def attachment(self):
        """Gets the attachment of this InlineResponse2005.  # noqa: E501

        The file object attached to the image  # noqa: E501

        :return: The attachment of this InlineResponse2005.  # noqa: E501
        :rtype: object
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this InlineResponse2005.

        The file object attached to the image  # noqa: E501

        :param attachment: The attachment of this InlineResponse2005.  # noqa: E501
        :type: object
        """

        self._attachment = attachment

    @property
    def sender(self):
        """Gets the sender of this InlineResponse2005.  # noqa: E501

        User/Agent/AgentBot object  # noqa: E501

        :return: The sender of this InlineResponse2005.  # noqa: E501
        :rtype: object
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this InlineResponse2005.

        User/Agent/AgentBot object  # noqa: E501

        :param sender: The sender of this InlineResponse2005.  # noqa: E501
        :type: object
        """

        self._sender = sender

    @property
    def conversation_id(self):
        """Gets the conversation_id of this InlineResponse2005.  # noqa: E501

        ID of the conversation  # noqa: E501

        :return: The conversation_id of this InlineResponse2005.  # noqa: E501
        :rtype: int
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id):
        """Sets the conversation_id of this InlineResponse2005.

        ID of the conversation  # noqa: E501

        :param conversation_id: The conversation_id of this InlineResponse2005.  # noqa: E501
        :type: int
        """

        self._conversation_id = conversation_id

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
        if issubclass(InlineResponse2005, dict):
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
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
