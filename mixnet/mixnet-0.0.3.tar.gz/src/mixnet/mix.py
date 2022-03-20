'''
mixnet.py: A model to predict compressive strength of concrete based on it's composition
'''
import xgboost as xgb
import numpy as np

from importlib.resources import files, as_file
from pathlib import Path

def compressive_strength(
    cement: float,
    slag: float,
    fly_ash: float,
    water: float,
    superplasticizer: float,
    coarse_aggregate: float,
    fine_aggregate: float,
    age: float,
) -> float:
    '''
    Computes compressive strength based on
    mixture composition.
    Unit of every quantity is in kg/m^3
    '''
    concrete_net = xgb.Booster()
    

    
    
    path = (Path(__file__).parent / "concrete.net").resolve()
    concrete_net.load_model(path)

    item = np.array(
        [
            [
                cement,
                slag,
                fly_ash,
                water,
                superplasticizer,
                coarse_aggregate,
                fine_aggregate,
                age,
            ],
        ]
    )

    item_test = xgb.DMatrix(item)
    # print(f'The Mixture will have compressive strength of {ypred[0]} MPa')
    return concrete_net.predict(item_test)[0]



if __name__ == "__main__":
    CEMENT           = 540  # KG/M^3
    SLAG             = 12
    FLY_ASH          = 40
    WATER            = 4
    SUPERPLASTICIZER = 20
    COARSE_AGGREGATE = 35
    FINE_AGGREGATE   = 43
    AGE              = 34

    compressive_strength(
        CEMENT,
        SLAG,
        FLY_ASH,
        WATER,
        SUPERPLASTICIZER,
        COARSE_AGGREGATE,
        FINE_AGGREGATE,
        AGE,
    )
