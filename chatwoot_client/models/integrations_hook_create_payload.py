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

class IntegrationsHookCreatePayload(object):
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
        'app_id': 'str',
        'inbox_id': 'str',
        'settings': 'object'
    }

    attribute_map = {
        'app_id': 'app_id',
        'inbox_id': 'inbox_id',
        'settings': 'settings'
    }

    def __init__(self, app_id=None, inbox_id=None, settings=None):  # noqa: E501
        """IntegrationsHookCreatePayload - a model defined in Swagger"""  # noqa: E501
        self._app_id = None
        self._inbox_id = None
        self._settings = None
        self.discriminator = None
        if app_id is not None:
            self.app_id = app_id
        if inbox_id is not None:
            self.inbox_id = inbox_id
        if settings is not None:
            self.settings = settings

    @property
    def app_id(self):
        """Gets the app_id of this IntegrationsHookCreatePayload.  # noqa: E501

        The ID of app for which integration hook is being created  # noqa: E501

        :return: The app_id of this IntegrationsHookCreatePayload.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this IntegrationsHookCreatePayload.

        The ID of app for which integration hook is being created  # noqa: E501

        :param app_id: The app_id of this IntegrationsHookCreatePayload.  # noqa: E501
        :type: str
        """

        self._app_id = app_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this IntegrationsHookCreatePayload.  # noqa: E501

        The inbox ID, if the hook is an inbox hook  # noqa: E501

        :return: The inbox_id of this IntegrationsHookCreatePayload.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this IntegrationsHookCreatePayload.

        The inbox ID, if the hook is an inbox hook  # noqa: E501

        :param inbox_id: The inbox_id of this IntegrationsHookCreatePayload.  # noqa: E501
        :type: str
        """

        self._inbox_id = inbox_id

    @property
    def settings(self):
        """Gets the settings of this IntegrationsHookCreatePayload.  # noqa: E501

        The settings required by the integration  # noqa: E501

        :return: The settings of this IntegrationsHookCreatePayload.  # noqa: E501
        :rtype: object
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this IntegrationsHookCreatePayload.

        The settings required by the integration  # noqa: E501

        :param settings: The settings of this IntegrationsHookCreatePayload.  # noqa: E501
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
        if issubclass(IntegrationsHookCreatePayload, dict):
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
        if not isinstance(other, IntegrationsHookCreatePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
