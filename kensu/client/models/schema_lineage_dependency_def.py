# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat

from six import iteritems


class SchemaLineageDependencyDef(object):
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
        'from_schema_ref': 'SchemaRef',
        'to_schema_ref': 'SchemaRef',
        'column_data_dependencies': 'dict(str, list[str])',
        'column_control_dependencies': 'dict(str, list[str])'
    }

    attribute_map = {
        'from_schema_ref': 'fromSchemaRef',
        'to_schema_ref': 'toSchemaRef',
        'column_data_dependencies': 'columnDataDependencies',
        'column_control_dependencies': 'columnControlDependencies'
    }

    def __init__(self, from_schema_ref=None, to_schema_ref=None, column_data_dependencies=None, column_control_dependencies=None):
        """
        SchemaLineageDependencyDef - a model defined in Swagger
        """

        self._from_schema_ref = None
        self._to_schema_ref = None
        self._column_data_dependencies = None
        self._column_control_dependencies = None

        self.from_schema_ref = from_schema_ref
        self.to_schema_ref = to_schema_ref
        if column_data_dependencies is not None:
          self.column_data_dependencies = column_data_dependencies
        if column_control_dependencies is not None:
          self.column_control_dependencies = column_control_dependencies

    @property
    def from_schema_ref(self):
        """
        Gets the from_schema_ref of this SchemaLineageDependencyDef.

        :return: The from_schema_ref of this SchemaLineageDependencyDef.
        :rtype: SchemaRef
        """
        return self._from_schema_ref

    @from_schema_ref.setter
    def from_schema_ref(self, from_schema_ref):
        """
        Sets the from_schema_ref of this SchemaLineageDependencyDef.

        :param from_schema_ref: The from_schema_ref of this SchemaLineageDependencyDef.
        :type: SchemaRef
        """
        if from_schema_ref is None:
            raise ValueError("Invalid value for `from_schema_ref`, must not be `None`")

        self._from_schema_ref = from_schema_ref

    @property
    def to_schema_ref(self):
        """
        Gets the to_schema_ref of this SchemaLineageDependencyDef.

        :return: The to_schema_ref of this SchemaLineageDependencyDef.
        :rtype: SchemaRef
        """
        return self._to_schema_ref

    @to_schema_ref.setter
    def to_schema_ref(self, to_schema_ref):
        """
        Sets the to_schema_ref of this SchemaLineageDependencyDef.

        :param to_schema_ref: The to_schema_ref of this SchemaLineageDependencyDef.
        :type: SchemaRef
        """
        if to_schema_ref is None:
            raise ValueError("Invalid value for `to_schema_ref`, must not be `None`")

        self._to_schema_ref = to_schema_ref

    @property
    def column_data_dependencies(self):
        """
        Gets the column_data_dependencies of this SchemaLineageDependencyDef.
        Column data-dependencies in format: output_column => list of its input columns

        :return: The column_data_dependencies of this SchemaLineageDependencyDef.
        :rtype: dict(str, list[str])
        """
        return self._column_data_dependencies

    @column_data_dependencies.setter
    def column_data_dependencies(self, column_data_dependencies):
        """
        Sets the column_data_dependencies of this SchemaLineageDependencyDef.
        Column data-dependencies in format: output_column => list of its input columns

        :param column_data_dependencies: The column_data_dependencies of this SchemaLineageDependencyDef.
        :type: dict(str, list[str])
        """

        self._column_data_dependencies = column_data_dependencies

    @property
    def column_control_dependencies(self):
        """
        Gets the column_control_dependencies of this SchemaLineageDependencyDef.
        Column control-dependencies in format: output_column => list of its input columns

        :return: The column_control_dependencies of this SchemaLineageDependencyDef.
        :rtype: dict(str, list[str])
        """
        return self._column_control_dependencies

    @column_control_dependencies.setter
    def column_control_dependencies(self, column_control_dependencies):
        """
        Sets the column_control_dependencies of this SchemaLineageDependencyDef.
        Column control-dependencies in format: output_column => list of its input columns

        :param column_control_dependencies: The column_control_dependencies of this SchemaLineageDependencyDef.
        :type: dict(str, list[str])
        """

        self._column_control_dependencies = column_control_dependencies

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
        if not isinstance(other, SchemaLineageDependencyDef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other