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

class InlineResponse2007(object):
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
        'open': 'int',
        'unattended': 'int',
        'unassigned': 'int'
    }

    attribute_map = {
        'open': 'open',
        'unattended': 'unattended',
        'unassigned': 'unassigned'
    }

    def __init__(self, open=None, unattended=None, unassigned=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501
        self._open = None
        self._unattended = None
        self._unassigned = None
        self.discriminator = None
        if open is not None:
            self.open = open
        if unattended is not None:
            self.unattended = unattended
        if unassigned is not None:
            self.unassigned = unassigned

    @property
    def open(self):
        """Gets the open of this InlineResponse2007.  # noqa: E501


        :return: The open of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this InlineResponse2007.


        :param open: The open of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._open = open

    @property
    def unattended(self):
        """Gets the unattended of this InlineResponse2007.  # noqa: E501


        :return: The unattended of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._unattended

    @unattended.setter
    def unattended(self, unattended):
        """Sets the unattended of this InlineResponse2007.


        :param unattended: The unattended of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._unattended = unattended

    @property
    def unassigned(self):
        """Gets the unassigned of this InlineResponse2007.  # noqa: E501


        :return: The unassigned of this InlineResponse2007.  # noqa: E501
        :rtype: int
        """
        return self._unassigned

    @unassigned.setter
    def unassigned(self, unassigned):
        """Sets the unassigned of this InlineResponse2007.


        :param unassigned: The unassigned of this InlineResponse2007.  # noqa: E501
        :type: int
        """

        self._unassigned = unassigned

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
