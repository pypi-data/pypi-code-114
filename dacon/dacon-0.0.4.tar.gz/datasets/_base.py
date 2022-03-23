import pandas as pd
import numpy as np
import os


def load_data(cpt_id, file_name='train.csv') :
    """
    Args:
        cpt_id : (int) 대회 id
        file_name : (str) 'train.csv', 'test.csv', 'sample_submission.csv', ...

    Returns:
        _type_ : pd.DataFrame
    """

    # if str(cpt_id) in os.listdir(self.data_path) :    
    root_path = 'datasets/dataset'
    data_path = os.path.join(root_path, str(cpt_id), file_name) # 'dataset/{cpt_id}/{file_name}.csv'
    data = pd.read_csv(data_path)
    
    return data
    
    # else:
    #     print(f'{cpt_id}에 해당하는 데이터가 없습니다.')
        
        
def get_cpt_id(competition='all') :
    cpt_id_dict = {
        '펭귄 몸무게 예측 경진대회' : 235862
     }

    if competition=='all' :
        return cpt_id_dict
     
    else :
        try :
            return cpt_id_dict[competition]
        except :
            print('입력하신 대회(competition)가 존재하지 않습니다.')
            print('get_cpt_id()를 통해 전체 cpt_id 목록을 확인하실 수 있습니다.')
        