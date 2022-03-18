# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import action_server_pb2 as action__server_dot_action__server__pb2


class ActionServerServiceStub(object):
    """Provide vehicle actions (as a server) such as arming, taking off, and landing.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeArmDisarm = channel.unary_stream(
                '/mavsdk.rpc.action_server.ActionServerService/SubscribeArmDisarm',
                request_serializer=action__server_dot_action__server__pb2.SubscribeArmDisarmRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.ArmDisarmResponse.FromString,
                )
        self.SubscribeFlightModeChange = channel.unary_stream(
                '/mavsdk.rpc.action_server.ActionServerService/SubscribeFlightModeChange',
                request_serializer=action__server_dot_action__server__pb2.SubscribeFlightModeChangeRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.FlightModeChangeResponse.FromString,
                )
        self.SubscribeTakeoff = channel.unary_stream(
                '/mavsdk.rpc.action_server.ActionServerService/SubscribeTakeoff',
                request_serializer=action__server_dot_action__server__pb2.SubscribeTakeoffRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.TakeoffResponse.FromString,
                )
        self.SubscribeLand = channel.unary_stream(
                '/mavsdk.rpc.action_server.ActionServerService/SubscribeLand',
                request_serializer=action__server_dot_action__server__pb2.SubscribeLandRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.LandResponse.FromString,
                )
        self.SubscribeReboot = channel.unary_stream(
                '/mavsdk.rpc.action_server.ActionServerService/SubscribeReboot',
                request_serializer=action__server_dot_action__server__pb2.SubscribeRebootRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.RebootResponse.FromString,
                )
        self.SubscribeShutdown = channel.unary_stream(
                '/mavsdk.rpc.action_server.ActionServerService/SubscribeShutdown',
                request_serializer=action__server_dot_action__server__pb2.SubscribeShutdownRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.ShutdownResponse.FromString,
                )
        self.SubscribeTerminate = channel.unary_stream(
                '/mavsdk.rpc.action_server.ActionServerService/SubscribeTerminate',
                request_serializer=action__server_dot_action__server__pb2.SubscribeTerminateRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.TerminateResponse.FromString,
                )
        self.SetAllowTakeoff = channel.unary_unary(
                '/mavsdk.rpc.action_server.ActionServerService/SetAllowTakeoff',
                request_serializer=action__server_dot_action__server__pb2.SetAllowTakeoffRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.SetAllowTakeoffResponse.FromString,
                )
        self.SetArmable = channel.unary_unary(
                '/mavsdk.rpc.action_server.ActionServerService/SetArmable',
                request_serializer=action__server_dot_action__server__pb2.SetArmableRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.SetArmableResponse.FromString,
                )
        self.SetDisarmable = channel.unary_unary(
                '/mavsdk.rpc.action_server.ActionServerService/SetDisarmable',
                request_serializer=action__server_dot_action__server__pb2.SetDisarmableRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.SetDisarmableResponse.FromString,
                )
        self.SetAllowableFlightModes = channel.unary_unary(
                '/mavsdk.rpc.action_server.ActionServerService/SetAllowableFlightModes',
                request_serializer=action__server_dot_action__server__pb2.SetAllowableFlightModesRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.SetAllowableFlightModesResponse.FromString,
                )
        self.GetAllowableFlightModes = channel.unary_unary(
                '/mavsdk.rpc.action_server.ActionServerService/GetAllowableFlightModes',
                request_serializer=action__server_dot_action__server__pb2.GetAllowableFlightModesRequest.SerializeToString,
                response_deserializer=action__server_dot_action__server__pb2.GetAllowableFlightModesResponse.FromString,
                )


class ActionServerServiceServicer(object):
    """Provide vehicle actions (as a server) such as arming, taking off, and landing.
    """

    def SubscribeArmDisarm(self, request, context):
        """Subscribe to ARM/DISARM commands
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeFlightModeChange(self, request, context):
        """Subscribe to DO_SET_MODE
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeTakeoff(self, request, context):
        """Subscribe to takeoff command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeLand(self, request, context):
        """Subscribe to land command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeReboot(self, request, context):
        """Subscribe to reboot command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeShutdown(self, request, context):
        """Subscribe to shutdown command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeTerminate(self, request, context):
        """Subscribe to terminate command
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAllowTakeoff(self, request, context):
        """Can the vehicle takeoff
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetArmable(self, request, context):
        """Can the vehicle arm when requested
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDisarmable(self, request, context):
        """Can the vehicle disarm when requested
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAllowableFlightModes(self, request, context):
        """Set which modes the vehicle can transition to (Manual always allowed)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllowableFlightModes(self, request, context):
        """Get which modes the vehicle can transition to (Manual always allowed)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ActionServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeArmDisarm': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeArmDisarm,
                    request_deserializer=action__server_dot_action__server__pb2.SubscribeArmDisarmRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.ArmDisarmResponse.SerializeToString,
            ),
            'SubscribeFlightModeChange': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeFlightModeChange,
                    request_deserializer=action__server_dot_action__server__pb2.SubscribeFlightModeChangeRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.FlightModeChangeResponse.SerializeToString,
            ),
            'SubscribeTakeoff': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeTakeoff,
                    request_deserializer=action__server_dot_action__server__pb2.SubscribeTakeoffRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.TakeoffResponse.SerializeToString,
            ),
            'SubscribeLand': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeLand,
                    request_deserializer=action__server_dot_action__server__pb2.SubscribeLandRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.LandResponse.SerializeToString,
            ),
            'SubscribeReboot': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeReboot,
                    request_deserializer=action__server_dot_action__server__pb2.SubscribeRebootRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.RebootResponse.SerializeToString,
            ),
            'SubscribeShutdown': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeShutdown,
                    request_deserializer=action__server_dot_action__server__pb2.SubscribeShutdownRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.ShutdownResponse.SerializeToString,
            ),
            'SubscribeTerminate': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeTerminate,
                    request_deserializer=action__server_dot_action__server__pb2.SubscribeTerminateRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.TerminateResponse.SerializeToString,
            ),
            'SetAllowTakeoff': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAllowTakeoff,
                    request_deserializer=action__server_dot_action__server__pb2.SetAllowTakeoffRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.SetAllowTakeoffResponse.SerializeToString,
            ),
            'SetArmable': grpc.unary_unary_rpc_method_handler(
                    servicer.SetArmable,
                    request_deserializer=action__server_dot_action__server__pb2.SetArmableRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.SetArmableResponse.SerializeToString,
            ),
            'SetDisarmable': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDisarmable,
                    request_deserializer=action__server_dot_action__server__pb2.SetDisarmableRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.SetDisarmableResponse.SerializeToString,
            ),
            'SetAllowableFlightModes': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAllowableFlightModes,
                    request_deserializer=action__server_dot_action__server__pb2.SetAllowableFlightModesRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.SetAllowableFlightModesResponse.SerializeToString,
            ),
            'GetAllowableFlightModes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllowableFlightModes,
                    request_deserializer=action__server_dot_action__server__pb2.GetAllowableFlightModesRequest.FromString,
                    response_serializer=action__server_dot_action__server__pb2.GetAllowableFlightModesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.action_server.ActionServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ActionServerService(object):
    """Provide vehicle actions (as a server) such as arming, taking off, and landing.
    """

    @staticmethod
    def SubscribeArmDisarm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.action_server.ActionServerService/SubscribeArmDisarm',
            action__server_dot_action__server__pb2.SubscribeArmDisarmRequest.SerializeToString,
            action__server_dot_action__server__pb2.ArmDisarmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeFlightModeChange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.action_server.ActionServerService/SubscribeFlightModeChange',
            action__server_dot_action__server__pb2.SubscribeFlightModeChangeRequest.SerializeToString,
            action__server_dot_action__server__pb2.FlightModeChangeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeTakeoff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.action_server.ActionServerService/SubscribeTakeoff',
            action__server_dot_action__server__pb2.SubscribeTakeoffRequest.SerializeToString,
            action__server_dot_action__server__pb2.TakeoffResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeLand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.action_server.ActionServerService/SubscribeLand',
            action__server_dot_action__server__pb2.SubscribeLandRequest.SerializeToString,
            action__server_dot_action__server__pb2.LandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeReboot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.action_server.ActionServerService/SubscribeReboot',
            action__server_dot_action__server__pb2.SubscribeRebootRequest.SerializeToString,
            action__server_dot_action__server__pb2.RebootResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeShutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.action_server.ActionServerService/SubscribeShutdown',
            action__server_dot_action__server__pb2.SubscribeShutdownRequest.SerializeToString,
            action__server_dot_action__server__pb2.ShutdownResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeTerminate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.action_server.ActionServerService/SubscribeTerminate',
            action__server_dot_action__server__pb2.SubscribeTerminateRequest.SerializeToString,
            action__server_dot_action__server__pb2.TerminateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAllowTakeoff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action_server.ActionServerService/SetAllowTakeoff',
            action__server_dot_action__server__pb2.SetAllowTakeoffRequest.SerializeToString,
            action__server_dot_action__server__pb2.SetAllowTakeoffResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetArmable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action_server.ActionServerService/SetArmable',
            action__server_dot_action__server__pb2.SetArmableRequest.SerializeToString,
            action__server_dot_action__server__pb2.SetArmableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDisarmable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action_server.ActionServerService/SetDisarmable',
            action__server_dot_action__server__pb2.SetDisarmableRequest.SerializeToString,
            action__server_dot_action__server__pb2.SetDisarmableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAllowableFlightModes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action_server.ActionServerService/SetAllowableFlightModes',
            action__server_dot_action__server__pb2.SetAllowableFlightModesRequest.SerializeToString,
            action__server_dot_action__server__pb2.SetAllowableFlightModesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllowableFlightModes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action_server.ActionServerService/GetAllowableFlightModes',
            action__server_dot_action__server__pb2.GetAllowableFlightModesRequest.SerializeToString,
            action__server_dot_action__server__pb2.GetAllowableFlightModesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
