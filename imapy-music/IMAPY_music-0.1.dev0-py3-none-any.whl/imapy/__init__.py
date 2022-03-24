from decimal import Decimal

from .scripts.metro_weights_mazzola import MetroWeights_Mazzola
from .scripts.weight_set import WeightSet


class IMA():
    """
    The class used to calculate the Inner Metric Analysis from a set of musical onsets
    ...

    Attributes
    ----------
    mw : object of class MetroWeights_Mazzola
        calculator for Inner Metric Analysis based on Mazzola's *The Topos of Music*
    weight_set : object of class WeightSet
        Set of Weights resulting from the application of Inner Metric Analysis

    Methods
    -------
    setParameters(period=2, length=2, offset=0, resolution=1, maxPeriod=0)
        Sets Weights for the
    """

    mw: MetroWeights_Mazzola = None
    weight_set: WeightSet = None

    def __init__(self, onsets, period=2, length=2, offset=0, resolution=1, maxPeriod=0):
        """
        """
        self.setParameters(period, length, offset, resolution, maxPeriod)
        self.calculateWeights(onsets)

    def setParameters(self, period=2, length=2, offset=0, resolution=1, maxPeriod=0):
        """
        """
        self.mw = MetroWeights_Mazzola(
            period, length, offset, resolution, maxPeriod)

    def calculateWeights(self, onsets):
        """
        """
        self.weight_set = self.mw.getWeights(onsets)

    def calculate_IMA_score(self, fm='.6f') -> list[float]:
        """
        """
        maxw: int = max(self.weight_set.weights)
        if maxw == 0:
            maxw = 1

        if format is None:
            return [Decimal(weight/maxw) for weight in self.weight_set.weights]
        return [float(format(Decimal(weight/maxw), fm)) for weight in self.weight_set.weights]

    def __str__(self) -> str:
        """
        """
        print("Maximal local meters:")
        self.weight_set.meterCollection.printAll()

        print("Weights")
        print(' '.join([f"{weight}" for weight in self.weight_set.weights]))

        print("Spectral Weights")
        print(
            ' '.join([f"{weight}" for weight in self.weight_set.spectralWeight]))
