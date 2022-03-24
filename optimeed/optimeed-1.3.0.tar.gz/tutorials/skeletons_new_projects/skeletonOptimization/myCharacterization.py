from optimeed.optimize import InterfaceCharacterization


class MyCharacterization(InterfaceCharacterization):
    def compute(self, theDevice):
        # Performs some actions to determine the characteristics of the device.
        # For example, imagine linked to a FEM solver, algorithm would be:
        # write_params(theDevice)
        # mesh_geometry()
        # solve()
        # read_results()
        # results -> theDevice (ex: theDevice.Torque = myTorque)
        pass
