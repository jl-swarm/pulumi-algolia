# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IndexArgs', 'Index']

@pulumi.input_type
class IndexArgs:
    def __init__(__self__, *,
                 attribute_for_distinct: Optional[pulumi.Input[str]] = None,
                 attributes_for_facetings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 attributes_to_retrieves: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 distinct: Optional[pulumi.Input[int]] = None,
                 hits_per_page: Optional[pulumi.Input[int]] = None,
                 max_values_per_facet: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pagination_limited_to: Optional[pulumi.Input[int]] = None,
                 rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 replicas: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 searchable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sort_facet_values_by: Optional[pulumi.Input[str]] = None,
                 unretrievable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Index resource.
        """
        if attribute_for_distinct is not None:
            pulumi.set(__self__, "attribute_for_distinct", attribute_for_distinct)
        if attributes_for_facetings is not None:
            pulumi.set(__self__, "attributes_for_facetings", attributes_for_facetings)
        if attributes_to_retrieves is not None:
            pulumi.set(__self__, "attributes_to_retrieves", attributes_to_retrieves)
        if custom_rankings is not None:
            pulumi.set(__self__, "custom_rankings", custom_rankings)
        if distinct is not None:
            pulumi.set(__self__, "distinct", distinct)
        if hits_per_page is not None:
            pulumi.set(__self__, "hits_per_page", hits_per_page)
        if max_values_per_facet is not None:
            pulumi.set(__self__, "max_values_per_facet", max_values_per_facet)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pagination_limited_to is not None:
            pulumi.set(__self__, "pagination_limited_to", pagination_limited_to)
        if rankings is not None:
            pulumi.set(__self__, "rankings", rankings)
        if replicas is not None:
            pulumi.set(__self__, "replicas", replicas)
        if searchable_attributes is not None:
            pulumi.set(__self__, "searchable_attributes", searchable_attributes)
        if sort_facet_values_by is not None:
            pulumi.set(__self__, "sort_facet_values_by", sort_facet_values_by)
        if unretrievable_attributes is not None:
            pulumi.set(__self__, "unretrievable_attributes", unretrievable_attributes)

    @property
    @pulumi.getter(name="attributeForDistinct")
    def attribute_for_distinct(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "attribute_for_distinct")

    @attribute_for_distinct.setter
    def attribute_for_distinct(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attribute_for_distinct", value)

    @property
    @pulumi.getter(name="attributesForFacetings")
    def attributes_for_facetings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "attributes_for_facetings")

    @attributes_for_facetings.setter
    def attributes_for_facetings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attributes_for_facetings", value)

    @property
    @pulumi.getter(name="attributesToRetrieves")
    def attributes_to_retrieves(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "attributes_to_retrieves")

    @attributes_to_retrieves.setter
    def attributes_to_retrieves(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attributes_to_retrieves", value)

    @property
    @pulumi.getter(name="customRankings")
    def custom_rankings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_rankings")

    @custom_rankings.setter
    def custom_rankings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_rankings", value)

    @property
    @pulumi.getter
    def distinct(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "distinct")

    @distinct.setter
    def distinct(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "distinct", value)

    @property
    @pulumi.getter(name="hitsPerPage")
    def hits_per_page(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "hits_per_page")

    @hits_per_page.setter
    def hits_per_page(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "hits_per_page", value)

    @property
    @pulumi.getter(name="maxValuesPerFacet")
    def max_values_per_facet(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_values_per_facet")

    @max_values_per_facet.setter
    def max_values_per_facet(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_values_per_facet", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="paginationLimitedTo")
    def pagination_limited_to(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "pagination_limited_to")

    @pagination_limited_to.setter
    def pagination_limited_to(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pagination_limited_to", value)

    @property
    @pulumi.getter
    def rankings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "rankings")

    @rankings.setter
    def rankings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rankings", value)

    @property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "replicas")

    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "replicas", value)

    @property
    @pulumi.getter(name="searchableAttributes")
    def searchable_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "searchable_attributes")

    @searchable_attributes.setter
    def searchable_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "searchable_attributes", value)

    @property
    @pulumi.getter(name="sortFacetValuesBy")
    def sort_facet_values_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sort_facet_values_by")

    @sort_facet_values_by.setter
    def sort_facet_values_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sort_facet_values_by", value)

    @property
    @pulumi.getter(name="unretrievableAttributes")
    def unretrievable_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "unretrievable_attributes")

    @unretrievable_attributes.setter
    def unretrievable_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "unretrievable_attributes", value)


@pulumi.input_type
class _IndexState:
    def __init__(__self__, *,
                 attribute_for_distinct: Optional[pulumi.Input[str]] = None,
                 attributes_for_facetings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 attributes_to_retrieves: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 distinct: Optional[pulumi.Input[int]] = None,
                 hits_per_page: Optional[pulumi.Input[int]] = None,
                 max_values_per_facet: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pagination_limited_to: Optional[pulumi.Input[int]] = None,
                 rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 replicas: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 searchable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sort_facet_values_by: Optional[pulumi.Input[str]] = None,
                 unretrievable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Index resources.
        """
        if attribute_for_distinct is not None:
            pulumi.set(__self__, "attribute_for_distinct", attribute_for_distinct)
        if attributes_for_facetings is not None:
            pulumi.set(__self__, "attributes_for_facetings", attributes_for_facetings)
        if attributes_to_retrieves is not None:
            pulumi.set(__self__, "attributes_to_retrieves", attributes_to_retrieves)
        if custom_rankings is not None:
            pulumi.set(__self__, "custom_rankings", custom_rankings)
        if distinct is not None:
            pulumi.set(__self__, "distinct", distinct)
        if hits_per_page is not None:
            pulumi.set(__self__, "hits_per_page", hits_per_page)
        if max_values_per_facet is not None:
            pulumi.set(__self__, "max_values_per_facet", max_values_per_facet)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pagination_limited_to is not None:
            pulumi.set(__self__, "pagination_limited_to", pagination_limited_to)
        if rankings is not None:
            pulumi.set(__self__, "rankings", rankings)
        if replicas is not None:
            pulumi.set(__self__, "replicas", replicas)
        if searchable_attributes is not None:
            pulumi.set(__self__, "searchable_attributes", searchable_attributes)
        if sort_facet_values_by is not None:
            pulumi.set(__self__, "sort_facet_values_by", sort_facet_values_by)
        if unretrievable_attributes is not None:
            pulumi.set(__self__, "unretrievable_attributes", unretrievable_attributes)

    @property
    @pulumi.getter(name="attributeForDistinct")
    def attribute_for_distinct(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "attribute_for_distinct")

    @attribute_for_distinct.setter
    def attribute_for_distinct(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attribute_for_distinct", value)

    @property
    @pulumi.getter(name="attributesForFacetings")
    def attributes_for_facetings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "attributes_for_facetings")

    @attributes_for_facetings.setter
    def attributes_for_facetings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attributes_for_facetings", value)

    @property
    @pulumi.getter(name="attributesToRetrieves")
    def attributes_to_retrieves(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "attributes_to_retrieves")

    @attributes_to_retrieves.setter
    def attributes_to_retrieves(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attributes_to_retrieves", value)

    @property
    @pulumi.getter(name="customRankings")
    def custom_rankings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "custom_rankings")

    @custom_rankings.setter
    def custom_rankings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_rankings", value)

    @property
    @pulumi.getter
    def distinct(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "distinct")

    @distinct.setter
    def distinct(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "distinct", value)

    @property
    @pulumi.getter(name="hitsPerPage")
    def hits_per_page(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "hits_per_page")

    @hits_per_page.setter
    def hits_per_page(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "hits_per_page", value)

    @property
    @pulumi.getter(name="maxValuesPerFacet")
    def max_values_per_facet(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_values_per_facet")

    @max_values_per_facet.setter
    def max_values_per_facet(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_values_per_facet", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="paginationLimitedTo")
    def pagination_limited_to(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "pagination_limited_to")

    @pagination_limited_to.setter
    def pagination_limited_to(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pagination_limited_to", value)

    @property
    @pulumi.getter
    def rankings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "rankings")

    @rankings.setter
    def rankings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rankings", value)

    @property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "replicas")

    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "replicas", value)

    @property
    @pulumi.getter(name="searchableAttributes")
    def searchable_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "searchable_attributes")

    @searchable_attributes.setter
    def searchable_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "searchable_attributes", value)

    @property
    @pulumi.getter(name="sortFacetValuesBy")
    def sort_facet_values_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sort_facet_values_by")

    @sort_facet_values_by.setter
    def sort_facet_values_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sort_facet_values_by", value)

    @property
    @pulumi.getter(name="unretrievableAttributes")
    def unretrievable_attributes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "unretrievable_attributes")

    @unretrievable_attributes.setter
    def unretrievable_attributes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "unretrievable_attributes", value)


