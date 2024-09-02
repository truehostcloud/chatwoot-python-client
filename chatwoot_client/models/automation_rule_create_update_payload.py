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

class AutomationRuleCreateUpdatePayload(object):
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
        'name': 'str',
        'description': 'str',
        'event_name': 'str',
        'active': 'bool',
        'actions': 'list[object]',
        'conditions': 'list[object]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'event_name': 'event_name',
        'active': 'active',
        'actions': 'actions',
        'conditions': 'conditions'
    }

    def __init__(self, name=None, description=None, event_name=None, active=None, actions=None, conditions=None):  # noqa: E501
        """AutomationRuleCreateUpdatePayload - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._event_name = None
        self._active = None
        self._actions = None
        self._conditions = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if event_name is not None:
            self.event_name = event_name
        if active is not None:
            self.active = active
        if actions is not None:
            self.actions = actions
        if conditions is not None:
            self.conditions = conditions

    @property
    def name(self):
        """Gets the name of this AutomationRuleCreateUpdatePayload.  # noqa: E501

        Rule name  # noqa: E501

        :return: The name of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutomationRuleCreateUpdatePayload.

        Rule name  # noqa: E501

        :param name: The name of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this AutomationRuleCreateUpdatePayload.  # noqa: E501

        The description about the automation and actions  # noqa: E501

        :return: The description of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AutomationRuleCreateUpdatePayload.

        The description about the automation and actions  # noqa: E501

        :param description: The description of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def event_name(self):
        """Gets the event_name of this AutomationRuleCreateUpdatePayload.  # noqa: E501

        The event when you want to execute the automation actions  # noqa: E501

        :return: The event_name of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this AutomationRuleCreateUpdatePayload.

        The event when you want to execute the automation actions  # noqa: E501

        :param event_name: The event_name of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["conversation_created", "conversation_updated", "message_created"]  # noqa: E501
        if event_name not in allowed_values:
            raise ValueError(
                "Invalid value for `event_name` ({0}), must be one of {1}"  # noqa: E501
                .format(event_name, allowed_values)
            )

        self._event_name = event_name

    @property
    def active(self):
        """Gets the active of this AutomationRuleCreateUpdatePayload.  # noqa: E501

        Enable/disable automation rule  # noqa: E501

        :return: The active of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AutomationRuleCreateUpdatePayload.

        Enable/disable automation rule  # noqa: E501

        :param active: The active of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def actions(self):
        """Gets the actions of this AutomationRuleCreateUpdatePayload.  # noqa: E501

        Array of actions which you want to perform when condition matches, e.g add label support if message contains content help.  # noqa: E501

        :return: The actions of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :rtype: list[object]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this AutomationRuleCreateUpdatePayload.

        Array of actions which you want to perform when condition matches, e.g add label support if message contains content help.  # noqa: E501

        :param actions: The actions of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :type: list[object]
        """

        self._actions = actions

    @property
    def conditions(self):
        """Gets the conditions of this AutomationRuleCreateUpdatePayload.  # noqa: E501

        Array of conditions on which conversation filter would work, e.g message content contains text help.  # noqa: E501

        :return: The conditions of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :rtype: list[object]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AutomationRuleCreateUpdatePayload.

        Array of conditions on which conversation filter would work, e.g message content contains text help.  # noqa: E501

        :param conditions: The conditions of this AutomationRuleCreateUpdatePayload.  # noqa: E501
        :type: list[object]
        """

        self._conditions = conditions

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
        if issubclass(AutomationRuleCreateUpdatePayload, dict):
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
        if not isinstance(other, AutomationRuleCreateUpdatePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
