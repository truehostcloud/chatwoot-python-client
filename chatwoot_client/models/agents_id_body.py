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

class AgentsIdBody(object):
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
        'role': 'str',
        'availability': 'str',
        'auto_offline': 'bool'
    }

    attribute_map = {
        'role': 'role',
        'availability': 'availability',
        'auto_offline': 'auto_offline'
    }

    def __init__(self, role=None, availability=None, auto_offline=None):  # noqa: E501
        """AgentsIdBody - a model defined in Swagger"""  # noqa: E501
        self._role = None
        self._availability = None
        self._auto_offline = None
        self.discriminator = None
        self.role = role
        if availability is not None:
            self.availability = availability
        if auto_offline is not None:
            self.auto_offline = auto_offline

    @property
    def role(self):
        """Gets the role of this AgentsIdBody.  # noqa: E501

        Whether its administrator or agent  # noqa: E501

        :return: The role of this AgentsIdBody.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AgentsIdBody.

        Whether its administrator or agent  # noqa: E501

        :param role: The role of this AgentsIdBody.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["agent", "administrator"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def availability(self):
        """Gets the availability of this AgentsIdBody.  # noqa: E501

        The availability setting of the agent.  # noqa: E501

        :return: The availability of this AgentsIdBody.  # noqa: E501
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this AgentsIdBody.

        The availability setting of the agent.  # noqa: E501

        :param availability: The availability of this AgentsIdBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["available", "busy", "offline"]  # noqa: E501
        if availability not in allowed_values:
            raise ValueError(
                "Invalid value for `availability` ({0}), must be one of {1}"  # noqa: E501
                .format(availability, allowed_values)
            )

        self._availability = availability

    @property
    def auto_offline(self):
        """Gets the auto_offline of this AgentsIdBody.  # noqa: E501

        Whether the availability status of agent is configured to go offline automatically when away.  # noqa: E501

        :return: The auto_offline of this AgentsIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_offline

    @auto_offline.setter
    def auto_offline(self, auto_offline):
        """Sets the auto_offline of this AgentsIdBody.

        Whether the availability status of agent is configured to go offline automatically when away.  # noqa: E501

        :param auto_offline: The auto_offline of this AgentsIdBody.  # noqa: E501
        :type: bool
        """

        self._auto_offline = auto_offline

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
        if issubclass(AgentsIdBody, dict):
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
        if not isinstance(other, AgentsIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