class Index(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_for_distinct: Optional[pulumi.Input[str]] = None,
                 attributes_for_facetings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 attributes_to_retrieves: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 distinct: Optional[pulumi.Input[int]] = None,
                 hits_per_page: Optional[pulumi.Input[int]] = None,
                 max_values_per_facet: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pagination_limited_to: Optional[pulumi.Input[int]] = None,
                 rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 replicas: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 searchable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sort_facet_values_by: Optional[pulumi.Input[str]] = None,
                 unretrievable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Index resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[IndexArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Index resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IndexArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IndexArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attribute_for_distinct: Optional[pulumi.Input[str]] = None,
                 attributes_for_facetings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 attributes_to_retrieves: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 distinct: Optional[pulumi.Input[int]] = None,
                 hits_per_page: Optional[pulumi.Input[int]] = None,
                 max_values_per_facet: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pagination_limited_to: Optional[pulumi.Input[int]] = None,
                 rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 replicas: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 searchable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sort_facet_values_by: Optional[pulumi.Input[str]] = None,
                 unretrievable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IndexArgs.__new__(IndexArgs)

            __props__.__dict__["attribute_for_distinct"] = attribute_for_distinct
            __props__.__dict__["attributes_for_facetings"] = attributes_for_facetings
            __props__.__dict__["attributes_to_retrieves"] = attributes_to_retrieves
            __props__.__dict__["custom_rankings"] = custom_rankings
            __props__.__dict__["distinct"] = distinct
            __props__.__dict__["hits_per_page"] = hits_per_page
            __props__.__dict__["max_values_per_facet"] = max_values_per_facet
            __props__.__dict__["name"] = name
            __props__.__dict__["pagination_limited_to"] = pagination_limited_to
            __props__.__dict__["rankings"] = rankings
            __props__.__dict__["replicas"] = replicas
            __props__.__dict__["searchable_attributes"] = searchable_attributes
            __props__.__dict__["sort_facet_values_by"] = sort_facet_values_by
            __props__.__dict__["unretrievable_attributes"] = unretrievable_attributes
        super(Index, __self__).__init__(
            'algolia:index/index:Index',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            attribute_for_distinct: Optional[pulumi.Input[str]] = None,
            attributes_for_facetings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            attributes_to_retrieves: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom_rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            distinct: Optional[pulumi.Input[int]] = None,
            hits_per_page: Optional[pulumi.Input[int]] = None,
            max_values_per_facet: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            pagination_limited_to: Optional[pulumi.Input[int]] = None,
            rankings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            replicas: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            searchable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            sort_facet_values_by: Optional[pulumi.Input[str]] = None,
            unretrievable_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Index':
        """
        Get an existing Index resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IndexState.__new__(_IndexState)

        __props__.__dict__["attribute_for_distinct"] = attribute_for_distinct
        __props__.__dict__["attributes_for_facetings"] = attributes_for_facetings
        __props__.__dict__["attributes_to_retrieves"] = attributes_to_retrieves
        __props__.__dict__["custom_rankings"] = custom_rankings
        __props__.__dict__["distinct"] = distinct
        __props__.__dict__["hits_per_page"] = hits_per_page
        __props__.__dict__["max_values_per_facet"] = max_values_per_facet
        __props__.__dict__["name"] = name
        __props__.__dict__["pagination_limited_to"] = pagination_limited_to
        __props__.__dict__["rankings"] = rankings
        __props__.__dict__["replicas"] = replicas
        __props__.__dict__["searchable_attributes"] = searchable_attributes
        __props__.__dict__["sort_facet_values_by"] = sort_facet_values_by
        __props__.__dict__["unretrievable_attributes"] = unretrievable_attributes
        return Index(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attributeForDistinct")
    def attribute_for_distinct(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "attribute_for_distinct")

    @property
    @pulumi.getter(name="attributesForFacetings")
    def attributes_for_facetings(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "attributes_for_facetings")

    @property
    @pulumi.getter(name="attributesToRetrieves")
    def attributes_to_retrieves(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "attributes_to_retrieves")

    @property
    @pulumi.getter(name="customRankings")
    def custom_rankings(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "custom_rankings")

    @property
    @pulumi.getter
    def distinct(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "distinct")

    @property
    @pulumi.getter(name="hitsPerPage")
    def hits_per_page(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "hits_per_page")

    @property
    @pulumi.getter(name="maxValuesPerFacet")
    def max_values_per_facet(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_values_per_facet")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="paginationLimitedTo")
    def pagination_limited_to(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "pagination_limited_to")

    @property
    @pulumi.getter
    def rankings(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "rankings")

    @property
    @pulumi.getter
    def replicas(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "replicas")

    @property
    @pulumi.getter(name="searchableAttributes")
    def searchable_attributes(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "searchable_attributes")

    @property
    @pulumi.getter(name="sortFacetValuesBy")
    def sort_facet_values_by(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sort_facet_values_by")

    @property
    @pulumi.getter(name="unretrievableAttributes")
    def unretrievable_attributes(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "unretrievable_attributes")

