import finesse
import numpy as np
from finesse.analysis.actions import Action, RunLocks, OptimiseRFReadoutPhaseDC


def make_aligo(RF_AS_readout=False, verbose=False):
    base = finesse.Model()
    base.parse(aligo_katscript)
    base.run(
        OptimiseRFReadoutPhaseDC(
            "CARM",
            "REFL9",
            "PRCL",
            "POP9",
            "SRCL",
            "POP45",
            "DARM",
            "AS45",
        )
    )

    set_lock_gains(base, verbose=verbose)

    if not RF_AS_readout:
        base.run(DARM_RF_to_DC())

    return base


class DARM_RF_to_DC(Action):
    """Locks a model using DARM RF readout then transitions the model into using a DC
    readout and locks."""

    def __init__(self, name="DarmRF2DC"):
        super().__init__(name)
        self.__lock_rf = RunLocks("DARM_rf_lock")
        self.__lock_dc = RunLocks("DARM_dc_lock")

    def _do(self, state):
        self.__lock_rf._do(state)
        state.model.DARM_rf_lock.disabled = True
        # kick lock away from zero tuning for DC lock to grab with
        state.model.DARM.DC += 0.5e-3
        # take a guess at the gain
        state.model.DARM_dc_lock.gain = -0.01
        state.model.DARM_dc_lock.disabled = False
        self.__lock_dc._do(state)
        return None

    def _requests(self, model, memo, first=True):
        self.__lock_rf._requests(model, memo)
        self.__lock_dc._requests(model, memo)
        return memo


class DRFPMI_state(Action):
    """Assumes a mode has a PRM, SRM, ITMX, ETMX, ITMY, and ETMY mirror elements in.
    This action will change the alignment state of these. The options are:

    'PRMI', 'SRMI', 'MI', 'FPMI', 'PRFPMI', 'SRFPMI', 'DRFPMI', 'XARM', 'YARM'

    This action will change the state of the model.
    """

    def __init__(self, state: str, name="drfpmi_state"):
        super().__init__(name)
        states = (
            "PRMI",
            "SRMI",
            "MI",
            "FPMI",
            "PRFPMI",
            "SRFPMI",
            "DRFPMI",
            "XARM",
            "YARM",
        )
        if state not in states:
            raise ValueError(f"State '{state}' is not a valid option: {states}")
        self.state = state

    def _do(self, state):
        if self.state == "PRMI":
            state.model.PRM.misaligned = 0
            state.model.SRM.misaligned = 1
            state.model.ETMX.misaligned = 1
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 1
            state.model.ITMY.misaligned = 0
        elif self.state == "SRMI":
            state.model.PRM.misaligned = 1
            state.model.SRM.misaligned = 0
            state.model.ETMX.misaligned = 1
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 1
            state.model.ITMY.misaligned = 0
        elif self.state == "MI":
            state.model.PRM.misaligned = 1
            state.model.SRM.misaligned = 1
            state.model.ETMX.misaligned = 1
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 1
            state.model.ITMY.misaligned = 0
        elif self.state == "FPMI":
            state.model.PRM.misaligned = 1
            state.model.SRM.misaligned = 1
            state.model.ETMX.misaligned = 0
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 0
            state.model.ITMY.misaligned = 0
        elif self.state == "PRFPMI":
            state.model.PRM.misaligned = 0
            state.model.SRM.misaligned = 1
            state.model.ETMX.misaligned = 0
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 0
            state.model.ITMY.misaligned = 0
        elif self.state == "SRFPMI":
            state.model.PRM.misaligned = 1
            state.model.SRM.misaligned = 0
            state.model.ETMX.misaligned = 0
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 0
            state.model.ITMY.misaligned = 0
        elif self.state == "DRFPMI":
            state.model.PRM.misaligned = 0
            state.model.SRM.misaligned = 0
            state.model.ETMX.misaligned = 0
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 0
            state.model.ITMY.misaligned = 0
        elif self.state == "YARM":
            state.model.PRM.misaligned = 1
            state.model.SRM.misaligned = 1
            state.model.ETMX.misaligned = 1
            state.model.ITMX.misaligned = 1
            state.model.ETMY.misaligned = 0
            state.model.ITMY.misaligned = 0
        elif self.state == "XARM":
            state.model.PRM.misaligned = 1
            state.model.SRM.misaligned = 1
            state.model.ETMX.misaligned = 0
            state.model.ITMX.misaligned = 0
            state.model.ETMY.misaligned = 1
            state.model.ITMY.misaligned = 1
        else:
            raise Exception(f"{self.state} not implemented")

    def _requests(self, model, memo, first=True):
        # changing the mirror misaligned parameter is essentially
        # changing the mirror reflectivity model parameter
        memo["changing_parameters"].extend(
            (
                "PRM.misaligned",
                "SRM.misaligned",
                "ETMX.misaligned",
                "ITMX.misaligned",
                "ETMY.misaligned",
                "ITMY.misaligned",
            )
        )
        return memo


def set_lock_gains(model, d_dof=1e-6, gain_scale=1, verbose=False):
    """For the current state of the model each lock will have its gain computed. This is
    done by computing the gradient of the error signal with respect to the set feedback.

    The optical gain is then computed as -1/(slope).

    This function alters the state of the provided model.

    Parameters
    ----------
    model : Model
        Model to set the lock gains of
    d_dof : double
        step size for computing the slope of the error signals
    verbose : boolean
        Prints information when true
    """
    from finesse.analysis.actions import Xaxis, Series
    from finesse.components.readout import ReadoutDetectorOutput

    for lock in model.locks:
        # Make sure readouts being used have their outputs enabled
        if type(lock.error_signal) is ReadoutDetectorOutput:
            lock.error_signal.readout.output_detectors = True

    # Use a flattened series analysis as it only creates one model
    # and xaxis resets all the parameters each time
    analysis = Series(
        *(
            Xaxis(lock.feedback, "lin", -d_dof, d_dof, 1, relative=True, name=lock.name)
            for lock in model.locks
        ),
        flatten=True,
    )
    sol = model.run(analysis)

    for lock in model.locks:
        lock_sol = sol[lock.name]
        x = lock_sol.x1
        error = lock_sol[lock.error_signal.name] + lock.offset
        grad = np.gradient(error, x[1] - x[0]).mean()
        if grad == 0:
            lock.gain = np.NaN
        else:
            lock.gain = -1 / grad * gain_scale

        if verbose:
            print(lock, lock.error_signal.name, lock.gain)


def get_lock_error_signals(model, dof_range, steps=1000, verbose=False):
    from finesse.analysis.actions import Xaxis, Series
    from finesse.components.readout import ReadoutDetectorOutput

    for lock in model.locks:
        # Make sure readouts being used have their outputs enabled
        if type(lock.error_signal) is ReadoutDetectorOutput:
            lock.error_signal.readout.output_detectors = True

    # Use a flattened series analysis as it only creates one model
    # and xaxis resets all the parameters each time
    analysis = Series(
        *(
            Xaxis(
                lock.feedback,
                "lin",
                -dof_range,
                dof_range,
                steps,
                relative=True,
                name=lock.feedback.owner.name,
            )
            for lock in model.locks
        ),
        flatten=True,
    )
    sol = model.run(analysis)
    return sol