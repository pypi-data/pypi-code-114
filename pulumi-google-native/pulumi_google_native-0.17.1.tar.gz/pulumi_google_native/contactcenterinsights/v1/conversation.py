# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ConversationArgs', 'Conversation']

@pulumi.input_type
class ConversationArgs:
    def __init__(__self__, *,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 call_metadata: Optional[pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationCallMetadataArgs']] = None,
                 conversation_id: Optional[pulumi.Input[str]] = None,
                 data_source: Optional[pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationDataSourceArgs']] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 medium: Optional[pulumi.Input['ConversationMedium']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 obfuscated_user_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Conversation resource.
        :param pulumi.Input[str] agent_id: An opaque, user-specified string representing the human agent who handled the conversation.
        :param pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationCallMetadataArgs'] call_metadata: Call-specific metadata.
        :param pulumi.Input[str] conversation_id: A unique ID for the new conversation. This ID will become the final component of the conversation's resource name. If no ID is specified, a server-generated ID will be used. This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `a-z-`
        :param pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationDataSourceArgs'] data_source: The source of the audio and transcription for the conversation.
        :param pulumi.Input[str] expire_time: The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry.
        :param pulumi.Input[str] language_code: A user-specified language code for the conversation.
        :param pulumi.Input['ConversationMedium'] medium: Immutable. The conversation medium, if unspecified will default to PHONE_CALL.
        :param pulumi.Input[str] name: Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation}
        :param pulumi.Input[str] obfuscated_user_id: Obfuscated user ID which the customer sent to us.
        :param pulumi.Input[str] start_time: The time at which the conversation started.
        :param pulumi.Input[str] ttl: Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time.
        """
        if agent_id is not None:
            pulumi.set(__self__, "agent_id", agent_id)
        if call_metadata is not None:
            pulumi.set(__self__, "call_metadata", call_metadata)
        if conversation_id is not None:
            pulumi.set(__self__, "conversation_id", conversation_id)
        if data_source is not None:
            pulumi.set(__self__, "data_source", data_source)
        if expire_time is not None:
            pulumi.set(__self__, "expire_time", expire_time)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if medium is not None:
            pulumi.set(__self__, "medium", medium)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if obfuscated_user_id is not None:
            pulumi.set(__self__, "obfuscated_user_id", obfuscated_user_id)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[str]]:
        """
        An opaque, user-specified string representing the human agent who handled the conversation.
        """
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="callMetadata")
    def call_metadata(self) -> Optional[pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationCallMetadataArgs']]:
        """
        Call-specific metadata.
        """
        return pulumi.get(self, "call_metadata")

    @call_metadata.setter
    def call_metadata(self, value: Optional[pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationCallMetadataArgs']]):
        pulumi.set(self, "call_metadata", value)

    @property
    @pulumi.getter(name="conversationId")
    def conversation_id(self) -> Optional[pulumi.Input[str]]:
        """
        A unique ID for the new conversation. This ID will become the final component of the conversation's resource name. If no ID is specified, a server-generated ID will be used. This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `a-z-`
        """
        return pulumi.get(self, "conversation_id")

    @conversation_id.setter
    def conversation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "conversation_id", value)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationDataSourceArgs']]:
        """
        The source of the audio and transcription for the conversation.
        """
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input['GoogleCloudContactcenterinsightsV1ConversationDataSourceArgs']]):
        pulumi.set(self, "data_source", value)

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted.
        """
        return pulumi.get(self, "expire_time")

    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expire_time", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[str]]:
        """
        A user-specified language code for the conversation.
        """
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input['ConversationMedium']]:
        """
        Immutable. The conversation medium, if unspecified will default to PHONE_CALL.
        """
        return pulumi.get(self, "medium")

    @medium.setter
    def medium(self, value: Optional[pulumi.Input['ConversationMedium']]):
        pulumi.set(self, "medium", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation}
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="obfuscatedUserId")
    def obfuscated_user_id(self) -> Optional[pulumi.Input[str]]:
        """
        Obfuscated user ID which the customer sent to us.
        """
        return pulumi.get(self, "obfuscated_user_id")

    @obfuscated_user_id.setter
    def obfuscated_user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "obfuscated_user_id", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time at which the conversation started.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[str]]:
        """
        Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ttl", value)


class Conversation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 call_metadata: Optional[pulumi.Input[pulumi.InputType['GoogleCloudContactcenterinsightsV1ConversationCallMetadataArgs']]] = None,
                 conversation_id: Optional[pulumi.Input[str]] = None,
                 data_source: Optional[pulumi.Input[pulumi.InputType['GoogleCloudContactcenterinsightsV1ConversationDataSourceArgs']]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 medium: Optional[pulumi.Input['ConversationMedium']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 obfuscated_user_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a conversation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_id: An opaque, user-specified string representing the human agent who handled the conversation.
        :param pulumi.Input[pulumi.InputType['GoogleCloudContactcenterinsightsV1ConversationCallMetadataArgs']] call_metadata: Call-specific metadata.
        :param pulumi.Input[str] conversation_id: A unique ID for the new conversation. This ID will become the final component of the conversation's resource name. If no ID is specified, a server-generated ID will be used. This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `a-z-`
        :param pulumi.Input[pulumi.InputType['GoogleCloudContactcenterinsightsV1ConversationDataSourceArgs']] data_source: The source of the audio and transcription for the conversation.
        :param pulumi.Input[str] expire_time: The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry.
        :param pulumi.Input[str] language_code: A user-specified language code for the conversation.
        :param pulumi.Input['ConversationMedium'] medium: Immutable. The conversation medium, if unspecified will default to PHONE_CALL.
        :param pulumi.Input[str] name: Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation}
        :param pulumi.Input[str] obfuscated_user_id: Obfuscated user ID which the customer sent to us.
        :param pulumi.Input[str] start_time: The time at which the conversation started.
        :param pulumi.Input[str] ttl: Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ConversationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a conversation.

        :param str resource_name: The name of the resource.
        :param ConversationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConversationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 call_metadata: Optional[pulumi.Input[pulumi.InputType['GoogleCloudContactcenterinsightsV1ConversationCallMetadataArgs']]] = None,
                 conversation_id: Optional[pulumi.Input[str]] = None,
                 data_source: Optional[pulumi.Input[pulumi.InputType['GoogleCloudContactcenterinsightsV1ConversationDataSourceArgs']]] = None,
                 expire_time: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 medium: Optional[pulumi.Input['ConversationMedium']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 obfuscated_user_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConversationArgs.__new__(ConversationArgs)

            __props__.__dict__["agent_id"] = agent_id
            __props__.__dict__["call_metadata"] = call_metadata
            __props__.__dict__["conversation_id"] = conversation_id
            __props__.__dict__["data_source"] = data_source
            __props__.__dict__["expire_time"] = expire_time
            __props__.__dict__["labels"] = labels
            __props__.__dict__["language_code"] = language_code
            __props__.__dict__["location"] = location
            __props__.__dict__["medium"] = medium
            __props__.__dict__["name"] = name
            __props__.__dict__["obfuscated_user_id"] = obfuscated_user_id
            __props__.__dict__["project"] = project
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["create_time"] = None
            __props__.__dict__["dialogflow_intents"] = None
            __props__.__dict__["duration"] = None
            __props__.__dict__["latest_analysis"] = None
            __props__.__dict__["runtime_annotations"] = None
            __props__.__dict__["transcript"] = None
            __props__.__dict__["turn_count"] = None
            __props__.__dict__["update_time"] = None
        super(Conversation, __self__).__init__(
            'google-native:contactcenterinsights/v1:Conversation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Conversation':
        """
        Get an existing Conversation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConversationArgs.__new__(ConversationArgs)

        __props__.__dict__["agent_id"] = None
        __props__.__dict__["call_metadata"] = None
        __props__.__dict__["create_time"] = None
        __props__.__dict__["data_source"] = None
        __props__.__dict__["dialogflow_intents"] = None
        __props__.__dict__["duration"] = None
        __props__.__dict__["expire_time"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["language_code"] = None
        __props__.__dict__["latest_analysis"] = None
        __props__.__dict__["medium"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["obfuscated_user_id"] = None
        __props__.__dict__["runtime_annotations"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["transcript"] = None
        __props__.__dict__["ttl"] = None
        __props__.__dict__["turn_count"] = None
        __props__.__dict__["update_time"] = None
        return Conversation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[str]:
        """
        An opaque, user-specified string representing the human agent who handled the conversation.
        """
        return pulumi.get(self, "agent_id")

    @property
    @pulumi.getter(name="callMetadata")
    def call_metadata(self) -> pulumi.Output['outputs.GoogleCloudContactcenterinsightsV1ConversationCallMetadataResponse']:
        """
        Call-specific metadata.
        """
        return pulumi.get(self, "call_metadata")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time at which the conversation was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> pulumi.Output['outputs.GoogleCloudContactcenterinsightsV1ConversationDataSourceResponse']:
        """
        The source of the audio and transcription for the conversation.
        """
        return pulumi.get(self, "data_source")

    @property
    @pulumi.getter(name="dialogflowIntents")
    def dialogflow_intents(self) -> pulumi.Output[Mapping[str, str]]:
        """
        All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/{project}/agent/{agent}/intents/{intent}
        """
        return pulumi.get(self, "dialogflow_intents")

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Output[str]:
        """
        The duration of the conversation.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[str]:
        """
        The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted.
        """
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[str]:
        """
        A user-specified language code for the conversation.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter(name="latestAnalysis")
    def latest_analysis(self) -> pulumi.Output['outputs.GoogleCloudContactcenterinsightsV1AnalysisResponse']:
        """
        The conversation's latest analysis, if one exists.
        """
        return pulumi.get(self, "latest_analysis")

    @property
    @pulumi.getter
    def medium(self) -> pulumi.Output[str]:
        """
        Immutable. The conversation medium, if unspecified will default to PHONE_CALL.
        """
        return pulumi.get(self, "medium")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="obfuscatedUserId")
    def obfuscated_user_id(self) -> pulumi.Output[str]:
        """
        Obfuscated user ID which the customer sent to us.
        """
        return pulumi.get(self, "obfuscated_user_id")

    @property
    @pulumi.getter(name="runtimeAnnotations")
    def runtime_annotations(self) -> pulumi.Output[Sequence['outputs.GoogleCloudContactcenterinsightsV1RuntimeAnnotationResponse']]:
        """
        The annotations that were generated during the customer and agent interaction.
        """
        return pulumi.get(self, "runtime_annotations")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        The time at which the conversation started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def transcript(self) -> pulumi.Output['outputs.GoogleCloudContactcenterinsightsV1ConversationTranscriptResponse']:
        """
        The conversation transcript.
        """
        return pulumi.get(self, "transcript")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[str]:
        """
        Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="turnCount")
    def turn_count(self) -> pulumi.Output[int]:
        """
        The number of turns in the conversation.
        """
        return pulumi.get(self, "turn_count")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The most recent time at which the conversation was updated.
        """
        return pulumi.get(self, "update_time")

