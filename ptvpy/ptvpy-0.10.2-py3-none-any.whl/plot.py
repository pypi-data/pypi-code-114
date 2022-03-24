"""Tools for plotting and visual inspection."""


import functools

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

# Needed for scatter_plot_3d, registers Axes3D as a 'projection' object
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401, lgtm[py/unused-import]
from mpl_toolkits.axes_grid1 import make_axes_locatable


__all__ = [
    "SlideShowPlot",
    "heat_map",
    "histogram",
    "scatter_plot_2d",
    "scatter_plot_3d",
    "vector_field",
    "violin_plot",
]


def _suppress_autostart(plot):
    """Suppress autostart of animation in SlideShowPlot.

    A FuncAnimation auto-starts as soon as the GUI's event queue starts
    regardless of prior actions. Thus a sure way to pause the animation is to
    modify the behavior of the first 2 two actions (calls to `func`) by the
    animation itself. `func` is called once before the event queue starts. Thus
    we need to disable on the second call once the queue is actually running.

    Parameters
    ----------
    plot : SlideShowPlot
        The SlideShowPlot with the animation to suppress.

    Returns
    -------
    func : callable
        The frame function to pass to as the `func` argument to FuncAnimation's
        constructor.
    """
    # TODO Find a way to pause animation initially without this hack
    func = plot._advance_animation

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.call_count < 2:
            plot.animation_state = False
            wrapper.call_count += 1
        else:
            return func(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


class SlideShowPlot:
    """Display annotated frames as a slide show.

    The animated slide show can be (un)paused with the space key. The slider
    can be controlled by dragging with the mouse or using the arrow keys.
    Clicking near a tracked particle will display its properties and path; use
    the left mouse button to unselect.

    Parameters
    ----------
    frames : sequence
        An index-able sized container object that returns each frame as an
        array.
    particles : pandas.DataFrame, optional
        Information on detected particles.
    autostart : bool, optional
        If True, the animation starts playing as soon as the GUI's event
        queue starts.

    Attributes
    ----------
    frame_nr : int
        Currently displayed frame and slider position.
    animation_state : bool
        Control the animation state. Setting this False will pause the
        animation. Works only after event queue of the GUI backend has started.
    """

    def __init__(self, frames, particles=None, autostart=False):
        if particles is None:
            particles = pd.DataFrame(columns=["frame", "particle", "x", "y"])

        # Data storing attributes
        self.frames = frames
        self.particles = particles
        self.highlighted_particle: pd.DataFrame = None

        # Setup figure and axes placement
        self.figure = plt.figure()
        self.image_axes = self.figure.subplots()
        self.image_axes.set_xlabel("x")
        self.image_axes.set_ylabel("y")

        divider = make_axes_locatable(self.image_axes)
        self.slider_axes = divider.new_vertical(size="5%", pad=0.5, pack_start=True)
        self.colorbar_axes = divider.new_horizontal(
            size="5%", pad=0.2, pack_start=False
        )
        self.figure.add_axes(self.slider_axes)
        self.figure.add_axes(self.colorbar_axes)

        # Setup slider
        self.slider = Slider(
            self.slider_axes,
            label="Frame",
            valmin=0,
            valmax=len(self.frames) - 1,
            valinit=0,
            valfmt="%i",
            valstep=1,
        )
        self.slider.on_changed(self.update_plot)

        # Setup artists
        self.frame_artist = self.image_axes.imshow(
            self.frames[self.frame_nr], origin="lower", cmap="gray"
        )
        colorbar = self.figure.colorbar(
            self.frame_artist, cax=self.colorbar_axes, orientation="vertical"
        )
        colorbar.set_label("brightness")

        in_frame = self.particles_in_frame(self.frame_nr)
        (self.particle_artist,) = self.image_axes.plot(
            in_frame["x"], in_frame["y"], "r+", markersize=8, picker=True
        )
        # TODO: Investigate - Doesn't work when setting with plot method in
        #  which case pickradius is merily set to True
        self.particle_artist.set_pickradius(10)
        self.trace_artist: plt.Line2D = None

        # Init annotation, a popup displaying detailed information about a
        # picked article
        self.annotation = self.image_axes.annotate(
            "",
            xy=(0, 0),
            xytext=(-20, 20),
            textcoords="offset points",
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->", color="yellow"),
        )
        self.annotation.set_visible(False)

        # Init animation
        self._animation_state = True
        func = self._advance_animation if autostart else _suppress_autostart(self)
        self.animation = FuncAnimation(self.figure, func=func)

        # Connect slots
        self.figure.canvas.mpl_connect("key_press_event", self._on_key_press)
        self.figure.canvas.mpl_connect("pick_event", self._on_pick)
        self.figure.canvas.mpl_connect("button_press_event", self._on_button_press)
        self.figure.canvas.mpl_connect("button_release_event", self._on_button_release)
        self._button_3_start_pos = None  # Used in button event slots

    @property
    def frame_nr(self):
        return int(self.slider.val)

    @frame_nr.setter
    def frame_nr(self, nr):
        nr = int(nr % (self.slider.valmax + 1))
        self.slider.set_val(nr)

    @property
    def animation_state(self):
        return self._animation_state

    @animation_state.setter
    def animation_state(self, state):
        if state is True:
            self.animation.event_source.start()
        elif state is False:
            self.animation.event_source.stop()
        else:
            raise TypeError("expects a boolean")
        self._animation_state = state

    def particles_in_frame(self, nr):
        """Select particle data from a single frame."""
        return self.particles[self.particles["frame"] == nr]

    def update_plot(self, *_):
        """Redraw the plot to match the current frame number."""
        self.frame_artist.set_data(self.frames[self.frame_nr])
        self.frame_artist.autoscale()
        particles = self.particles_in_frame(self.frame_nr)
        self.particle_artist.set_data(particles["x"], particles["y"])

        if self.highlighted_particle is not None:
            # Update annotation if particle is currently visible
            nr = self.highlighted_particle["particle"].iloc[0]
            particle = particles[particles["particle"] == nr].squeeze()
            if particle.size > 0:
                self._update_particle_annotation(particle)

        self.figure.canvas.draw_idle()

    def highlight_particle(self, particle):
        """Show path and annotation of a particle over multiple frames.

        Parameters
        ----------
        particle : pandas.DataFrame[x, y, [particle, ...]]
            A DataFrame with a particle's position and optionally ID.
        """
        self.remove_highlight()

        if "particle" in particle:
            # If ID was provided show the particles trajectory
            nr = particle["particle"]
            self.highlighted_particle = self.particles[self.particles["particle"] == nr]
            (self.trace_artist,) = self.image_axes.plot(
                self.highlighted_particle["x"],
                self.highlighted_particle["y"],
                "y--",
                zorder=1,
            )
            particle = self.highlighted_particle[
                self.highlighted_particle["frame"] == self.frame_nr
            ].squeeze()  # Ensure that it's a Series

        self._update_particle_annotation(particle)
        self.annotation.set_visible(True)
        self.figure.canvas.draw_idle()

    def remove_highlight(self):
        """Remove path and annotation of a particle from the plot."""
        if self.trace_artist is not None:
            self.trace_artist.remove()
            self.trace_artist = None
        self.highlighted_particle = None
        self.annotation.set_visible(False)
        self.figure.canvas.draw_idle()

    def _update_particle_annotation(self, particle):
        """Update position and text of annotation."""
        self.annotation.xy = (particle["x"], particle["y"])
        self.annotation.set_text(
            "\n".join(f"{key} = {value:g}" for key, value in particle.items())
        )

    def _advance_animation(self, *_):
        """Advance animation (slot for animation)."""
        self.frame_nr += 1

    def _on_key_press(self, event):
        """Deal with key press events."""
        if event.key == "right":
            self.frame_nr += 1
        elif event.key == "left":
            self.frame_nr -= 1
        elif event.key == " ":
            self.animation_state = not self.animation_state  # Toggle

    def _on_pick(self, event):
        """Deal with pick events (selection of artist elements)."""
        if event.artist == self.particle_artist:
            index = event.ind[0]
            particle = self.particles_in_frame(self.frame_nr).iloc[index, :]
            self.highlight_particle(particle)

    def _on_button_press(self, event):
        """Deal with mouse button press events."""
        if event.button == 3:
            self._button_3_start_pos = (event.x, event.y)

    def _on_button_release(self, event):
        """Deal with mouse button release events."""
        if event.button == 3:
            if self._button_3_start_pos == (event.x, event.y):
                # Don't remove when mouse was dragged while pressed, this
                # allows proper use of the pan and zoom modes
                self.remove_highlight()


def heat_map(x, y, z, *, data, fig_ax=None):
    """Plot variable as a color-coded 2D heatmap.

    Parameters
    ----------
    x, y, z : str
        Column names for `data`. `x` and `y` are interpreted as coordinates of the
        regular sampled scalar field `z`.
    data : pandas.DataFrame, columns (x, y, z)
        DataFrame with columns matching the 3 variables above.
    fig_ax : (matplotlib.Figure, maptlotlib.Axes), optional
        The figure and axes used to create the plot. If not provided new ones
        will be created.

    Returns
    -------
    figure : matplotlib.Figure
        The created figure.
    axes : matplotlib.Axes
        The created axes.
    """
    data = data.pivot(index=x, columns=y, values=z)

    figure, axes = plt.subplots() if fig_ax is None else fig_ax
    caxes = axes.pcolormesh(
        data.index, data.columns, data.values, cmap="magma", shading="nearest"
    )
    cbar = figure.colorbar(caxes)

    cbar.outline.set_linewidth(0)
    cbar.ax.set_ylabel(z)
    axes.set_xlabel(x)
    axes.set_ylabel(y)
    sns.despine(ax=axes)
    figure.set_tight_layout(True)

    return figure, axes


def histogram(*variables, data, log=True, fig_ax=None):
    """Create a histogram of `x`.

    Parameters
    ----------
    *variables : iterable[str]
        Column names for `data`.
    data : pandas.DataFrame
        DataFrame with columns matching the names in `variables`.
    log : bool, optional
        Use logarithmic scale for y-axis showing the size of each bin.
    fig_ax : (matplotlib.Figure, maptlotlib.Axes), optional
        The figure and axes used to create the plot. If not provided new ones
        will be created.

    Returns
    -------
    figure : matplotlib.figure.Figure
        Figure used to draw.
    axes : matplotlib.axes.Axes
        Axes used for plotting.
    """
    figure, axes = plt.subplots() if fig_ax is None else fig_ax
    axes.grid(True, alpha=0.5)

    sns.histplot(
        data[list(variables)].dropna(),
        kde=True,
        ax=axes,
        log_scale=(False, log),
    )

    return figure, axes


def scatter_plot_2d(x, y, *, data, color=None, order=0, fig_ax=None):
    """Plot regression plot between two variables.

    Parameters
    ----------
    x, y: str
        Column names for `data`.
    data : pandas.DataFrame, columns (x, y[, color])
        DataFrame with columns matching the 4 variables above.
    color : str or ndarray, optional
        Column name for `data`. Used as the basis for coloring the scatter points using
        a colormap.
    order : int, optional
        Fit a regression model to the data if > 0. 1 will use a linear regression,
        values >= 2 will use a polynomial fit of the specified order.
    fig_ax : (matplotlib.Figure, maptlotlib.Axes), optional
        The figure and axes used to create the plot. If not provided new ones
        will be created.

    Returns
    -------
    figure : matplotlib.Figure
        The created figure.
    axes : matplotlib.Axes
        The created axes.
    """
    figure, axes = plt.subplots() if fig_ax is None else fig_ax
    axes.grid(True, alpha=0.5)

    points = axes.scatter(data[x], data[y], c=data.get(color, None), cmap="magma", s=10)
    if color is not None:
        cbar = figure.colorbar(points)
        cbar.outline.set_linewidth(0)
        reg_line_color = "gray"
    else:
        reg_line_color = None

    # Postpone setting alpha to avoid pale colors in colorbar
    points.set_alpha(0.2)

    if order > 0:
        sns.regplot(
            x=x,
            y=y,
            data=data,
            scatter=False,
            truncate=True,
            order=order,
            ax=axes,
            color=reg_line_color,
        )

    return figure, axes


def scatter_plot_3d(x, y, z, *, data, color=None):
    """Create a scatter plot with 3 dimensions.

    Parameters
    ----------
    x, y, z : str
        Column names for `data`. `x` and `y` are interpreted as coordinates of the
        regular sampled scalar field `z`.
    data : pandas.DataFrame, columns (x, y, z[, color])
        DataFrame with columns matching the given variables above.
    color : str, optional
        Column name for `data`. Used as the basis for coloring the scatter points using
        a colormap.

    Returns
    -------
    figure : matplotlib.Figure
        The created figure.
    axes : matplotlib.Axes
        The created axes.
    """
    x = data.get(x, x)
    y = data.get(y, y)
    z = data.get(z, z)
    if color is not None:
        color = data.get(color, color)

    figure = plt.figure()
    axes = figure.add_subplot(111, projection="3d")
    points = axes.scatter(xs=x, ys=y, zs=z, c=color, cmap="magma", depthshade=False)

    # Set label names
    axes.set_xlabel(x.name)
    axes.set_ylabel(y.name)
    axes.set_zlabel(z.name)

    if color is not None:
        cbar = figure.colorbar(points)
        cbar.outline.set_linewidth(0)
        cbar.set_label(color.name)

    # Postpone setting alpha to avoid pale colors in colorbar
    points.set_alpha(0.2)

    figure.set_tight_layout(True)
    return figure, axes


def vector_field(x, y, dx, dy, *, data, show_heatmap=True, fig_ax=None):
    """Plot two variables as a 2D vector field.

    Parameters
    ----------
    x, y, dx, dy : str
        Column names for `data`. `x` and `y` are interpreted as coordinates of the two
        regular sampled scalar fields `dx` (in `x` direction) and `dy` (in `y`
        direction) of the vector field.
    data : pandas.DataFrame, columns (x, y, dx, dy)
        DataFrame with columns matching the 4 variables above.
    show_heatmap : bool, optional
        If true, a map of the absolute value of each arrow (`dx`, `dy`) is used
        to plot a heatmap in the background.
    fig_ax : (matplotlib.Figure, maptlotlib.Axes), optional
        The figure and axes used to create the plot. If not provided new ones
        will be created.

    Returns
    -------
    figure : matplotlib.Figure
        The created figure.
    axes : matplotlib.Axes
        The created axes.
    """
    data = data[[x, y, dx, dy]]
    dxy = f"|({dx}, {dy})|"
    data[dxy] = np.sqrt(data[dx] ** 2 + data[dy] ** 2)

    figure, axes = plt.subplots() if fig_ax is None else fig_ax

    if show_heatmap:
        heat_map(x, y, dxy, data=data, fig_ax=(figure, axes))

    axes.quiver(
        data[x], data[y], data[dx], data[dy], data[dxy], cmap="binary", units="xy"
    )

    axes.set_xlabel(x)
    axes.set_ylabel(y)
    axes.set_xlabel("{} [{}]".format(axes.get_xlabel(), dx))
    axes.set_ylabel("{} [{}]".format(axes.get_ylabel(), dy))

    if not show_heatmap:
        # Only show grid when there is no heatmap in the background
        axes.grid(True, alpha=0.5)

    return figure, axes


def violin_plot(*variables, data, fig_ax=None):
    """Make shard violin plot for given variables.

    Parameters
    ----------
    *variables : iterable[str]
        Column names for `data`.
    data : pandas.DataFrame
        DataFrame with columns matching the names in `variables`.
    fig_ax : (matplotlib.Figure, maptlotlib.Axes), optional
        The figure and axes used to create the plot. If not provided new ones
        will be created.

    Returns
    -------
    figure : matplotlib.figure.Figure
        Figure used to draw.
    axes : matplotlib.axes.Axes
        Axes used for plotting.
    """
    to_plot = data[list(variables)]

    figure, axes = plt.subplots() if fig_ax is None else fig_ax
    axes.grid(True, alpha=0.5)
    sns.violinplot(data=to_plot, ax=axes, scale="count", inner="quartile")

    return figure, axes
