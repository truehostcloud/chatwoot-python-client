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

class Webhook(object):
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
        'url': 'str',
        'subscriptions': 'list[str]',
        'account_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'subscriptions': 'subscriptions',
        'account_id': 'account_id'
    }

    def __init__(self, id=None, url=None, subscriptions=None, account_id=None):  # noqa: E501
        """Webhook - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._url = None
        self._subscriptions = None
        self._account_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if subscriptions is not None:
            self.subscriptions = subscriptions
        if account_id is not None:
            self.account_id = account_id

    @property
    def id(self):
        """Gets the id of this Webhook.  # noqa: E501

        The ID of the webhook  # noqa: E501

        :return: The id of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Webhook.

        The ID of the webhook  # noqa: E501

        :param id: The id of this Webhook.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this Webhook.  # noqa: E501

        The url to which the events will be send  # noqa: E501

        :return: The url of this Webhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Webhook.

        The url to which the events will be send  # noqa: E501

        :param url: The url of this Webhook.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def subscriptions(self):
        """Gets the subscriptions of this Webhook.  # noqa: E501

        The list of subscribed events  # noqa: E501

        :return: The subscriptions of this Webhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this Webhook.

        The list of subscribed events  # noqa: E501

        :param subscriptions: The subscriptions of this Webhook.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["conversation_created", "conversation_status_changed", "conversation_updated", "contact_created", "contact_updated", "message_created", "message_updated", "webwidget_triggered"]  # noqa: E501
        if not set(subscriptions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `subscriptions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(subscriptions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._subscriptions = subscriptions

    @property
    def account_id(self):
        """Gets the account_id of this Webhook.  # noqa: E501

        The id of the account which the webhook object belongs to  # noqa: E501

        :return: The account_id of this Webhook.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Webhook.

        The id of the account which the webhook object belongs to  # noqa: E501

        :param account_id: The account_id of this Webhook.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

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
        if issubclass(Webhook, dict):
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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
