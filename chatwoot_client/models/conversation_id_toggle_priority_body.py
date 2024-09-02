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

class ConversationIdTogglePriorityBody(object):
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
        'priority': 'str'
    }

    attribute_map = {
        'priority': 'priority'
    }

    def __init__(self, priority=None):  # noqa: E501
        """ConversationIdTogglePriorityBody - a model defined in Swagger"""  # noqa: E501
        self._priority = None
        self.discriminator = None
        self.priority = priority

    @property
    def priority(self):
        """Gets the priority of this ConversationIdTogglePriorityBody.  # noqa: E501

        The priority of the conversation  # noqa: E501

        :return: The priority of this ConversationIdTogglePriorityBody.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ConversationIdTogglePriorityBody.

        The priority of the conversation  # noqa: E501

        :param priority: The priority of this ConversationIdTogglePriorityBody.  # noqa: E501
        :type: str
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501
        allowed_values = ["urgent", "high", "medium", "low", "none"]  # noqa: E501
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

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
        if issubclass(ConversationIdTogglePriorityBody, dict):
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
        if not isinstance(other, ConversationIdTogglePriorityBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
