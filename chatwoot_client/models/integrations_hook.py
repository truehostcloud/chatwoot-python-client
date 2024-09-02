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

class IntegrationsHook(object):
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
        'id': 'str',
        'app_id': 'str',
        'inbox_id': 'str',
        'account_id': 'str',
        'status': 'bool',
        'hook_type': 'bool',
        'settings': 'object'
    }

    attribute_map = {
        'id': 'id',
        'app_id': 'app_id',
        'inbox_id': 'inbox_id',
        'account_id': 'account_id',
        'status': 'status',
        'hook_type': 'hook_type',
        'settings': 'settings'
    }

    def __init__(self, id=None, app_id=None, inbox_id=None, account_id=None, status=None, hook_type=None, settings=None):  # noqa: E501
        """IntegrationsHook - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._app_id = None
        self._inbox_id = None
        self._account_id = None
        self._status = None
        self._hook_type = None
        self._settings = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if app_id is not None:
            self.app_id = app_id
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if account_id is not None:
            self.account_id = account_id
        if status is not None:
            self.status = status
        if hook_type is not None:
            self.hook_type = hook_type
        if settings is not None:
            self.settings = settings

    @property
    def id(self):
        """Gets the id of this IntegrationsHook.  # noqa: E501

        The ID of the integration hook  # noqa: E501

        :return: The id of this IntegrationsHook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntegrationsHook.

        The ID of the integration hook  # noqa: E501

        :param id: The id of this IntegrationsHook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def app_id(self):
        """Gets the app_id of this IntegrationsHook.  # noqa: E501

        The ID of the integration app  # noqa: E501

        :return: The app_id of this IntegrationsHook.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this IntegrationsHook.

        The ID of the integration app  # noqa: E501

        :param app_id: The app_id of this IntegrationsHook.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this IntegrationsHook.  # noqa: E501

        Inbox ID if its an Inbox integration  # noqa: E501

        :return: The inbox_id of this IntegrationsHook.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this IntegrationsHook.

        Inbox ID if its an Inbox integration  # noqa: E501

        :param inbox_id: The inbox_id of this IntegrationsHook.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def account_id(self):
        """Gets the account_id of this IntegrationsHook.  # noqa: E501

        Account ID of the integration  # noqa: E501

        :return: The account_id of this IntegrationsHook.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this IntegrationsHook.

        Account ID of the integration  # noqa: E501

        :param account_id: The account_id of this IntegrationsHook.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def status(self):
        """Gets the status of this IntegrationsHook.  # noqa: E501

        Whether the integration hook is enabled for the account  # noqa: E501

        :return: The status of this IntegrationsHook.  # noqa: E501
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IntegrationsHook.

        Whether the integration hook is enabled for the account  # noqa: E501

        :param status: The status of this IntegrationsHook.  # noqa: E501
        :type: bool
        """

        self._status = status

    @property
    def hook_type(self):
        """Gets the hook_type of this IntegrationsHook.  # noqa: E501

        Whether its an account or inbox integration hook  # noqa: E501

        :return: The hook_type of this IntegrationsHook.  # noqa: E501
        :rtype: bool
        """
        return self._hook_type

    @hook_type.setter
    def hook_type(self, hook_type):
        """Sets the hook_type of this IntegrationsHook.

        Whether its an account or inbox integration hook  # noqa: E501

        :param hook_type: The hook_type of this IntegrationsHook.  # noqa: E501
        :type: bool
        """

        self._hook_type = hook_type

    @property
    def settings(self):
        """Gets the settings of this IntegrationsHook.  # noqa: E501

        The associated settings for the integration  # noqa: E501

        :return: The settings of this IntegrationsHook.  # noqa: E501
        :rtype: object
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this IntegrationsHook.

        The associated settings for the integration  # noqa: E501

        :param settings: The settings of this IntegrationsHook.  # noqa: E501
        :type: object
        """

        self._settings = settings

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
        if issubclass(IntegrationsHook, dict):
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
        if not isinstance(other, IntegrationsHook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
