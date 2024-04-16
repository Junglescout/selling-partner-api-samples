# coding: utf-8

"""
    Amazon Shipping API

    The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.  # noqa: E501

    OpenAPI spec version: v2
    Contact: swa-api-core@amazon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CarrierAccountAttribute(object):
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
        'attribute_name': 'str',
        'property_group': 'str',
        'value': 'str'
    }

    attribute_map = {
        'attribute_name': 'attributeName',
        'property_group': 'propertyGroup',
        'value': 'value'
    }

    def __init__(self, attribute_name=None, property_group=None, value=None):  # noqa: E501
        """CarrierAccountAttribute - a model defined in Swagger"""  # noqa: E501
        self._attribute_name = None
        self._property_group = None
        self._value = None
        self.discriminator = None
        if attribute_name is not None:
            self.attribute_name = attribute_name
        if property_group is not None:
            self.property_group = property_group
        if value is not None:
            self.value = value

    @property
    def attribute_name(self):
        """Gets the attribute_name of this CarrierAccountAttribute.  # noqa: E501

        Attribute Name .  # noqa: E501

        :return: The attribute_name of this CarrierAccountAttribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name):
        """Sets the attribute_name of this CarrierAccountAttribute.

        Attribute Name .  # noqa: E501

        :param attribute_name: The attribute_name of this CarrierAccountAttribute.  # noqa: E501
        :type: str
        """

        self._attribute_name = attribute_name

    @property
    def property_group(self):
        """Gets the property_group of this CarrierAccountAttribute.  # noqa: E501

        Property Group.  # noqa: E501

        :return: The property_group of this CarrierAccountAttribute.  # noqa: E501
        :rtype: str
        """
        return self._property_group

    @property_group.setter
    def property_group(self, property_group):
        """Sets the property_group of this CarrierAccountAttribute.

        Property Group.  # noqa: E501

        :param property_group: The property_group of this CarrierAccountAttribute.  # noqa: E501
        :type: str
        """

        self._property_group = property_group

    @property
    def value(self):
        """Gets the value of this CarrierAccountAttribute.  # noqa: E501

        Value .  # noqa: E501

        :return: The value of this CarrierAccountAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CarrierAccountAttribute.

        Value .  # noqa: E501

        :param value: The value of this CarrierAccountAttribute.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(CarrierAccountAttribute, dict):
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
        if not isinstance(other, CarrierAccountAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other