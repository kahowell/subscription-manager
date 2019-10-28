# coding: utf-8

"""
    candlepin-rpc-api

    RPC-ish interface for candlepin.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Module(object):
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
        'name': 'str',
        'stream': 'str',
        'version': 'str',
        'context': 'str',
        'arch': 'str',
        'profiles': 'list[str]',
        'installed_profiles': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'stream': 'stream',
        'version': 'version',
        'context': 'context',
        'arch': 'arch',
        'profiles': 'profiles',
        'installed_profiles': 'installed_profiles',
        'status': 'status'
    }

    def __init__(self, name=None, stream=None, version=None, context=None, arch=None, profiles=None, installed_profiles=None, status=None):  # noqa: E501
        """Module - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._stream = None
        self._version = None
        self._context = None
        self._arch = None
        self._profiles = None
        self._installed_profiles = None
        self._status = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if stream is not None:
            self.stream = stream
        if version is not None:
            self.version = version
        if context is not None:
            self.context = context
        if arch is not None:
            self.arch = arch
        if profiles is not None:
            self.profiles = profiles
        if installed_profiles is not None:
            self.installed_profiles = installed_profiles
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this Module.  # noqa: E501


        :return: The name of this Module.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Module.


        :param name: The name of this Module.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def stream(self):
        """Gets the stream of this Module.  # noqa: E501


        :return: The stream of this Module.  # noqa: E501
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this Module.


        :param stream: The stream of this Module.  # noqa: E501
        :type: str
        """

        self._stream = stream

    @property
    def version(self):
        """Gets the version of this Module.  # noqa: E501


        :return: The version of this Module.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Module.


        :param version: The version of this Module.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def context(self):
        """Gets the context of this Module.  # noqa: E501


        :return: The context of this Module.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this Module.


        :param context: The context of this Module.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def arch(self):
        """Gets the arch of this Module.  # noqa: E501


        :return: The arch of this Module.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this Module.


        :param arch: The arch of this Module.  # noqa: E501
        :type: str
        """

        self._arch = arch

    @property
    def profiles(self):
        """Gets the profiles of this Module.  # noqa: E501


        :return: The profiles of this Module.  # noqa: E501
        :rtype: list[str]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this Module.


        :param profiles: The profiles of this Module.  # noqa: E501
        :type: list[str]
        """

        self._profiles = profiles

    @property
    def installed_profiles(self):
        """Gets the installed_profiles of this Module.  # noqa: E501


        :return: The installed_profiles of this Module.  # noqa: E501
        :rtype: list[str]
        """
        return self._installed_profiles

    @installed_profiles.setter
    def installed_profiles(self, installed_profiles):
        """Sets the installed_profiles of this Module.


        :param installed_profiles: The installed_profiles of this Module.  # noqa: E501
        :type: list[str]
        """

        self._installed_profiles = installed_profiles

    @property
    def status(self):
        """Gets the status of this Module.  # noqa: E501


        :return: The status of this Module.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Module.


        :param status: The status of this Module.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(Module, dict):
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
        if not isinstance(other, Module):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
