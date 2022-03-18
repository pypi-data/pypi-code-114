from __future__ import annotations

from collections import Counter
from textwrap import dedent
from types import TracebackType
from typing import Any, Iterable, Mapping, Type

import jmespath
import rich
import rich.align
import rich.console
import rich.layout
import rich.live
import rich.panel
import rich.progress

from ...errors import ClusterCreationError
from ..states import CombinedProcessStateEnum, ProcessStateEnum
from .util import get_instance_types, get_worker_statuses


class RichClusterWidget:
    """A Rich renderable showing cluster status."""

    n_workers: int
    _cluster_details: Mapping[str, Any] | None
    _progress: rich.progress.Progress

    def __init__(
        self,
        n_workers: int = 0,
        transient: bool = False,
        console: rich.console.Console | None = None,
    ):
        """Set up the renderable widget."""
        self._cluster_details = None

        if console:
            self.console = console
        else:
            self.console = rich.console.Console()
            self.console.size = (100, 26)

        self._progress = progress = rich.progress.Progress(
            "{task.description}",
            rich.progress.BarColumn(),
            rich.progress.TextColumn("[progress.percentage]{task.completed}"),
        )
        self._provision_task = progress.add_task("Provisioning", total=n_workers)
        self._boot_task = progress.add_task("Booting Instance", total=n_workers)
        self._downloading_extracting_task = progress.add_task(
            "Launching Software Environment", total=n_workers
        )
        self._ready_task = progress.add_task("Ready", total=n_workers)
        self._error_task = progress.add_task("Errored", total=n_workers)
        self._stopping_task = progress.add_task("Stopping", total=n_workers)
        self._stopped_task = progress.add_task("Stopped", total=n_workers)

        # Calls _get_renderable, so the progress bar must be set up first.
        self.live = rich.live.Live(
            transient=transient,
            console=self.console,
            get_renderable=self._get_renderable,
        )

    def start(self):
        """Start the live instance."""
        self.live.start(refresh=False)

    def stop(self):
        """Stop the live instance."""
        self.live.stop()

    def __enter__(self) -> RichClusterWidget:
        """Enter a live-updating context.

        Example
        -------
        with RichClusterWidget(n_workers) as w:
            # do stuff
        """
        self.start()
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Exit the live-updating context and reset the display ID.

        Keep the widget around for user inspection if there was a cluster creation
        error, otherwise remove it.
        """
        if exc_type == ClusterCreationError and self.live.transient:
            self.live.transient = False
        self.stop()

    def update(self, cluster_details: Mapping[str, Any], *args, **kwargs) -> None:
        """Update cluster data.

        Note: this does not trigger any refreshing, that is handled by the Live
        instance, which does it periodically.
        """
        self._cluster_details = cluster_details

        # We explicitly refresh to make sure updated info is shown.
        # (Bad timing can lead auto-refresh to not show the update before we stop.)
        self.live.refresh()

    def _ipython_display_(self) -> None:
        """Render in a notebook context.

        Note: this is *not* called in an IPython terminal context. Instead,
        _repr_mimebundle_ is used in the IPython terminal.
        """
        self.console.print(self._get_renderable(), new_line_start=True)

    def __rich_console__(
        self, console: rich.console.Console, options: rich.console.ConsoleOptions
    ) -> rich.console.RenderResult:
        """Implement the Rich console interface.

        In particular, this is used in ``_repr_mimebundle_`` to display to an IPython
        terminal.
        """
        yield self._get_renderable()

    def _repr_mimebundle_(
        self, include: Iterable[str], exclude: Iterable[str], **kwargs
    ) -> dict[str, str]:
        """Display the widget in an IPython console context.

        This is adapted from the code in `rich.jupyter.JupyterMixin`. We can't
        use that mixin because it doesn't allow you to specify your own console
        (instead using the global one). We want our own console because we
        manually set the size to not take up the full terminal.
        """
        console = self.console
        segments = list(console.render(self, console.options))  # type: ignore
        text = console._render_buffer(segments)  # Unfortunate private member access...
        data = {"text/plain": text}
        if include:
            data = {k: v for (k, v) in data.items() if k in include}
        if exclude:
            data = {k: v for (k, v) in data.items() if k not in exclude}
        return data

    def _get_renderable(self) -> rich.console.RenderableType:
        """Construct the rendered layout."""
        progress = self._progress

        if self._cluster_details:
            desired_workers = self._cluster_details["desired_workers"]
            n_workers = len(jmespath.search("workers[*]", self._cluster_details) or [])
            overall_cluster_status = self._cluster_details["current_state"]["state"]
            scheduler_status = self._cluster_details["scheduler"]["current_state"][
                "state"
            ]
            scheduler_ready = (
                ProcessStateEnum(scheduler_status) == ProcessStateEnum.started
            )
            dashboard_address = (
                jmespath.search(
                    "scheduler.instance.public_ip_address", self._cluster_details
                )
                if scheduler_ready
                else None
            )
            scheduler_instance_type, worker_instance_types = get_instance_types(
                self._cluster_details
            )
            region = self._cluster_details["cluster_options"]["region_name"]
            cluster_name = self._cluster_details["name"]

            statuses = get_worker_statuses(self._cluster_details)
            progress.update(
                self._provision_task,
                total=n_workers,
                completed=statuses[CombinedProcessStateEnum.instance_queued]
                + statuses[CombinedProcessStateEnum.instance_starting],
            )
            progress.update(
                self._downloading_extracting_task,
                total=n_workers,
                completed=statuses[CombinedProcessStateEnum.downloading],
            )
            progress.update(
                self._boot_task,
                total=n_workers,
                completed=statuses[CombinedProcessStateEnum.instance_running],
            )
            progress.update(
                self._ready_task,
                total=n_workers,
                completed=statuses[CombinedProcessStateEnum.ready],
            )
            progress.update(
                self._stopping_task,
                total=n_workers,
                completed=statuses[CombinedProcessStateEnum.stopping],
            )
            progress.update(
                self._stopped_task,
                total=n_workers,
                completed=statuses[CombinedProcessStateEnum.stopped],
            )
            progress.update(
                self._error_task,
                total=n_workers,
                completed=statuses[CombinedProcessStateEnum.error],
            )
        else:
            overall_cluster_status = "Not available"
            scheduler_status = "Not available"
            dashboard_address = None
            scheduler_instance_type = "Not available"
            worker_instance_types = Counter()
            region = "Unknown"
            cluster_name = ""
            desired_workers = ""

        dashboard_address = (
            f"http://{dashboard_address}:8787" if dashboard_address else None
        )
        dashboard_label = (
            f"[link={dashboard_address}]{dashboard_address}[/link]"
            if dashboard_address
            else "Scheduler has not started"
        )

        worker_instance_types_label = ", ".join(
            f"{k or 'Unknown'} ({v:,})" for k, v in worker_instance_types.items()
        )
        config = dedent(
            f"""
            [bold red]Region:[/bold red] {region}

            [bold red]Scheduler Instance Type:[/bold red] {scheduler_instance_type or 'Not Available'}

            [bold red]Worker Instance Type(s):[/bold red] {worker_instance_types_label or 'Not Available'}

            [bold red]Workers Requested:[/bold red] {desired_workers}"""
        )

        status = dedent(
            f"""
            [bold red]Cluster Name:[/bold red] {cluster_name}

            [bold red]Cluster Status:[/bold red] {overall_cluster_status}

            [bold red]Scheduler Status:[/bold red] {scheduler_status}

            [bold red]Dashboard Address:[/bold red] {dashboard_label}"""
        )

        """Define the layout."""
        layout = rich.layout.Layout(name="root")

        layout.split(
            rich.layout.Layout(
                rich.panel.Panel(
                    rich.align.Align.center("[bold red frame]Coiled Cluster"),
                ),
                name="header",
                size=3,
            ),
            rich.layout.Layout(name="body", size=12),
            rich.layout.Layout(name="progress", size=9),
        )
        layout["body"].split_row(
            rich.layout.Layout(name="overview"),
            rich.layout.Layout(name="configuration"),
        )
        layout["progress"].update(
            rich.panel.Panel(
                rich.align.Align.center(progress.get_renderable(), vertical="middle"),
                title="Dask Worker States",
            )
        )
        layout["body"]["overview"].update(rich.panel.Panel(status, title="Overview"))
        layout["body"]["configuration"].update(
            rich.panel.Panel(config, title="Configuration")
        )
        return layout
