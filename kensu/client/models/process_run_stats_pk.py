# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat

from six import iteritems


class ProcessRunStatsPK(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'process_run_ref': 'ProcessRunRef',
        'timestamp': 'int'
    }

    attribute_map = {
        'process_run_ref': 'processRunRef',
        'timestamp': 'timestamp'
    }

    def __init__(self, process_run_ref=None, timestamp=None):
        """
        ProcessRunStatsPK - a model defined in Swagger
        """

        self._process_run_ref = None
        self._timestamp = None

        self.process_run_ref = process_run_ref
        self.timestamp = timestamp

    @property
    def process_run_ref(self):
        """
        Gets the process_run_ref of this ProcessRunStatsPK.

        :return: The process_run_ref of this ProcessRunStatsPK.
        :rtype: ProcessRunRef
        """
        return self._process_run_ref

    @process_run_ref.setter
    def process_run_ref(self, process_run_ref):
        """
        Sets the process_run_ref of this ProcessRunStatsPK.

        :param process_run_ref: The process_run_ref of this ProcessRunStatsPK.
        :type: ProcessRunRef
        """
        if process_run_ref is None:
            raise ValueError("Invalid value for `process_run_ref`, must not be `None`")

        self._process_run_ref = process_run_ref

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ProcessRunStatsPK.

        :return: The timestamp of this ProcessRunStatsPK.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ProcessRunStatsPK.

        :param timestamp: The timestamp of this ProcessRunStatsPK.
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProcessRunStatsPK):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other