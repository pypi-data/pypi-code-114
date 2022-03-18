# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import transponder_pb2 as transponder_dot_transponder__pb2


class TransponderServiceStub(object):
    """
    Allow users to get ADS-B information
    and set ADS-B update rates.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeTransponder = channel.unary_stream(
                '/mavsdk.rpc.transponder.TransponderService/SubscribeTransponder',
                request_serializer=transponder_dot_transponder__pb2.SubscribeTransponderRequest.SerializeToString,
                response_deserializer=transponder_dot_transponder__pb2.TransponderResponse.FromString,
                )
        self.SetRateTransponder = channel.unary_unary(
                '/mavsdk.rpc.transponder.TransponderService/SetRateTransponder',
                request_serializer=transponder_dot_transponder__pb2.SetRateTransponderRequest.SerializeToString,
                response_deserializer=transponder_dot_transponder__pb2.SetRateTransponderResponse.FromString,
                )


class TransponderServiceServicer(object):
    """
    Allow users to get ADS-B information
    and set ADS-B update rates.
    """

    def SubscribeTransponder(self, request, context):
        """Subscribe to 'transponder' updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRateTransponder(self, request, context):
        """Set rate to 'transponder' updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransponderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeTransponder': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeTransponder,
                    request_deserializer=transponder_dot_transponder__pb2.SubscribeTransponderRequest.FromString,
                    response_serializer=transponder_dot_transponder__pb2.TransponderResponse.SerializeToString,
            ),
            'SetRateTransponder': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRateTransponder,
                    request_deserializer=transponder_dot_transponder__pb2.SetRateTransponderRequest.FromString,
                    response_serializer=transponder_dot_transponder__pb2.SetRateTransponderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.transponder.TransponderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransponderService(object):
    """
    Allow users to get ADS-B information
    and set ADS-B update rates.
    """

    @staticmethod
    def SubscribeTransponder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mavsdk.rpc.transponder.TransponderService/SubscribeTransponder',
            transponder_dot_transponder__pb2.SubscribeTransponderRequest.SerializeToString,
            transponder_dot_transponder__pb2.TransponderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetRateTransponder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.transponder.TransponderService/SetRateTransponder',
            transponder_dot_transponder__pb2.SetRateTransponderRequest.SerializeToString,
            transponder_dot_transponder__pb2.SetRateTransponderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
