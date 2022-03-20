""" Various ways to plot the data """

# imports
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import imageio


# a plot of the field 
def create_football_field(linenumbers=True,
                          endzones=True,
                          highlight_line=False,
                          highlight_line_number=50,
                          highlighted_name='Line of Scrimmage',
                          fifty_is_los=False,
                          figsize=(12, 6.33)):
    """
    Function that plots the football field for viewing plays.
    Allows for showing or hiding endzones.
    Initially Adapated from:  https://www.kaggle.com/robikscube/nfl-big-data-bowl-plotting-player-position
    """
    rect = patches.Rectangle((0, 0), 120, 53.3, linewidth=0.1,
                             edgecolor='r', facecolor='white', zorder=0)

    fig, ax = plt.subplots(1, figsize=figsize)
    ax.add_patch(rect)

    plt.plot([10, 10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
              80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
             [0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3,
              53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
             color='black')
    if fifty_is_los:
        plt.plot([60, 60], [0, 53.3], color='gold')
        plt.text(62, 50, '<- Player Yardline at Snap', color='gold')
    # Endzones
    if endzones:
        ez1 = patches.Rectangle((0, 0), 10, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='grey',
                                alpha=0.2,
                                zorder=0)
        ez2 = patches.Rectangle((110, 0), 120, 53.3,
                                linewidth=0.1,
                                edgecolor='r',
                                facecolor='grey',
                                alpha=0.2,
                                zorder=0)
        ax.add_patch(ez1)
        ax.add_patch(ez2)
    plt.xlim(0, 120)
    plt.ylim(-5, 58.3)
    plt.axis('off')
    if linenumbers:
        for x in range(20, 110, 10):
            numb = x
            if x > 50:
                numb = 120 - x
            plt.text(x, 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='black')
            plt.text(x - 0.95, 53.3 - 5, str(numb - 10),
                     horizontalalignment='center',
                     fontsize=20,  # fontname='Arial',
                     color='black', rotation=180)
    if endzones:
        hash_range = range(11, 110)
    else:
        hash_range = range(1, 120)

    for x in hash_range:
        ax.plot([x, x], [0.4, 0.7], color='black')
        ax.plot([x, x], [53.0, 52.5], color='black')
        ax.plot([x, x], [22.91, 23.57], color='black')
        ax.plot([x, x], [29.73, 30.39], color='black')

    if highlight_line:
        hl = highlight_line_number + 10
        plt.plot([hl, hl], [0, 53.3], color='yellow')
        plt.text(hl + 2, 50, '<- {}'.format(highlighted_name),
                 color='yellow')
    return fig, ax

def plot_play(p, 
              frame=1, 
              homecol="red", 
              awaycol="blue", 
              ballcol="orange", 
              show = True, 
              save=False):
    
    # assert that a play Dataframe is passed.  Likely will be from extract <inserthere>
    assert isinstance(p, pd.DataFrame)
    p.columns = p.columns.str.lower()

    fig, ax = create_football_field()

    if frame is not None and isinstance(frame, int):
        p = p.loc[p.frameid==frame, :]
    # away team
    p.query("team == 'away'").plot(x='x', y='y', kind='scatter', ax=ax, color=awaycol, s=30, legend='Away')
    # home team
    p.query("team == 'home'").plot(x='x', y='y', kind='scatter', ax=ax, color=homecol, s=30, legend='Home')   
    # football 
    p.query("team == 'football'").plot(x='x', y='y', kind='scatter', ax=ax, color=ballcol, s=30, legend='Football')
    
    plt.legend()

    if show:
        plt.show() 

    if save:
        plt.savefig(f"plots/frame-{frame}.png")  

    plt.close()



# function to make the gif from a play
def make_gif(play, 
             fname="play.gif", 
             homecol="red", 
             awaycol="blue", 
             ballcol="orange", 
             show=True, 
             save=False):
  """
  Uses plot_play and create_football_field to take a valid play and plot each frame
  and stitch together the gif for the play on the field.
  """

  # isolate the frames for the play
  frames = list(set(play.frameid))

  # generate the image for each frame
  for frame in frames:
    plot_play(p=play, 
              frame=frame, 
              save=True, 
              show=False, 
              awaycol=awaycol, 
              homecol=homecol, 
              ballcol=ballcol)
  
  # assemble into a gif
  filenames = os.listdir("plots/")
  images = []
  
  for filename in filenames:
    images.append(imageio.imread("plots/"+ filename))

  imageio.mimsave(fname, images)


