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

class Inbox(object):
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
        'website_url': 'str',
        'channel_type': 'str',
        'avatar_url': 'str',
        'widget_color': 'str',
        'website_token': 'str',
        'enable_auto_assignment': 'bool',
        'web_widget_script': 'str',
        'welcome_title': 'str',
        'welcome_tagline': 'str',
        'greeting_enabled': 'bool',
        'greeting_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'website_url': 'website_url',
        'channel_type': 'channel_type',
        'avatar_url': 'avatar_url',
        'widget_color': 'widget_color',
        'website_token': 'website_token',
        'enable_auto_assignment': 'enable_auto_assignment',
        'web_widget_script': 'web_widget_script',
        'welcome_title': 'welcome_title',
        'welcome_tagline': 'welcome_tagline',
        'greeting_enabled': 'greeting_enabled',
        'greeting_message': 'greeting_message'
    }

    def __init__(self, id=None, name=None, website_url=None, channel_type=None, avatar_url=None, widget_color=None, website_token=None, enable_auto_assignment=None, web_widget_script=None, welcome_title=None, welcome_tagline=None, greeting_enabled=None, greeting_message=None):  # noqa: E501
        """Inbox - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._website_url = None
        self._channel_type = None
        self._avatar_url = None
        self._widget_color = None
        self._website_token = None
        self._enable_auto_assignment = None
        self._web_widget_script = None
        self._welcome_title = None
        self._welcome_tagline = None
        self._greeting_enabled = None
        self._greeting_message = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if website_url is not None:
            self.website_url = website_url
        if channel_type is not None:
            self.channel_type = channel_type
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if widget_color is not None:
            self.widget_color = widget_color
        if website_token is not None:
            self.website_token = website_token
        if enable_auto_assignment is not None:
            self.enable_auto_assignment = enable_auto_assignment
        if web_widget_script is not None:
            self.web_widget_script = web_widget_script
        if welcome_title is not None:
            self.welcome_title = welcome_title
        if welcome_tagline is not None:
            self.welcome_tagline = welcome_tagline
        if greeting_enabled is not None:
            self.greeting_enabled = greeting_enabled
        if greeting_message is not None:
            self.greeting_message = greeting_message

    @property
    def id(self):
        """Gets the id of this Inbox.  # noqa: E501

        ID of the inbox  # noqa: E501

        :return: The id of this Inbox.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Inbox.

        ID of the inbox  # noqa: E501

        :param id: The id of this Inbox.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Inbox.  # noqa: E501

        The name of the inbox  # noqa: E501

        :return: The name of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Inbox.

        The name of the inbox  # noqa: E501

        :param name: The name of this Inbox.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def website_url(self):
        """Gets the website_url of this Inbox.  # noqa: E501

        Website URL  # noqa: E501

        :return: The website_url of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """Sets the website_url of this Inbox.

        Website URL  # noqa: E501

        :param website_url: The website_url of this Inbox.  # noqa: E501
        :type: str
        """

        self._website_url = website_url

    @property
    def channel_type(self):
        """Gets the channel_type of this Inbox.  # noqa: E501

        The type of the inbox  # noqa: E501

        :return: The channel_type of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this Inbox.

        The type of the inbox  # noqa: E501

        :param channel_type: The channel_type of this Inbox.  # noqa: E501
        :type: str
        """

        self._channel_type = channel_type

    @property
    def avatar_url(self):
        """Gets the avatar_url of this Inbox.  # noqa: E501

        The avatar image of the inbox  # noqa: E501

        :return: The avatar_url of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this Inbox.

        The avatar image of the inbox  # noqa: E501

        :param avatar_url: The avatar_url of this Inbox.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def widget_color(self):
        """Gets the widget_color of this Inbox.  # noqa: E501

        Widget Color used for customization of the widget  # noqa: E501

        :return: The widget_color of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._widget_color

    @widget_color.setter
    def widget_color(self, widget_color):
        """Sets the widget_color of this Inbox.

        Widget Color used for customization of the widget  # noqa: E501

        :param widget_color: The widget_color of this Inbox.  # noqa: E501
        :type: str
        """

        self._widget_color = widget_color

    @property
    def website_token(self):
        """Gets the website_token of this Inbox.  # noqa: E501

        Website Token  # noqa: E501

        :return: The website_token of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._website_token

    @website_token.setter
    def website_token(self, website_token):
        """Sets the website_token of this Inbox.

        Website Token  # noqa: E501

        :param website_token: The website_token of this Inbox.  # noqa: E501
        :type: str
        """

        self._website_token = website_token

    @property
    def enable_auto_assignment(self):
        """Gets the enable_auto_assignment of this Inbox.  # noqa: E501

        The flag which shows whether Auto Assignment is enabled or not  # noqa: E501

        :return: The enable_auto_assignment of this Inbox.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_assignment

    @enable_auto_assignment.setter
    def enable_auto_assignment(self, enable_auto_assignment):
        """Sets the enable_auto_assignment of this Inbox.

        The flag which shows whether Auto Assignment is enabled or not  # noqa: E501

        :param enable_auto_assignment: The enable_auto_assignment of this Inbox.  # noqa: E501
        :type: bool
        """

        self._enable_auto_assignment = enable_auto_assignment

    @property
    def web_widget_script(self):
        """Gets the web_widget_script of this Inbox.  # noqa: E501

        Script used to load the website widget  # noqa: E501

        :return: The web_widget_script of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._web_widget_script

    @web_widget_script.setter
    def web_widget_script(self, web_widget_script):
        """Sets the web_widget_script of this Inbox.

        Script used to load the website widget  # noqa: E501

        :param web_widget_script: The web_widget_script of this Inbox.  # noqa: E501
        :type: str
        """

        self._web_widget_script = web_widget_script

    @property
    def welcome_title(self):
        """Gets the welcome_title of this Inbox.  # noqa: E501

        Welcome title to be displayed on the widget  # noqa: E501

        :return: The welcome_title of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._welcome_title

    @welcome_title.setter
    def welcome_title(self, welcome_title):
        """Sets the welcome_title of this Inbox.

        Welcome title to be displayed on the widget  # noqa: E501

        :param welcome_title: The welcome_title of this Inbox.  # noqa: E501
        :type: str
        """

        self._welcome_title = welcome_title

    @property
    def welcome_tagline(self):
        """Gets the welcome_tagline of this Inbox.  # noqa: E501

        Welcome tagline to be displayed on the widget  # noqa: E501

        :return: The welcome_tagline of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._welcome_tagline

    @welcome_tagline.setter
    def welcome_tagline(self, welcome_tagline):
        """Sets the welcome_tagline of this Inbox.

        Welcome tagline to be displayed on the widget  # noqa: E501

        :param welcome_tagline: The welcome_tagline of this Inbox.  # noqa: E501
        :type: str
        """

        self._welcome_tagline = welcome_tagline

    @property
    def greeting_enabled(self):
        """Gets the greeting_enabled of this Inbox.  # noqa: E501

        The flag which shows whether greeting is enabled  # noqa: E501

        :return: The greeting_enabled of this Inbox.  # noqa: E501
        :rtype: bool
        """
        return self._greeting_enabled

    @greeting_enabled.setter
    def greeting_enabled(self, greeting_enabled):
        """Sets the greeting_enabled of this Inbox.

        The flag which shows whether greeting is enabled  # noqa: E501

        :param greeting_enabled: The greeting_enabled of this Inbox.  # noqa: E501
        :type: bool
        """

        self._greeting_enabled = greeting_enabled

    @property
    def greeting_message(self):
        """Gets the greeting_message of this Inbox.  # noqa: E501

        A greeting message when the user starts the conversation  # noqa: E501

        :return: The greeting_message of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._greeting_message

    @greeting_message.setter
    def greeting_message(self, greeting_message):
        """Sets the greeting_message of this Inbox.

        A greeting message when the user starts the conversation  # noqa: E501

        :param greeting_message: The greeting_message of this Inbox.  # noqa: E501
        :type: str
        """

        self._greeting_message = greeting_message

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
        if issubclass(Inbox, dict):
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
        if not isinstance(other, Inbox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
