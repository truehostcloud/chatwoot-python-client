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

class Account(object):
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
        'name': 'str',
        'role': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role'
    }

    def __init__(self, id=None, name=None, role=None):  # noqa: E501
        """Account - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._role = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role

    @property
    def id(self):
        """Gets the id of this Account.  # noqa: E501

        Account ID  # noqa: E501

        :return: The id of this Account.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Account.

        Account ID  # noqa: E501

        :param id: The id of this Account.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Account.  # noqa: E501

        Name of the account  # noqa: E501

        :return: The name of this Account.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Account.

        Name of the account  # noqa: E501

        :param name: The name of this Account.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """Gets the role of this Account.  # noqa: E501

        The user role in the account  # noqa: E501

        :return: The role of this Account.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Account.

        The user role in the account  # noqa: E501

        :param role: The role of this Account.  # noqa: E501
        :type: str
        """
        allowed_values = ["administrator", "agent"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if issubclass(Account, dict):
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
        if not isinstance(other, Account):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
