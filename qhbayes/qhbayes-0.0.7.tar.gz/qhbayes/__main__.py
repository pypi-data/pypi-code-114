import argparse

import matplotlib.pyplot as plt

from .app import make_dashboard
from .data import IVESPA, Aubry, Mastin, Sparks

parser = argparse.ArgumentParser()
parser.add_argument(
    "-app", "--app", action="store_true", help="launch the QHBayes app in browser"
)
parser.add_argument(
    "-data",
    "--dataset",
    type=str,
    choices=["Mastin", "Sparks", "Aubry", "IVESPA"],
    help="Select dataset for example",
)
parser.add_argument(
    "-x",
    "--xvar",
    type=str,
    choices=["H", "Q"],
    help="Select explanatory variable for example",
)
parser.add_argument(
    "-y",
    "--yvar",
    type=str,
    choices=["H", "Q"],
    help="Select explanatory variable for example",
)
parser.add_argument(
    "-obs",
    "--observation",
    type=float,
    default=10.0,
    help="Specify observation for example",
)
parser.add_argument(
    "-s",
    "--samples",
    type=int,
    default=100,
    help="Specify number of samples to draw in posterior simulation for example",
)
args = parser.parse_args()

if args.app:
    make_dashboard()
else:
    print("Running QHBayes example")
    print(f"{args.dataset} {args.yvar}|{args.xvar}")

    if args.dataset == "Mastin":
        data = Mastin
    elif args.dataset == "Sparks":
        data = Sparks
    elif args.dataset == "Aubry":
        data = Aubry
    else:  # args.dataset == 'IVESPA':
        data = IVESPA

    data.set_vars(xvar=args.xvar, yvar=args.yvar)  # sets independent and variables

    data.mle(plot=True)  # maximum likelihood estimator (Mastin curve)
    data.set_obs(args.observation)  # Example -- set observed H to 10 km

    data.posterior_simulate(
        args.samples, plot=True
    )  # Sample from the posterior distribution (get MER values) for 1000 samples, and plot it

    # cdf10 = Mastin.posterior_probability(
    #     yp=7
    # )  # What is the probability density for a MER of Q=10^7
    # pp05 = Mastin.posterior_point(pp=0.5)  # What MER value has p(Q<MER) = 0.5
    # print(cdf10)
    # print(pp05)

    # print(
    #     Mastin.posterior_median()
    # )  # What is the median value of the posterior MER (given H=10 km)
    # print(
    #     Mastin.posterior_mean()
    # )  # What is the mean value of the posterior MER (given H=10 km)

    data.posterior_distribution()  # Calculate the full posterior distribution (i.e. for range of H, find MER)
    data.posterior_plot()  # Now plot the curve.
    plt.show()
