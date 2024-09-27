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

class ConversationSender(object):
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
        'additional_attributes': 'object',
        'availability_status': 'str',
        'email': 'str',
        'id': 'int',
        'name': 'str',
        'phone_number': 'str',
        'identifier': 'str',
        'custom_attributes': 'object',
        'last_activity_at': 'int',
        'created_at': 'int'
    }

    attribute_map = {
        'additional_attributes': 'additional_attributes',
        'availability_status': 'availability_status',
        'email': 'email',
        'id': 'id',
        'name': 'name',
        'phone_number': 'phone_number',
        'identifier': 'identifier',
        'custom_attributes': 'custom_attributes',
        'last_activity_at': 'last_activity_at',
        'created_at': 'created_at'
    }

    def __init__(self, additional_attributes=None, availability_status=None, email=None, id=None, name=None, phone_number=None, identifier=None, custom_attributes=None, last_activity_at=None, created_at=None):  # noqa: E501
        """ConversationSender - a model defined in Swagger"""  # noqa: E501
        self._additional_attributes = None
        self._availability_status = None
        self._email = None
        self._id = None
        self._name = None
        self._phone_number = None
        self._identifier = None
        self._custom_attributes = None
        self._last_activity_at = None
        self._created_at = None
        self.discriminator = None
        if additional_attributes is not None:
            self.additional_attributes = additional_attributes
        if availability_status is not None:
            self.availability_status = availability_status
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if phone_number is not None:
            self.phone_number = phone_number
        if identifier is not None:
            self.identifier = identifier
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if last_activity_at is not None:
            self.last_activity_at = last_activity_at
        if created_at is not None:
            self.created_at = created_at

    @property
    def additional_attributes(self):
        """Gets the additional_attributes of this ConversationSender.  # noqa: E501

        The object containing additional attributes related to the sender  # noqa: E501

        :return: The additional_attributes of this ConversationSender.  # noqa: E501
        :rtype: object
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """Sets the additional_attributes of this ConversationSender.

        The object containing additional attributes related to the sender  # noqa: E501

        :param additional_attributes: The additional_attributes of this ConversationSender.  # noqa: E501
        :type: object
        """

        self._additional_attributes = additional_attributes

    @property
    def availability_status(self):
        """Gets the availability_status of this ConversationSender.  # noqa: E501

        Availability status of the user  # noqa: E501

        :return: The availability_status of this ConversationSender.  # noqa: E501
        :rtype: str
        """
        return self._availability_status

    @availability_status.setter
    def availability_status(self, availability_status):
        """Sets the availability_status of this ConversationSender.

        Availability status of the user  # noqa: E501

        :param availability_status: The availability_status of this ConversationSender.  # noqa: E501
        :type: str
        """
        allowed_values = ["online", "offline"]  # noqa: E501
        if availability_status not in allowed_values:
            raise ValueError(
                "Invalid value for `availability_status` ({0}), must be one of {1}"  # noqa: E501
                .format(availability_status, allowed_values)
            )

        self._availability_status = availability_status

    @property
    def email(self):
        """Gets the email of this ConversationSender.  # noqa: E501

        Email address of the sender  # noqa: E501

        :return: The email of this ConversationSender.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ConversationSender.

        Email address of the sender  # noqa: E501

        :param email: The email of this ConversationSender.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this ConversationSender.  # noqa: E501

        ID of the sender  # noqa: E501

        :return: The id of this ConversationSender.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConversationSender.

        ID of the sender  # noqa: E501

        :param id: The id of this ConversationSender.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ConversationSender.  # noqa: E501

        The name of the sender  # noqa: E501

        :return: The name of this ConversationSender.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConversationSender.

        The name of the sender  # noqa: E501

        :param name: The name of this ConversationSender.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_number(self):
        """Gets the phone_number of this ConversationSender.  # noqa: E501

        Phone number of the sender  # noqa: E501

        :return: The phone_number of this ConversationSender.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ConversationSender.

        Phone number of the sender  # noqa: E501

        :param phone_number: The phone_number of this ConversationSender.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def identifier(self):
        """Gets the identifier of this ConversationSender.  # noqa: E501

        A unique identifier for the contact in external system  # noqa: E501

        :return: The identifier of this ConversationSender.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ConversationSender.

        A unique identifier for the contact in external system  # noqa: E501

        :param identifier: The identifier of this ConversationSender.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this ConversationSender.  # noqa: E501

        An object where you can store custom attributes for contact.  # noqa: E501

        :return: The custom_attributes of this ConversationSender.  # noqa: E501
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this ConversationSender.

        An object where you can store custom attributes for contact.  # noqa: E501

        :param custom_attributes: The custom_attributes of this ConversationSender.  # noqa: E501
        :type: object
        """

        self._custom_attributes = custom_attributes

    @property
    def last_activity_at(self):
        """Gets the last_activity_at of this ConversationSender.  # noqa: E501

        The time at which the last activity was done  # noqa: E501

        :return: The last_activity_at of this ConversationSender.  # noqa: E501
        :rtype: int
        """
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, last_activity_at):
        """Sets the last_activity_at of this ConversationSender.

        The time at which the last activity was done  # noqa: E501

        :param last_activity_at: The last_activity_at of this ConversationSender.  # noqa: E501
        :type: int
        """

        self._last_activity_at = last_activity_at

    @property
    def created_at(self):
        """Gets the created_at of this ConversationSender.  # noqa: E501

        The time at which the sender was created  # noqa: E501

        :return: The created_at of this ConversationSender.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConversationSender.

        The time at which the sender was created  # noqa: E501

        :param created_at: The created_at of this ConversationSender.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

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
        if issubclass(ConversationSender, dict):
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
        if not isinstance(other, ConversationSender):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other