# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_odu_odu_node_edge_point_spec import TapiOduOduNodeEdgePointSpec  # noqa: F401,E501
from tapi_server import util


class TapiOduOwnedNodeEdgePointAugmentation1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, odu_node_edge_point_spec=None):  # noqa: E501
        """TapiOduOwnedNodeEdgePointAugmentation1 - a model defined in OpenAPI

        :param odu_node_edge_point_spec: The odu_node_edge_point_spec of this TapiOduOwnedNodeEdgePointAugmentation1.  # noqa: E501
        :type odu_node_edge_point_spec: TapiOduOduNodeEdgePointSpec
        """
        self.openapi_types = {
            'odu_node_edge_point_spec': TapiOduOduNodeEdgePointSpec
        }

        self.attribute_map = {
            'odu_node_edge_point_spec': 'odu-node-edge-point-spec'
        }

        self._odu_node_edge_point_spec = odu_node_edge_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduOwnedNodeEdgePointAugmentation1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.OwnedNodeEdgePointAugmentation1 of this TapiOduOwnedNodeEdgePointAugmentation1.  # noqa: E501
        :rtype: TapiOduOwnedNodeEdgePointAugmentation1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def odu_node_edge_point_spec(self):
        """Gets the odu_node_edge_point_spec of this TapiOduOwnedNodeEdgePointAugmentation1.


        :return: The odu_node_edge_point_spec of this TapiOduOwnedNodeEdgePointAugmentation1.
        :rtype: TapiOduOduNodeEdgePointSpec
        """
        return self._odu_node_edge_point_spec

    @odu_node_edge_point_spec.setter
    def odu_node_edge_point_spec(self, odu_node_edge_point_spec):
        """Sets the odu_node_edge_point_spec of this TapiOduOwnedNodeEdgePointAugmentation1.


        :param odu_node_edge_point_spec: The odu_node_edge_point_spec of this TapiOduOwnedNodeEdgePointAugmentation1.
        :type odu_node_edge_point_spec: TapiOduOduNodeEdgePointSpec
        """

        self._odu_node_edge_point_spec = odu_node_edge_point_spec
