# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetAgentResult',
    'AwaitableGetAgentResult',
    'get_agent',
    'get_agent_output',
]

@pulumi.output_type
class GetAgentResult:
    def __init__(__self__, advanced_settings=None, avatar_uri=None, default_language_code=None, description=None, display_name=None, enable_spell_correction=None, enable_stackdriver_logging=None, name=None, security_settings=None, speech_to_text_settings=None, start_flow=None, supported_language_codes=None, time_zone=None):
        if advanced_settings and not isinstance(advanced_settings, dict):
            raise TypeError("Expected argument 'advanced_settings' to be a dict")
        pulumi.set(__self__, "advanced_settings", advanced_settings)
        if avatar_uri and not isinstance(avatar_uri, str):
            raise TypeError("Expected argument 'avatar_uri' to be a str")
        pulumi.set(__self__, "avatar_uri", avatar_uri)
        if default_language_code and not isinstance(default_language_code, str):
            raise TypeError("Expected argument 'default_language_code' to be a str")
        pulumi.set(__self__, "default_language_code", default_language_code)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enable_spell_correction and not isinstance(enable_spell_correction, bool):
            raise TypeError("Expected argument 'enable_spell_correction' to be a bool")
        pulumi.set(__self__, "enable_spell_correction", enable_spell_correction)
        if enable_stackdriver_logging and not isinstance(enable_stackdriver_logging, bool):
            raise TypeError("Expected argument 'enable_stackdriver_logging' to be a bool")
        pulumi.set(__self__, "enable_stackdriver_logging", enable_stackdriver_logging)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if security_settings and not isinstance(security_settings, str):
            raise TypeError("Expected argument 'security_settings' to be a str")
        pulumi.set(__self__, "security_settings", security_settings)
        if speech_to_text_settings and not isinstance(speech_to_text_settings, dict):
            raise TypeError("Expected argument 'speech_to_text_settings' to be a dict")
        pulumi.set(__self__, "speech_to_text_settings", speech_to_text_settings)
        if start_flow and not isinstance(start_flow, str):
            raise TypeError("Expected argument 'start_flow' to be a str")
        pulumi.set(__self__, "start_flow", start_flow)
        if supported_language_codes and not isinstance(supported_language_codes, list):
            raise TypeError("Expected argument 'supported_language_codes' to be a list")
        pulumi.set(__self__, "supported_language_codes", supported_language_codes)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> 'outputs.GoogleCloudDialogflowCxV3AdvancedSettingsResponse':
        """
        Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.
        """
        return pulumi.get(self, "advanced_settings")

    @property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> str:
        """
        The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration.
        """
        return pulumi.get(self, "avatar_uri")

    @property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> str:
        """
        Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method.
        """
        return pulumi.get(self, "default_language_code")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The human-readable name of the agent, unique within the location.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> bool:
        """
        Indicates if automatic spell correction is enabled in detect intent requests.
        """
        return pulumi.get(self, "enable_spell_correction")

    @property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> bool:
        """
        Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead.
        """
        return pulumi.get(self, "enable_stackdriver_logging")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> str:
        """
        Name of the SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`.
        """
        return pulumi.get(self, "security_settings")

    @property
    @pulumi.getter(name="speechToTextSettings")
    def speech_to_text_settings(self) -> 'outputs.GoogleCloudDialogflowCxV3SpeechToTextSettingsResponse':
        """
        Speech recognition related settings.
        """
        return pulumi.get(self, "speech_to_text_settings")

    @property
    @pulumi.getter(name="startFlow")
    def start_flow(self) -> str:
        """
        Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects//locations//agents//flows/`.
        """
        return pulumi.get(self, "start_flow")

    @property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Sequence[str]:
        """
        The list of all languages supported by the agent (except for the `default_language_code`).
        """
        return pulumi.get(self, "supported_language_codes")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.
        """
        return pulumi.get(self, "time_zone")


class AwaitableGetAgentResult(GetAgentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentResult(
            advanced_settings=self.advanced_settings,
            avatar_uri=self.avatar_uri,
            default_language_code=self.default_language_code,
            description=self.description,
            display_name=self.display_name,
            enable_spell_correction=self.enable_spell_correction,
            enable_stackdriver_logging=self.enable_stackdriver_logging,
            name=self.name,
            security_settings=self.security_settings,
            speech_to_text_settings=self.speech_to_text_settings,
            start_flow=self.start_flow,
            supported_language_codes=self.supported_language_codes,
            time_zone=self.time_zone)


def get_agent(agent_id: Optional[str] = None,
              location: Optional[str] = None,
              project: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentResult:
    """
    Retrieves the specified agent.
    """
    __args__ = dict()
    __args__['agentId'] = agent_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dialogflow/v3:getAgent', __args__, opts=opts, typ=GetAgentResult).value

    return AwaitableGetAgentResult(
        advanced_settings=__ret__.advanced_settings,
        avatar_uri=__ret__.avatar_uri,
        default_language_code=__ret__.default_language_code,
        description=__ret__.description,
        display_name=__ret__.display_name,
        enable_spell_correction=__ret__.enable_spell_correction,
        enable_stackdriver_logging=__ret__.enable_stackdriver_logging,
        name=__ret__.name,
        security_settings=__ret__.security_settings,
        speech_to_text_settings=__ret__.speech_to_text_settings,
        start_flow=__ret__.start_flow,
        supported_language_codes=__ret__.supported_language_codes,
        time_zone=__ret__.time_zone)


@_utilities.lift_output_func(get_agent)
def get_agent_output(agent_id: Optional[pulumi.Input[str]] = None,
                     location: Optional[pulumi.Input[str]] = None,
                     project: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentResult]:
    """
    Retrieves the specified agent.
    """
    ...
