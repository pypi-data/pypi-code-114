import pandas as pd
from functools import reduce
static_resource_path="/ocean/projects/asc170022p/shared/Data/ukBiobank/meta_data_november_2021/"
home_directory="/ocean/projects/asc170022p/tighu/"
fs_combat_cols=['eid','53-2.0','34-0.0','31-0.0','54-2.0']

class harmonize_fs_data:

    def __init__(self):

        return

    def get_input_to_harmonizer(self):
        with open(home_directory+'/jupyter_notebooks/'+'UKB_fs_folder_paths_march_2022.csv') as f:
            folder_paths = f.read().splitlines()

        fs_subject_list = []
        for path in folder_paths:
            fs_subject_list.append(path.split("/")[-3])

        long_combat_df = pd.read_csv(home_directory + "ukb_brain_imaging_metadata.csv")
        long_combat_df = long_combat_df[long_combat_df['eid'].isin(fs_subject_list)]
        long_combat_df = long_combat_df.rename(
            columns={"eid": "Subject_ID", "31-0.0": "Sex", "34-0.0": "Year_of_Birth", "53-2.0": "Date_of_Brain_Scan",
                     "54-2.0": "Assesment_Centre"})
        long_combat_df['Assesment_Centre'] = long_combat_df['Assesment_Centre'].apply(lambda x: self.get_center(x))
        long_combat_df = long_combat_df.reset_index(drop=True)
        long_combat_df['Date_of_Brain_Scan'] = pd.to_datetime(long_combat_df['Date_of_Brain_Scan'])
        long_combat_df['Sex'] = long_combat_df['Sex'].apply(lambda x: self.ukb_subject_sex(x))
        long_combat_df['Age'] = long_combat_df['Year_of_Birth'].apply(lambda x: self.ukb_subject_age(x))
        long_combat_df['Age_at_Scan'] = long_combat_df.apply(lambda x: self.ukb_subject_age_at_scan(x), axis=1)

        vol_csv = pd.read_csv(home_directory + "ukb_aseg_stats_volumes_march_2022.csv")
        rh_csv = pd.read_csv(home_directory + "ukb_stats_rh_thicknesss_march_2022.csv")
        lh_csv = pd.read_csv(home_directory + "ukb_stats_lh_thickness_march_2022.csv")
        df_list = [lh_csv, rh_csv, vol_csv]

        df_long_combat_merged = reduce(lambda left, right: pd.merge(left, right, on=['folder_path'],
                                                                    how='outer'), df_list)
        df_long_combat_merged['Subject_ID'] = df_long_combat_merged['folder_path'].apply(
            lambda x: self.parse_subject_id_from_path(x))
        df_long_combat_merged['Subject_ID'] = df_long_combat_merged['folder_path'].apply(
            lambda x: self.parse_subject_id_from_path(x))

        long_combat_df['Subject_ID'] = long_combat_df['Subject_ID'].astype(str)

        final_df = pd.merge(long_combat_df, df_long_combat_merged, on='Subject_ID', how='inner')


        self.harmonize_df=final_df

        return self.harmonize_df



    def get_input_to_harmonizer_batch(self,subject_id_list):

        long_combat_df = pd.read_csv(home_directory + "ukb_brain_imaging_metadata.csv")
        long_combat_df = long_combat_df[long_combat_df['eid'].isin(subject_id_list)]
        long_combat_df = long_combat_df.rename(
            columns={"eid": "Subject_ID", "31-0.0": "Sex", "34-0.0": "Year_of_Birth", "53-2.0": "Date_of_Brain_Scan",
                     "54-2.0": "Assesment_Centre"})
        long_combat_df['Assesment_Centre'] = long_combat_df['Assesment_Centre'].apply(lambda x: self.get_center(x))
        long_combat_df = long_combat_df.reset_index(drop=True)
        long_combat_df['Date_of_Brain_Scan'] = pd.to_datetime(long_combat_df['Date_of_Brain_Scan'])
        long_combat_df['Sex'] = long_combat_df['Sex'].apply(lambda x: self.ukb_subject_sex(x))
        long_combat_df['Age'] = long_combat_df['Year_of_Birth'].apply(lambda x: self.ukb_subject_age(x))
        long_combat_df['Age_at_Scan'] = long_combat_df.apply(lambda x: self.ukb_subject_age_at_scan(x), axis=1)

        fs_features_df=pd.read_csv(home_directory+"jupyter_notebooks/ukb_fs_features.csv")
        fs_features_df = fs_features_df[fs_features_df['Subject_ID'].isin(subject_id_list)]

        final_df = pd.merge(long_combat_df, fs_features_df, on='Subject_ID', how='outer')

        return final_df

    def ukb_subject_sex(self,type):
        if type == 0.0:
            return "F"

        else:
            return "M"
    def ukb_subject_age(self,year):
        return int(2022 - year)

    def ukb_subject_age_at_scan(self,row):
        return int(row['Date_of_Brain_Scan'].year - row['Year_of_Birth'])

    def parse_subject_id_from_path(self,path):
        return path.split("/")[-3]

    def get_center(self,center):
        if center == 11025.0:
            return "Cheadle"

        elif center == 11026.0:
            return "Reading"

        elif center == 11027.0:
            return "Newcastle"
