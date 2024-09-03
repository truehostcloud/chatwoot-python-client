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

class IdContactInboxesBody(object):
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
        'inbox_id': 'int',
        'source_id': 'str'
    }

    attribute_map = {
        'inbox_id': 'inbox_id',
        'source_id': 'source_id'
    }

    def __init__(self, inbox_id=None, source_id=None):  # noqa: E501
        """IdContactInboxesBody - a model defined in Swagger"""  # noqa: E501
        self._inbox_id = None
        self._source_id = None
        self.discriminator = None
        self.inbox_id = inbox_id
        if source_id is not None:
            self.source_id = source_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this IdContactInboxesBody.  # noqa: E501

        The ID of the inbox  # noqa: E501

        :return: The inbox_id of this IdContactInboxesBody.  # noqa: E501
        :rtype: int
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this IdContactInboxesBody.

        The ID of the inbox  # noqa: E501

        :param inbox_id: The inbox_id of this IdContactInboxesBody.  # noqa: E501
        :type: int
        """
        if inbox_id is None:
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def source_id(self):
        """Gets the source_id of this IdContactInboxesBody.  # noqa: E501

        Contact Inbox Source Id  # noqa: E501

        :return: The source_id of this IdContactInboxesBody.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this IdContactInboxesBody.

        Contact Inbox Source Id  # noqa: E501

        :param source_id: The source_id of this IdContactInboxesBody.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

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
        if issubclass(IdContactInboxesBody, dict):
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
        if not isinstance(other, IdContactInboxesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
