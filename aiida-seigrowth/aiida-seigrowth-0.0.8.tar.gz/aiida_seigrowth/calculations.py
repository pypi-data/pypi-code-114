"""
Calculations provided by aiida_seigrowth.

Register calculations via the "aiida.calculations" entry point in setup.py.
"""
from aiida.common.datastructures import CalcInfo, CodeInfo
from aiida.engine import CalcJob
from aiida.orm import SinglefileData,Str


class PbeSeiCalculation(CalcJob):
    """
    AiiDA calculation plugin wrapping the python3.8 script executable pb.py.

    Simple AiiDA plugin wrapper to compute SEI growth by using population balance modeling
    """

    @classmethod
    def define(cls, spec):
    	super().define(spec)
    	spec.input("parameters", valid_type=SinglefileData, help="Parametri chimico/fisici per la crescita del SEI")
    	spec.input("InitialSeiDistribution", valid_type=SinglefileData, help ="Distribuzione iniziale del SEI")
    	spec.input("PybammData", valid_type = SinglefileData, help = "File .pkl prodotto dalla simulazione pybamm")
    	spec.input("Path", valid_type = Str, help = 'absolute path ai file di input')
    	# spec.inputs['metadata']['options']['parser_name'].default = 'seigrowth.pbe'
    	spec.inputs['metadata']['options']['resources'].default = {'num_machines': 1, 'num_mpiprocs_per_machine': 1}

    def prepare_for_submission(self, folder) -> CalcInfo:
				
        codeinfo = CodeInfo()
        codeinfo.code_uuid = self.inputs.code.uuid
        
        calcinfo = CalcInfo()
        calcinfo.local_copy_list = [(self.inputs.parameters.uuid, self.inputs.parameters.filename, 'parameters.dat')]
        calcinfo.local_copy_list = [(self.inputs.InitialSeiDistribution.uuid, self.inputs.InitialSeiDistribution.filename, 'InitialSEIDistribution.dat')]
        calcinfo.local_copy_list = [(self.inputs.PybammData.uuid, self.inputs.PybammData.filename, 'Trajectory.pkl')]
        
        calcinfo.codes_info = [codeinfo]
        return calcinfo
