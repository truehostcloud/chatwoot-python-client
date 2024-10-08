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

class AccountSummary(object):
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
        'avg_first_response_time': 'str',
        'avg_resolution_time': 'str',
        'conversations_count': 'int',
        'incoming_messages_count': 'int',
        'outgoing_messages_count': 'int',
        'resolutions_count': 'int',
        'previous': 'AccountSummaryPrevious'
    }

    attribute_map = {
        'avg_first_response_time': 'avg_first_response_time',
        'avg_resolution_time': 'avg_resolution_time',
        'conversations_count': 'conversations_count',
        'incoming_messages_count': 'incoming_messages_count',
        'outgoing_messages_count': 'outgoing_messages_count',
        'resolutions_count': 'resolutions_count',
        'previous': 'previous'
    }

    def __init__(self, avg_first_response_time=None, avg_resolution_time=None, conversations_count=None, incoming_messages_count=None, outgoing_messages_count=None, resolutions_count=None, previous=None):  # noqa: E501
        """AccountSummary - a model defined in Swagger"""  # noqa: E501
        self._avg_first_response_time = None
        self._avg_resolution_time = None
        self._conversations_count = None
        self._incoming_messages_count = None
        self._outgoing_messages_count = None
        self._resolutions_count = None
        self._previous = None
        self.discriminator = None
        if avg_first_response_time is not None:
            self.avg_first_response_time = avg_first_response_time
        if avg_resolution_time is not None:
            self.avg_resolution_time = avg_resolution_time
        if conversations_count is not None:
            self.conversations_count = conversations_count
        if incoming_messages_count is not None:
            self.incoming_messages_count = incoming_messages_count
        if outgoing_messages_count is not None:
            self.outgoing_messages_count = outgoing_messages_count
        if resolutions_count is not None:
            self.resolutions_count = resolutions_count
        if previous is not None:
            self.previous = previous

    @property
    def avg_first_response_time(self):
        """Gets the avg_first_response_time of this AccountSummary.  # noqa: E501


        :return: The avg_first_response_time of this AccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._avg_first_response_time

    @avg_first_response_time.setter
    def avg_first_response_time(self, avg_first_response_time):
        """Sets the avg_first_response_time of this AccountSummary.


        :param avg_first_response_time: The avg_first_response_time of this AccountSummary.  # noqa: E501
        :type: str
        """

        self._avg_first_response_time = avg_first_response_time

    @property
    def avg_resolution_time(self):
        """Gets the avg_resolution_time of this AccountSummary.  # noqa: E501


        :return: The avg_resolution_time of this AccountSummary.  # noqa: E501
        :rtype: str
        """
        return self._avg_resolution_time

    @avg_resolution_time.setter
    def avg_resolution_time(self, avg_resolution_time):
        """Sets the avg_resolution_time of this AccountSummary.


        :param avg_resolution_time: The avg_resolution_time of this AccountSummary.  # noqa: E501
        :type: str
        """

        self._avg_resolution_time = avg_resolution_time

    @property
    def conversations_count(self):
        """Gets the conversations_count of this AccountSummary.  # noqa: E501


        :return: The conversations_count of this AccountSummary.  # noqa: E501
        :rtype: int
        """
        return self._conversations_count

    @conversations_count.setter
    def conversations_count(self, conversations_count):
        """Sets the conversations_count of this AccountSummary.


        :param conversations_count: The conversations_count of this AccountSummary.  # noqa: E501
        :type: int
        """

        self._conversations_count = conversations_count

    @property
    def incoming_messages_count(self):
        """Gets the incoming_messages_count of this AccountSummary.  # noqa: E501


        :return: The incoming_messages_count of this AccountSummary.  # noqa: E501
        :rtype: int
        """
        return self._incoming_messages_count

    @incoming_messages_count.setter
    def incoming_messages_count(self, incoming_messages_count):
        """Sets the incoming_messages_count of this AccountSummary.


        :param incoming_messages_count: The incoming_messages_count of this AccountSummary.  # noqa: E501
        :type: int
        """

        self._incoming_messages_count = incoming_messages_count

    @property
    def outgoing_messages_count(self):
        """Gets the outgoing_messages_count of this AccountSummary.  # noqa: E501


        :return: The outgoing_messages_count of this AccountSummary.  # noqa: E501
        :rtype: int
        """
        return self._outgoing_messages_count

    @outgoing_messages_count.setter
    def outgoing_messages_count(self, outgoing_messages_count):
        """Sets the outgoing_messages_count of this AccountSummary.


        :param outgoing_messages_count: The outgoing_messages_count of this AccountSummary.  # noqa: E501
        :type: int
        """

        self._outgoing_messages_count = outgoing_messages_count

    @property
    def resolutions_count(self):
        """Gets the resolutions_count of this AccountSummary.  # noqa: E501


        :return: The resolutions_count of this AccountSummary.  # noqa: E501
        :rtype: int
        """
        return self._resolutions_count

    @resolutions_count.setter
    def resolutions_count(self, resolutions_count):
        """Sets the resolutions_count of this AccountSummary.


        :param resolutions_count: The resolutions_count of this AccountSummary.  # noqa: E501
        :type: int
        """

        self._resolutions_count = resolutions_count

    @property
    def previous(self):
        """Gets the previous of this AccountSummary.  # noqa: E501


        :return: The previous of this AccountSummary.  # noqa: E501
        :rtype: AccountSummaryPrevious
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this AccountSummary.


        :param previous: The previous of this AccountSummary.  # noqa: E501
        :type: AccountSummaryPrevious
        """

        self._previous = previous

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
        if issubclass(AccountSummary, dict):
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
        if not isinstance(other, AccountSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
