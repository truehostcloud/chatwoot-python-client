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

class Team(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'allow_auto_assign': 'bool',
        'account_id': 'int',
        'is_member': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'allow_auto_assign': 'allow_auto_assign',
        'account_id': 'account_id',
        'is_member': 'is_member'
    }

    def __init__(self, id=None, name=None, description=None, allow_auto_assign=None, account_id=None, is_member=None):  # noqa: E501
        """Team - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._allow_auto_assign = None
        self._account_id = None
        self._is_member = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if allow_auto_assign is not None:
            self.allow_auto_assign = allow_auto_assign
        if account_id is not None:
            self.account_id = account_id
        if is_member is not None:
            self.is_member = is_member

    @property
    def id(self):
        """Gets the id of this Team.  # noqa: E501

        The ID of the team  # noqa: E501

        :return: The id of this Team.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Team.

        The ID of the team  # noqa: E501

        :param id: The id of this Team.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501

        The name of the team  # noqa: E501

        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.

        The name of the team  # noqa: E501

        :param name: The name of this Team.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Team.  # noqa: E501

        The description about the team  # noqa: E501

        :return: The description of this Team.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Team.

        The description about the team  # noqa: E501

        :param description: The description of this Team.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def allow_auto_assign(self):
        """Gets the allow_auto_assign of this Team.  # noqa: E501

        If this setting is turned on, the system would automatically assign the conversation to an agent in the team while assigning the conversation to a team  # noqa: E501

        :return: The allow_auto_assign of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._allow_auto_assign

    @allow_auto_assign.setter
    def allow_auto_assign(self, allow_auto_assign):
        """Sets the allow_auto_assign of this Team.

        If this setting is turned on, the system would automatically assign the conversation to an agent in the team while assigning the conversation to a team  # noqa: E501

        :param allow_auto_assign: The allow_auto_assign of this Team.  # noqa: E501
        :type: bool
        """

        self._allow_auto_assign = allow_auto_assign

    @property
    def account_id(self):
        """Gets the account_id of this Team.  # noqa: E501

        The ID of the account with the team is a part of  # noqa: E501

        :return: The account_id of this Team.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Team.

        The ID of the account with the team is a part of  # noqa: E501

        :param account_id: The account_id of this Team.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def is_member(self):
        """Gets the is_member of this Team.  # noqa: E501

        This field shows whether the current user is a part of the team  # noqa: E501

        :return: The is_member of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._is_member

    @is_member.setter
    def is_member(self, is_member):
        """Sets the is_member of this Team.

        This field shows whether the current user is a part of the team  # noqa: E501

        :param is_member: The is_member of this Team.  # noqa: E501
        :type: bool
        """

        self._is_member = is_member

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
        if issubclass(Team, dict):
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
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
