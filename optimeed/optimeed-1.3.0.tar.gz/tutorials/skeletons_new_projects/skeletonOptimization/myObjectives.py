from optimeed.optimize import InterfaceObjCons


class MyObjective(InterfaceObjCons):
    def compute(self, theDevice):
        # return an objective to minimize, based on input device.
        # For example: return theDevice.torque
        pass

