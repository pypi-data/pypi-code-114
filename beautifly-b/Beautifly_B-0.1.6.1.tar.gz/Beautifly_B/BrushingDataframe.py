# -*- coding: utf-8 -*-
"""
Created on 4th March 2022

@author: Team B IE University
"""

import pandas as pd
import numpy as np

#import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
import holoviews as hv; hv.extension('bokeh', 'matplotlib')
import pandas as pd
from datetime import date
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
pd.options.mode.chained_assignment = None

## custom classes
from .woe import WOE
from .print_msg import Print_Msg
from .stats_bs import Stats_BS
from .ordinal import Ordinal
## 

pd.options.plotting.backend = 'holoviews'

class BrushingDataframe(pd.DataFrame):
    """
    The class is used to extend the properties of Dataframes to a prticular
    type of Dataframes in the Risk Indistry. 
    It provides the end user with both general and specific cleaning functions, 
    though they never reference a specific VARIABLE NAME.
    
    It facilitates the End User to perform some Date Feature Engineering,
    Scaling, Encoding, etc. to avoid code repetition.
    """

    #Initializing the inherited pd.DataFrame
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    
    @property
    def _constructor(self):
        def func_(*args,**kwargs):
            df = BrushingDataframe(*args,**kwargs)
            return df
        return func_
    
#-----------------------------------------------------------------------------
                        # DATA HANDLING
#-----------------------------------------------------------------------------
    def print_msg(text):
        print("--------------------------------------------------------------------------")
        print(text)
        print("--------------------------------------------------------------------------")

    def SetAttributes(self, kwargs):
        """
        The function will update the type of the variable submitted for change.
        It will veify first that the key is present in the desired dataframe.
        If present, it will try to change the type to the desired format.
        If not possible, it will continue to the next element.         
        Parameters
        ----------
        **kwargs : The key-argument pair of field-type relationship that
        wants to be updated.
        Returns
        -------
        None.
        """
        if self.shape[0] > 0:
            for key,vartype in kwargs.items():
                if key in self.columns:
                    try:
                        self[key] = self[key].astype(vartype)
                    except:
                        print("Undefied type {}".format(str(vartype)))
                else:
                    print("The dataframe does not contain variable {}.".format(str(key)))
        else:
            print("The dataframe has not yet been initialized")

#-----------------------------------------------------------------------------
                        # SUPERVISED - BINARY CLASSIFICATION - DATA CLEANING
