# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AgentArgs', 'Agent']

@pulumi.input_type
class AgentArgs:
    def __init__(__self__, *,
                 default_language_code: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 time_zone: pulumi.Input[str],
                 advanced_settings: Optional[pulumi.Input['GoogleCloudDialogflowCxV3AdvancedSettingsArgs']] = None,
                 avatar_uri: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_spell_correction: Optional[pulumi.Input[bool]] = None,
                 enable_stackdriver_logging: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 security_settings: Optional[pulumi.Input[str]] = None,
                 speech_to_text_settings: Optional[pulumi.Input['GoogleCloudDialogflowCxV3SpeechToTextSettingsArgs']] = None,
                 start_flow: Optional[pulumi.Input[str]] = None,
                 supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Agent resource.
        :param pulumi.Input[str] default_language_code: Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method.
        :param pulumi.Input[str] display_name: The human-readable name of the agent, unique within the location.
        :param pulumi.Input[str] time_zone: The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.
        :param pulumi.Input['GoogleCloudDialogflowCxV3AdvancedSettingsArgs'] advanced_settings: Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.
        :param pulumi.Input[str] avatar_uri: The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration.
        :param pulumi.Input[str] description: The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.
        :param pulumi.Input[bool] enable_spell_correction: Indicates if automatic spell correction is enabled in detect intent requests.
        :param pulumi.Input[bool] enable_stackdriver_logging: Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead.
        :param pulumi.Input[str] name: The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`.
        :param pulumi.Input[str] security_settings: Name of the SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`.
        :param pulumi.Input['GoogleCloudDialogflowCxV3SpeechToTextSettingsArgs'] speech_to_text_settings: Speech recognition related settings.
        :param pulumi.Input[str] start_flow: Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects//locations//agents//flows/`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supported_language_codes: The list of all languages supported by the agent (except for the `default_language_code`).
        """
        pulumi.set(__self__, "default_language_code", default_language_code)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "time_zone", time_zone)
        if advanced_settings is not None:
            pulumi.set(__self__, "advanced_settings", advanced_settings)
        if avatar_uri is not None:
            pulumi.set(__self__, "avatar_uri", avatar_uri)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_spell_correction is not None:
            pulumi.set(__self__, "enable_spell_correction", enable_spell_correction)
        if enable_stackdriver_logging is not None:
            pulumi.set(__self__, "enable_stackdriver_logging", enable_stackdriver_logging)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if security_settings is not None:
            pulumi.set(__self__, "security_settings", security_settings)
        if speech_to_text_settings is not None:
            pulumi.set(__self__, "speech_to_text_settings", speech_to_text_settings)
        if start_flow is not None:
            pulumi.set(__self__, "start_flow", start_flow)
        if supported_language_codes is not None:
            pulumi.set(__self__, "supported_language_codes", supported_language_codes)

    @property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> pulumi.Input[str]:
        """
        Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method.
        """
        return pulumi.get(self, "default_language_code")

    @default_language_code.setter
    def default_language_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_language_code", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The human-readable name of the agent, unique within the location.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[str]:
        """
        The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "time_zone", value)

    @property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input['GoogleCloudDialogflowCxV3AdvancedSettingsArgs']]:
        """
        Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.
        """
        return pulumi.get(self, "advanced_settings")

    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input['GoogleCloudDialogflowCxV3AdvancedSettingsArgs']]):
        pulumi.set(self, "advanced_settings", value)

    @property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration.
        """
        return pulumi.get(self, "avatar_uri")

    @avatar_uri.setter
    def avatar_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "avatar_uri", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if automatic spell correction is enabled in detect intent requests.
        """
        return pulumi.get(self, "enable_spell_correction")

    @enable_spell_correction.setter
    def enable_spell_correction(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_spell_correction", value)

    @property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead.
        """
        return pulumi.get(self, "enable_stackdriver_logging")

    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_stackdriver_logging", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`.
        """
        return pulumi.get(self, "security_settings")

    @security_settings.setter
    def security_settings(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_settings", value)

    @property
    @pulumi.getter(name="speechToTextSettings")
    def speech_to_text_settings(self) -> Optional[pulumi.Input['GoogleCloudDialogflowCxV3SpeechToTextSettingsArgs']]:
        """
        Speech recognition related settings.
        """
        return pulumi.get(self, "speech_to_text_settings")

    @speech_to_text_settings.setter
    def speech_to_text_settings(self, value: Optional[pulumi.Input['GoogleCloudDialogflowCxV3SpeechToTextSettingsArgs']]):
        pulumi.set(self, "speech_to_text_settings", value)

    @property
    @pulumi.getter(name="startFlow")
    def start_flow(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects//locations//agents//flows/`.
        """
        return pulumi.get(self, "start_flow")

    @start_flow.setter
    def start_flow(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_flow", value)

    @property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of all languages supported by the agent (except for the `default_language_code`).
        """
        return pulumi.get(self, "supported_language_codes")

    @supported_language_codes.setter
    def supported_language_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "supported_language_codes", value)


class Agent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3AdvancedSettingsArgs']]] = None,
                 avatar_uri: Optional[pulumi.Input[str]] = None,
                 default_language_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_spell_correction: Optional[pulumi.Input[bool]] = None,
                 enable_stackdriver_logging: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 security_settings: Optional[pulumi.Input[str]] = None,
                 speech_to_text_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3SpeechToTextSettingsArgs']]] = None,
                 start_flow: Optional[pulumi.Input[str]] = None,
                 supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an agent in the specified location. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3AdvancedSettingsArgs']] advanced_settings: Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.
        :param pulumi.Input[str] avatar_uri: The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration.
        :param pulumi.Input[str] default_language_code: Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method.
        :param pulumi.Input[str] description: The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.
        :param pulumi.Input[str] display_name: The human-readable name of the agent, unique within the location.
        :param pulumi.Input[bool] enable_spell_correction: Indicates if automatic spell correction is enabled in detect intent requests.
        :param pulumi.Input[bool] enable_stackdriver_logging: Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead.
        :param pulumi.Input[str] name: The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`.
        :param pulumi.Input[str] security_settings: Name of the SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3SpeechToTextSettingsArgs']] speech_to_text_settings: Speech recognition related settings.
        :param pulumi.Input[str] start_flow: Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects//locations//agents//flows/`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supported_language_codes: The list of all languages supported by the agent (except for the `default_language_code`).
        :param pulumi.Input[str] time_zone: The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an agent in the specified location. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training).

        :param str resource_name: The name of the resource.
        :param AgentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 advanced_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3AdvancedSettingsArgs']]] = None,
                 avatar_uri: Optional[pulumi.Input[str]] = None,
                 default_language_code: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_spell_correction: Optional[pulumi.Input[bool]] = None,
                 enable_stackdriver_logging: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 security_settings: Optional[pulumi.Input[str]] = None,
                 speech_to_text_settings: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3SpeechToTextSettingsArgs']]] = None,
                 start_flow: Optional[pulumi.Input[str]] = None,
                 supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = AgentArgs.__new__(AgentArgs)

            __props__.__dict__["advanced_settings"] = advanced_settings
            __props__.__dict__["avatar_uri"] = avatar_uri
            if default_language_code is None and not opts.urn:
                raise TypeError("Missing required property 'default_language_code'")
            __props__.__dict__["default_language_code"] = default_language_code
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enable_spell_correction"] = enable_spell_correction
            __props__.__dict__["enable_stackdriver_logging"] = enable_stackdriver_logging
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["security_settings"] = security_settings
            __props__.__dict__["speech_to_text_settings"] = speech_to_text_settings
            __props__.__dict__["start_flow"] = start_flow
            __props__.__dict__["supported_language_codes"] = supported_language_codes
            if time_zone is None and not opts.urn:
                raise TypeError("Missing required property 'time_zone'")
            __props__.__dict__["time_zone"] = time_zone
        super(Agent, __self__).__init__(
            'google-native:dialogflow/v3:Agent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Agent':
        """
        Get an existing Agent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgentArgs.__new__(AgentArgs)

        __props__.__dict__["advanced_settings"] = None
        __props__.__dict__["avatar_uri"] = None
        __props__.__dict__["default_language_code"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enable_spell_correction"] = None
        __props__.__dict__["enable_stackdriver_logging"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["security_settings"] = None
        __props__.__dict__["speech_to_text_settings"] = None
        __props__.__dict__["start_flow"] = None
        __props__.__dict__["supported_language_codes"] = None
        __props__.__dict__["time_zone"] = None
        return Agent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3AdvancedSettingsResponse']:
        """
        Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.
        """
        return pulumi.get(self, "advanced_settings")

    @property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> pulumi.Output[str]:
        """
        The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration.
        """
        return pulumi.get(self, "avatar_uri")

    @property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> pulumi.Output[str]:
        """
        Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method.
        """
        return pulumi.get(self, "default_language_code")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The human-readable name of the agent, unique within the location.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> pulumi.Output[bool]:
        """
        Indicates if automatic spell correction is enabled in detect intent requests.
        """
        return pulumi.get(self, "enable_spell_correction")

    @property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> pulumi.Output[bool]:
        """
        Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead.
        """
        return pulumi.get(self, "enable_stackdriver_logging")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Output[str]:
        """
        Name of the SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`.
        """
        return pulumi.get(self, "security_settings")

    @property
    @pulumi.getter(name="speechToTextSettings")
    def speech_to_text_settings(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3SpeechToTextSettingsResponse']:
        """
        Speech recognition related settings.
        """
        return pulumi.get(self, "speech_to_text_settings")

    @property
    @pulumi.getter(name="startFlow")
    def start_flow(self) -> pulumi.Output[str]:
        """
        Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects//locations//agents//flows/`.
        """
        return pulumi.get(self, "start_flow")

    @property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of all languages supported by the agent (except for the `default_language_code`).
        """
        return pulumi.get(self, "supported_language_codes")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[str]:
        """
        The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.
        """
        return pulumi.get(self, "time_zone")

