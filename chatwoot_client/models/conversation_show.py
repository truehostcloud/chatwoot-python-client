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
from chatwoot_client.models.conversation import Conversation  # noqa: F401,E501

class ConversationShow(Conversation):
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
        'meta': 'ConversationShowMeta'
    }
    if hasattr(Conversation, "swagger_types"):
        swagger_types.update(Conversation.swagger_types)

    attribute_map = {
        'meta': 'meta'
    }
    if hasattr(Conversation, "attribute_map"):
        attribute_map.update(Conversation.attribute_map)

    def __init__(self, meta=None, *args, **kwargs):  # noqa: E501
        """ConversationShow - a model defined in Swagger"""  # noqa: E501
        self._meta = None
        self.discriminator = None
        if meta is not None:
            self.meta = meta
        Conversation.__init__(self, *args, **kwargs)

    @property
    def meta(self):
        """Gets the meta of this ConversationShow.  # noqa: E501


        :return: The meta of this ConversationShow.  # noqa: E501
        :rtype: ConversationShowMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ConversationShow.


        :param meta: The meta of this ConversationShow.  # noqa: E501
        :type: ConversationShowMeta
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
        if issubclass(ConversationShow, dict):
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
        if not isinstance(other, ConversationShow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
