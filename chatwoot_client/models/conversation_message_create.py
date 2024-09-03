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

class ConversationMessageCreate(object):
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
        'content': 'str',
        'message_type': 'str',
        'private': 'bool',
        'content_type': 'str',
        'content_attributes': 'object',
        'template_params': 'Apiv1accountsaccountIdconversationsMessageTemplateParams'
    }

    attribute_map = {
        'content': 'content',
        'message_type': 'message_type',
        'private': 'private',
        'content_type': 'content_type',
        'content_attributes': 'content_attributes',
        'template_params': 'template_params'
    }

    def __init__(self, content=None, message_type=None, private=None, content_type=None, content_attributes=None, template_params=None):  # noqa: E501
        """ConversationMessageCreate - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._message_type = None
        self._private = None
        self._content_type = None
        self._content_attributes = None
        self._template_params = None
        self.discriminator = None
        self.content = content
        if message_type is not None:
            self.message_type = message_type
        if private is not None:
            self.private = private
        if content_type is not None:
            self.content_type = content_type
        if content_attributes is not None:
            self.content_attributes = content_attributes
        if template_params is not None:
            self.template_params = template_params

    @property
    def content(self):
        """Gets the content of this ConversationMessageCreate.  # noqa: E501

        The content of the message  # noqa: E501

        :return: The content of this ConversationMessageCreate.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ConversationMessageCreate.

        The content of the message  # noqa: E501

        :param content: The content of this ConversationMessageCreate.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def message_type(self):
        """Gets the message_type of this ConversationMessageCreate.  # noqa: E501


        :return: The message_type of this ConversationMessageCreate.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this ConversationMessageCreate.


        :param message_type: The message_type of this ConversationMessageCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["outgoing", "incoming"]  # noqa: E501
        if message_type not in allowed_values:
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def private(self):
        """Gets the private of this ConversationMessageCreate.  # noqa: E501

        Flag to identify if it is a private note  # noqa: E501

        :return: The private of this ConversationMessageCreate.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this ConversationMessageCreate.

        Flag to identify if it is a private note  # noqa: E501

        :param private: The private of this ConversationMessageCreate.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def content_type(self):
        """Gets the content_type of this ConversationMessageCreate.  # noqa: E501

        if you want to create custom message types  # noqa: E501

        :return: The content_type of this ConversationMessageCreate.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ConversationMessageCreate.

        if you want to create custom message types  # noqa: E501

        :param content_type: The content_type of this ConversationMessageCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["input_email", "cards", "input_select", "form", "article", "input_csat", "text"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def content_attributes(self):
        """Gets the content_attributes of this ConversationMessageCreate.  # noqa: E501

        attributes based on your content type  # noqa: E501

        :return: The content_attributes of this ConversationMessageCreate.  # noqa: E501
        :rtype: object
        """
        return self._content_attributes

    @content_attributes.setter
    def content_attributes(self, content_attributes):
        """Sets the content_attributes of this ConversationMessageCreate.

        attributes based on your content type  # noqa: E501

        :param content_attributes: The content_attributes of this ConversationMessageCreate.  # noqa: E501
        :type: object
        """

        self._content_attributes = content_attributes

    @property
    def template_params(self):
        """Gets the template_params of this ConversationMessageCreate.  # noqa: E501


        :return: The template_params of this ConversationMessageCreate.  # noqa: E501
        :rtype: Apiv1accountsaccountIdconversationsMessageTemplateParams
        """
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        """Sets the template_params of this ConversationMessageCreate.


        :param template_params: The template_params of this ConversationMessageCreate.  # noqa: E501
        :type: Apiv1accountsaccountIdconversationsMessageTemplateParams
        """

        self._template_params = template_params

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
        if issubclass(ConversationMessageCreate, dict):
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
        if not isinstance(other, ConversationMessageCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
