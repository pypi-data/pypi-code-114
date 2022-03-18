from d3m_interface import AutoML as BaseAutoML


class AutoMLContainer(BaseAutoML):

    def __init__(self, output_folder, container_runtime='docker', grpc_port=None, verbose=False):
        """Create/instantiate an AutoMLContainer object

        :param output_folder: Path to the output directory
        :param container_runtime: The container runtime to use, can be 'docker' or 'singularity'
        :param grpc_port: Port to be used by GRPC
        :param verbose: Whether or not to show all the logs from AutoML systems
        """

        automl_id = 'AlphaD3M'
        BaseAutoML.__init__(self, output_folder, automl_id, container_runtime, grpc_port, verbose)
