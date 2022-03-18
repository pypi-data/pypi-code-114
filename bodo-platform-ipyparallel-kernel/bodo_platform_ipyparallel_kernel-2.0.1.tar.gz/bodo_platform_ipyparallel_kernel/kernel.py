from ipykernel.ipkernel import IPythonKernel
import ipyparallel as ipp
from .platform_hostfile_update import update_hostfile

IPYPARALLEL_LINE_MAGICS = ("px", "autopx", "pxconfig", "pxresult")
IPYPARALLEL_CELL_MAGICS = ("px",)
IPYPARALLEL_MAGICS = tuple(
    [f"%{m}" for m in IPYPARALLEL_LINE_MAGICS]
    + [f"%%{m}" for m in IPYPARALLEL_CELL_MAGICS]
)


class IPyParallelKernel(IPythonKernel):
    banner = "IPyParallel Kernel"

    def start(self):
        super().start()
        self.ipyparallel_cluster_started = False
        self.ipyparallel_cluster = None

    def ipyparallel_magics_already_registered(self):
        # Check if any IPyParallel magics are already registered
        return any(
            [
                x in self.shell.magics_manager.magics["line"]
                for x in IPYPARALLEL_LINE_MAGICS
            ]
            + [
                x in self.shell.magics_manager.magics["cell"]
                for x in IPYPARALLEL_CELL_MAGICS
            ]
        )

    def start_ipyparallel_cluster(self):
        if not self.ipyparallel_cluster_started:
            self.log.info("Updaing Hostfile...")
            update_hostfile(self.log)
            self.log.info("Starting IPyParallel Cluster...")
            try:
                self.ipyparallel_cluster = (
                    ipp.Cluster()
                )  # Config is taken from ipcluster_config.py
                self.ipyparallel_rc = self.ipyparallel_cluster.start_and_connect_sync()
                self.ipyparallel_view = self.ipyparallel_rc.broadcast_view()
                self.ipyparallel_view.block = True
                self.ipyparallel_view.activate()
            except Exception as e:
                self.log.error(
                    "Something went wrong while trying to start the IPyParallel cluster..."
                )
                self.log.error(f"Error: {e}")
                self.log.info("Shutting Cluster down...")
                # Cluster might have been started, if so then stop it and remove any
                # lingering processes
                if self.ipyparallel_cluster is not None:
                    self.ipyparallel_cluster.stop_cluster_sync()
            else:
                self.ipyparallel_cluster_started = True

    async def do_execute(
        self,
        code: str,
        silent,
        store_history=True,
        user_expressions=None,
        allow_stdin=False,
    ):
        # Start the IPyParallel cluster if any IPyParallel
        # magic is used
        if (
            code.startswith(IPYPARALLEL_MAGICS)
            # If magics are already registered, that means user has started an
            # IPyParallel cluster manually, so we shouldn't start one ourselves.
            # This lets users use this kernel as a direct replacement for a regular
            # kernel.
            and not self.ipyparallel_magics_already_registered()
        ):
            self.start_ipyparallel_cluster()
        return await super().do_execute(
            code=code,
            silent=silent,
            store_history=store_history,
            user_expressions=user_expressions,
            allow_stdin=allow_stdin,
        )

    def stop_ipyparallel_cluster(self):
        if self.ipyparallel_cluster_started:
            self.log.info("Stopping IPyParallel Cluster...")
            self.ipyparallel_cluster.stop_cluster_sync()

    def do_shutdown(self, restart):
        self.stop_ipyparallel_cluster()
        return super().do_shutdown(restart)