#-----------------------------------------------------------------------------    
    def cleaning_missing(self, input_vars=[] ):
        """
        The cleaning missing will identfy Null values and replace the missing value with median for numerial and mode of objects
        Parameters
        ----------
        input_vars: list, default=Empty
        List of selected features. Default is empty where all columns will be included.

        Returns
        -------
          A print with the analysis and clean dataframe

        Examples
        --------
        import pandas as pd
        import Beautifly_B.BrushingDataframe as bdf
        dataframe = pd.read_csv("AUTO_LOANS_DATA.csv", sep=";")
        dataframe['BINARIZED_TARGET'] = dataframe['BUCKET'].apply(lambda x: 1 if x>0 else 0)
        myrdf = bdf.BrushingDataframe(dataframe)
        myrdf.cleaning_missing()

        """
        if input_vars:
            self = self[input_vars]
            
        for column in self.columns.values:
        # Replace NaNs with the median or mode of the column depending on the column type
            try:
                self[column].fillna(self[column].median(), inplace=True)
                Print_Msg.print_msg1("Impute Null values of {0} with median ".format(column))
            except TypeError:
                self[column] = self[column].str.lower()
                most_frequent = self[column].mode()
                if len(most_frequent) > 0:
                    self[column].fillna(self[column].mode()[0], inplace=True)
                    Print_Msg.print_msg1("Impute Null values of {0} with mode ".format(column))
                else:
                    self[column].fillna(method='bfill', inplace=True)
                    self[column].fillna(method='ffill', inplace=True)
                    Print_Msg.print_msg1("Impute Null values of {0} with bfill/ffill ".format(column))
   
        return self
    def scanning(self, input_vars=[] ):
       
        """
        Scanning will scan each column, provides analysis, recommendation, statistics analysis, visualization 
        of the histogram, bar plot and box plot to provide number of counts and distributions based on the features. 
        In addition, correlation matrix is generated to provide pair wise correlation between each numerical feature. 
        The recommendation check on suspected record ID features, data features and features with high number of 
        categorical features

        Parameters
        ----------
        input_vars: list, default=Empty
        List of selected features. Default is empty where all columns will be included.

        Returns
        -------
        Beutifly_B EDA.html located in the same folder in of the notebook, message completion of the scanning and 
        generating of the html report

        Examples
        --------
        import pandas as pd
        import Beautifly_B.BrushingDataframe as bdf
        dataframe = pd.read_csv("AUTO_LOANS_DATA.csv", sep=";")
        dataframe['BINARIZED_TARGET'] = dataframe['BUCKET'].apply(lambda x: 1 if x>0 else 0)
        myrdf = bdf.BrushingDataframe(dataframe)
        myrdf.cleaning_missing()
        myrdf.scanning()


        """

        if input_vars:
            self = self[input_vars]

        ## Check Null Values    
        null_df = self.isna().sum().to_frame("Null Counts")
        null_df = null_df.loc[null_df ['Null Counts']>0].rename_axis('Features').reset_index()
        null_table = hv.Table(null_df, label='Features with Null Values')

        ## Provide Basic stats
        kurt_l= []
        column_l =[]
        gmean_l = []
        skew_1 = []
        for column in self.select_dtypes(include='number').columns:
            column_l.append(column)
            kurt, gmean,skew  = Stats_BS.make_stats(self[column])
            kurt_l.append(kurt)
            gmean_l.append(gmean)
            skew_1 .append(skew)
        stats_df  = pd.DataFrame(list(zip(column_l,kurt_l, gmean_l,skew_1)), columns=['Feature','Kurtosis','GMean','Skew'])
        stats_table = hv.Table(stats_df, label='Features Basic Stats')

       ## Check data types
        types_df  = self.dtypes.to_frame("Data Types").rename_axis('Features').reset_index()
        types_df ["Data Types"] = types_df ["Data Types"].astype(str)

        ## percentage unique features with total rows
        unique_feat =[]
        for feature in types_df['Features']:
            unique_feat.append(int(self[feature].nunique() / self.shape[0] * 100))
        types_df["Unique Vs Rows %"]  =   unique_feat
        types_df ['Features'] = types_df ["Features"].astype(str)
        types_df.loc[(types_df['Data Types'].str.contains("object", case=False)) & (types_df['Features'].str.contains("date", case=False) ),"Recomendation"] = "Consider convert to Date or Time type"
        types_df.loc[(types_df["Unique Vs Rows %"] > 5) & (types_df['Data Types'] == 'object') ,"Recomendation"] = "High unique categories and should be removed or transformed"
        types_df.loc[(types_df["Unique Vs Rows %"] > 80) ,"Recomendation"] = "Suspected record ID and will be removed"
        types_df = types_df.fillna("")
        typ_table = hv.Table(types_df , label='Features data types')
        ## Plot Histogram for numericals
        hist_plots = []
        for column in self._get_numeric_data().columns:
            hist_plots.append(self[column].plot.hist(bins=100, bin_range=(0, self[column].max()), title='Histogram and Box Plot ' + str(column)).opts(width=800))
            hist_plots.append(self[column].plot.box(invert=True).opts(xrotation=90,width=800))
        
        histplots = hv.Layout(hist_plots)
        ## Plot for categorical
        cat_plots = []
        for column in self.select_dtypes(include=['object']).dtypes.index:
            #if int(self[column].nunique()) < 100:
            df = pd.DataFrame()
            df = self[column].value_counts().sort_index().to_frame().reset_index().rename(columns={"index": column, column: "Counts"})
            df = df.sort_values(by='Counts', ascending=False).head(100)
            cat_plots.append( hv.Bars(df.groupby(column).sum()[["Counts"]]).opts(invert_axes=True, width=800,height=500,xrotation=45,title=column,tools=['hover']))
        catplots = hv.Layout(cat_plots)

        corr = self.corr()
        corrplots = hv.HeatMap((corr.index, corr.columns, corr.values)).opts(title='Correlation Matrix').opts(width=800,height=500,xrotation=45,tools=['hover'])
        p = (null_table.opts(height=100) + stats_table.opts(width=700, height=400) +  typ_table.opts(width=800, height=400) + catplots + histplots + corrplots ).cols(2)
        
        renderer = hv.renderer('bokeh')
        renderer.save(p, 'Beutifly_B EDA')
        Print_Msg.print_msg1("Data scan and visualization is reported under Beutifly_B EDA.html. Please check your current notebook folder. ")
        
    
    

    def recommended_transformation(self, input_vars=[], ordinal_vars=[], WOE_tresh = 10, target='',reference_date= '',test_size_in= 0.3, 
    WOE_print = False, scaler = True):
        """

        The recommended transformation provides several transformation and conversions that consist of 
        -	ordinal type conversion
            Those features numerical features identified ordinal by user will be transformed 
            to categorical such as 1st, 2nd and 3rd etc 
        -	date conversion to month    
        -	date conversion to number of days based on given reference date
        -	suspected record ID features removal
        -	categorical features transformation to numerical based on One hot encoding or Weight of Evidence 
            (WOE) based on given threshold of number of categorical values.
        -	Standard scaler is selected by default.


        Parameters
        ----------
        input_vars: list, default=Empty
        List of selected features. Default is empty where all columns will be included.

         ordinal_vars: list, default=Empty
         List of ordinal features. Default is empty where no column is included.

         WOE_tresh: float or int, default=10
         Weight of Evidence treshold of number of categorical features values that decides if categorical 
         transformation is done with OneHotencoding or WOE. 
         Examples: if WOE_tresh = 10, features with 10 unique category values will be transformed using OneHotEncoding,
         whereas those with more than 10 will be under WOE

         target: string, default = None
         Target of the data sets that will be used for test , train splitting and and WO calculation

         reference_date: string,default = None
         The reference date is the name of the feature with type date that will be used for calculation 
         of number of days against all other features with date format. 

         test_size_in: float, default = 0.3
         Tihs is the size of test data sets in percentage for the splitting between training and test. Beautifly_B will default
         the splitting with stratify as the package is for classification binary only.

         scaler: boolean, default True
         Perform standard scaler if true

        Returns
        -------
        X_train, X_test, y_train, y_test,  splittinglist, length=2 * len(arrays)
        List containing train-test split of inputs.
        Feature_names  list of feature / column names of the dataframe

        Examples
        --------
        import pandas as pd
        import Beautifly_B.BrushingDataframe as bdf
        dataframe = pd.read_csv("AUTO_LOANS_DATA.csv", sep=";")
        dataframe['BINARIZED_TARGET'] = dataframe['BUCKET'].apply(lambda x: 1 if x>0 else 0)
        myrdf = bdf.BrushingDataframe(dataframe)
        myrdf.cleaning_missing()
        myrdf.scanning() 
        X_train, X_test, y_train, y_test, feature_names  = myrdf.recommended_transformation(ordinal_vars = ['ACCOUNT_NUMBER'],
                                                                     WOE_tresh = 13,reference_date="CUSTOMER_OPEN_DATE",
                                                                  target = "BINARIZED_TARGET",scaler = True)

        Important
        The current version of Beautifly_B provides recommendation of data preparation for binary classification only.
        More functionalities in the next release.

        """

        df = self.copy()
        if input_vars:
            df = df[input_vars]
            
            
        ### Check if Ordinal features is selected 
        for column in ordinal_vars:
            new_ord = column+"_ORD"
            df[new_ord] = np.vectorize(Ordinal.make_ordinal)(df[column].values)
        try:
            df.drop(columns=ordinal_vars , axis = 1,inplace=True)
        except ValueError:
            pass        


        ### Convert feature with Date descrtiption to date
        for column in df.columns:
            if (column.lower().find('date') != -1 ) & (df[column].dtype == 'object'):
                df[column] = pd.to_datetime(df[column])
                #log_recom.append("  Convert "+column+" to Date types")
                month = str(column.upper().replace('DATE', ""))+"_MONTH"
                #df[month] = df[column].dt.month_name(locale='English') # locale has  issue with some laptop
                df[month] = df[column].dt.month_name()
                Print_Msg.print_msg1("Transformed {0} from Date to Month".format(column))
                #log_recom.append("Create new feature based on refference day ")
                if (column != reference_date) and (reference_date != '') and (reference_date in list(df.columns)):
                    new_column = str(reference_date)+"___"+str(column)
                    df[new_column] = abs(df[column] - pd.to_datetime(df[reference_date]))
                    df[new_column] = df[new_column].dt.days
                    Print_Msg.print_msg1("Transformed {0} from Date to number {1} \n of days based on target {2} ".format(column,new_column,reference_date))
                else:
                    Print_Msg.print_msg1("{0} is an invalid feature please enter valid date feature".format(reference_date))

            
        ## remove feature with same number of records
        unique_feat =[]
        for column in df.columns:
            if (df[column].nunique() / df.shape[0] * 100) >90 :
                unique_feat.append(column)
        df.drop(columns=unique_feat , axis = 1,inplace=True)
        Print_Msg.print_msg1("Delete features that suspected record ID {0}...".format(str(unique_feat[:])))

        ### Assign dummy for small categorical values features based on treshold
        dummy_feat=[]
        for column in df.columns:
            if (df[column].dtype == 'object') & (df[column].nunique() <= WOE_tresh):
                dummy_feat.append(column)
        if dummy_feat:
            dummy_df = pd.get_dummies(df[dummy_feat])
            df.drop(columns = dummy_feat, axis = 1,inplace=True)
            df = pd.concat([df, dummy_df], axis=1)
            Print_Msg.print_msg1("Replace categorical features with dummy features {0}...".format(str(dummy_feat[:])))

        ### Split 
        try:
            df = df.reset_index()
        except ValueError:
            pass
        df.drop(['index'], axis = 1,inplace=True)
        df = df.select_dtypes(exclude=['datetime64[ns]'])


        if (not target)| (target not in df.columns):
            Print_Msg.print_msg1("Please enter a valid target")
            return None,None,None,None
    
        else:
            if (len(set(df[target])) !=2):
                Print_Msg.print_msg1("Target is not binary classification and transformation is aborted")
                return None,None,None,None

            else:
                y = df[target]    
                X = df.drop([target], axis = 1) 
                X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=df[target], test_size=test_size_in)
                Print_Msg.print_msg1("Split train with {0} records and test with {1} records \n both with {2} columns ".format(str(X_train.shape[0]),str( X_test.shape[0]),str(X_train.shape[1])))
            
        ### WOE on categorical features based on treshold default 10 unique category values. Fit on training data and transform to training and test data
        ### We use WOE to reduce number of dummy features from features with high unique categorical values
                my_WOE = WOE()
                X_train.loc[:,target] = y_train
                X_test.loc[:,target] = y_test
       
                for column in df.columns:
                    if (df[column].dtype == 'object') & (df[column].nunique() > WOE_tresh):
                        my_WOE.fit(X_train,column,target)
                        X_train.loc[:,column] = my_WOE.transform(X_train,column,target)
                        X_test.loc[:,column] = my_WOE.transform(X_test,column,target)
                        Print_Msg.print_msg1("Transformed {0} from object to Weight of Evidence WOE".format(column,))
                if WOE_print:
                    Print_Msg.print_msg1("Below is created WOE dictionary")
                    print(my_WOE.get_WOE_dict())
 
                X_train = X_train.fillna(0)
                X_test = X_test.fillna(0)
                X_train.drop([target], axis = 1,inplace=True) 
                X_test.drop([target], axis = 1,inplace=True) 

                # Scaled them up
                feature_names = X_train.columns
                if scaler:
                    scaler = preprocessing.StandardScaler().fit(X_train)
                    X_train = scaler.transform(X_train)
                    X_test = scaler.transform(X_test)

                Print_Msg.print_msg1("Apply standard scaling for all input features")
                return X_train, X_test, y_train, y_test, feature_names
