# coding: utf-8

"""
    Selling Partner API for Merchant Fulfillment

    The Selling Partner API for Merchant Fulfillment helps you build applications that let sellers purchase shipping for non-Prime and Prime orders using Amazon’s Buy Shipping Services.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from src.api_models.mfn_api.swagger_client.configuration import Configuration


class AdditionalSellerInputs(object):
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
        'additional_input_field_name': 'str',
        'additional_seller_input': 'AdditionalSellerInput'
    }

    attribute_map = {
        'additional_input_field_name': 'AdditionalInputFieldName',
        'additional_seller_input': 'AdditionalSellerInput'
    }

    def __init__(self, additional_input_field_name=None, additional_seller_input=None, _configuration=None):  # noqa: E501
        """AdditionalSellerInputs - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additional_input_field_name = None
        self._additional_seller_input = None
        self.discriminator = None

        self.additional_input_field_name = additional_input_field_name
        self.additional_seller_input = additional_seller_input

    @property
    def additional_input_field_name(self):
        """Gets the additional_input_field_name of this AdditionalSellerInputs.  # noqa: E501

        The name of the additional input field.  # noqa: E501

        :return: The additional_input_field_name of this AdditionalSellerInputs.  # noqa: E501
        :rtype: str
        """
        return self._additional_input_field_name

    @additional_input_field_name.setter
    def additional_input_field_name(self, additional_input_field_name):
        """Sets the additional_input_field_name of this AdditionalSellerInputs.

        The name of the additional input field.  # noqa: E501

        :param additional_input_field_name: The additional_input_field_name of this AdditionalSellerInputs.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and additional_input_field_name is None:
            raise ValueError("Invalid value for `additional_input_field_name`, must not be `None`")  # noqa: E501

        self._additional_input_field_name = additional_input_field_name

    @property
    def additional_seller_input(self):
        """Gets the additional_seller_input of this AdditionalSellerInputs.  # noqa: E501


        :return: The additional_seller_input of this AdditionalSellerInputs.  # noqa: E501
        :rtype: AdditionalSellerInput
        """
        return self._additional_seller_input

    @additional_seller_input.setter
    def additional_seller_input(self, additional_seller_input):
        """Sets the additional_seller_input of this AdditionalSellerInputs.


        :param additional_seller_input: The additional_seller_input of this AdditionalSellerInputs.  # noqa: E501
        :type: AdditionalSellerInput
        """
        if self._configuration.client_side_validation and additional_seller_input is None:
            raise ValueError("Invalid value for `additional_seller_input`, must not be `None`")  # noqa: E501

        self._additional_seller_input = additional_seller_input

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
        if issubclass(AdditionalSellerInputs, dict):
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
        if not isinstance(other, AdditionalSellerInputs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalSellerInputs):
            return True

        return self.to_dict() != other.to_dict()