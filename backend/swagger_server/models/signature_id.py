# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from .base_model_ import Model
from .. import util


class SignatureID(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, status: str=None, title: str=None, timestamp: str=None):  # noqa: E501
        """SignatureID - a model defined in Swagger

        :param id: The id of this SignatureID.  # noqa: E501
        :type id: str
        :param status: The status of this SignatureID.  # noqa: E501
        :type status: str
        :param title: The title of this SignatureID.  # noqa: E501
        :type title: str
        :param timestamp: The timestamp of this SignatureID.  # noqa: E501
        :type timestamp: str
        """
        self.swagger_types = {
            'id': str,
            'status': str,
            'title': str,
            'timestamp': str
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'title': 'title',
            'timestamp': 'timestamp'
        }

        self._id = id
        self._status = status
        self._title = title
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'SignatureID':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SignatureID of this SignatureID.  # noqa: E501
        :rtype: SignatureID
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this SignatureID.

        The signature ID  # noqa: E501

        :return: The id of this SignatureID.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SignatureID.

        The signature ID  # noqa: E501

        :param id: The id of this SignatureID.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self) -> str:
        """Gets the status of this SignatureID.

        A keyword describing the current state of the signature.  # noqa: E501

        :return: The status of this SignatureID.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this SignatureID.

        A keyword describing the current state of the signature.  # noqa: E501

        :param status: The status of this SignatureID.
        :type status: str
        """
        allowed_values = ["empty", "filled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self) -> str:
        """Gets the title of this SignatureID.

        The title of the document.  # noqa: E501

        :return: The title of this SignatureID.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this SignatureID.

        The title of the document.  # noqa: E501

        :param title: The title of this SignatureID.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this SignatureID.

        The timestamp of the last modification to the document.  # noqa: E501

        :return: The timestamp of this SignatureID.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this SignatureID.

        The timestamp of the last modification to the document.  # noqa: E501

        :param timestamp: The timestamp of this SignatureID.
        :type timestamp: str
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp
