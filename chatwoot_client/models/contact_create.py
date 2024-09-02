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

class ContactCreate(object):
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
        'inbox_id': 'float',
        'name': 'str',
        'email': 'str',
        'phone_number': 'str',
        'avatar': 'str',
        'avatar_url': 'str',
        'identifier': 'str',
        'custom_attributes': 'object'
    }

    attribute_map = {
        'inbox_id': 'inbox_id',
        'name': 'name',
        'email': 'email',
        'phone_number': 'phone_number',
        'avatar': 'avatar',
        'avatar_url': 'avatar_url',
        'identifier': 'identifier',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, inbox_id=None, name=None, email=None, phone_number=None, avatar=None, avatar_url=None, identifier=None, custom_attributes=None):  # noqa: E501
        """ContactCreate - a model defined in Swagger"""  # noqa: E501
        self._inbox_id = None
        self._name = None
        self._email = None
        self._phone_number = None
        self._avatar = None
        self._avatar_url = None
        self._identifier = None
        self._custom_attributes = None
        self.discriminator = None
        self.inbox_id = inbox_id
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if avatar is not None:
            self.avatar = avatar
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if identifier is not None:
            self.identifier = identifier
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes

    @property
    def inbox_id(self):
        """Gets the inbox_id of this ContactCreate.  # noqa: E501


        :return: The inbox_id of this ContactCreate.  # noqa: E501
        :rtype: float
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this ContactCreate.


        :param inbox_id: The inbox_id of this ContactCreate.  # noqa: E501
        :type: float
        """
        if inbox_id is None:
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def name(self):
        """Gets the name of this ContactCreate.  # noqa: E501

        name of the contact  # noqa: E501

        :return: The name of this ContactCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactCreate.

        name of the contact  # noqa: E501

        :param name: The name of this ContactCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this ContactCreate.  # noqa: E501

        email of the contact  # noqa: E501

        :return: The email of this ContactCreate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactCreate.

        email of the contact  # noqa: E501

        :param email: The email of this ContactCreate.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """Gets the phone_number of this ContactCreate.  # noqa: E501

        phone number of the contact  # noqa: E501

        :return: The phone_number of this ContactCreate.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ContactCreate.

        phone number of the contact  # noqa: E501

        :param phone_number: The phone_number of this ContactCreate.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def avatar(self):
        """Gets the avatar of this ContactCreate.  # noqa: E501

        Send the form data with the avatar image binary or use the avatar_url  # noqa: E501

        :return: The avatar of this ContactCreate.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this ContactCreate.

        Send the form data with the avatar image binary or use the avatar_url  # noqa: E501

        :param avatar: The avatar of this ContactCreate.  # noqa: E501
        :type: str
        """

        self._avatar = avatar

    @property
    def avatar_url(self):
        """Gets the avatar_url of this ContactCreate.  # noqa: E501

        The url to a jpeg, png file for the contact avatar  # noqa: E501

        :return: The avatar_url of this ContactCreate.  # noqa: E501
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """Sets the avatar_url of this ContactCreate.

        The url to a jpeg, png file for the contact avatar  # noqa: E501

        :param avatar_url: The avatar_url of this ContactCreate.  # noqa: E501
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def identifier(self):
        """Gets the identifier of this ContactCreate.  # noqa: E501

        A unique identifier for the contact in external system  # noqa: E501

        :return: The identifier of this ContactCreate.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ContactCreate.

        A unique identifier for the contact in external system  # noqa: E501

        :param identifier: The identifier of this ContactCreate.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this ContactCreate.  # noqa: E501

        An object where you can store custom attributes for contact. example {\"type\":\"customer\", \"age\":30}  # noqa: E501

        :return: The custom_attributes of this ContactCreate.  # noqa: E501
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this ContactCreate.

        An object where you can store custom attributes for contact. example {\"type\":\"customer\", \"age\":30}  # noqa: E501

        :param custom_attributes: The custom_attributes of this ContactCreate.  # noqa: E501
        :type: object
        """

        self._custom_attributes = custom_attributes

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
        if issubclass(ContactCreate, dict):
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
        if not isinstance(other, ContactCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
