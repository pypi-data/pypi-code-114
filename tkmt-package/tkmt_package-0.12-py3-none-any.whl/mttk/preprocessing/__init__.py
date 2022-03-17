class Preprocessing:
    def __init__(self):
          pass


    def data_preparation(self,dataset):
          """
           Assigns the dependent and the independent variables. 
           
           Parameters
           ----------
           X: input/dependent variables; returns all columns except the last. 
           y: output/ independent variable; returns the last column only.
           
           Example
           --------
           >>> from Ensemble_Learning import Average_weight_Ensemble
           >>> dy = df[['cycle','voltage', 'current', 'temperature']]
           >>> awe = Average_weight_Ensemble()
           >>> X1,y1= awe.data_preparation(dy)
           
          """
          import pandas as pd
          import numpy as np
          self.dataset  = dataset
          self.X        = self.dataset.iloc[:,:-1]
          self.y        = self.dataset.iloc[:,-1]
          return self.X, self.y
        
    def data_normalization(self):
          """
          Rescales the data such that all the feature values are in the range 0 to 1.
          
          Parameters
          ----------
          X_scal: scaled dependent variables; 
                  returns all columns except last with its values rescaled between 0 to 1.
                  
          y_scal: scaled independent variables;  
                  returns the last column with its values rescaled between 0 to 1.
          
          Example
          -------
          >>> from Ensemble_Learning import Average_weight_Ensemble
          >>> awe = Average_weight_Ensemble()
          >>> X_scal,y_scal = awe.data_normalization()
          
          """
          import pandas as pd
          import numpy as np
          from sklearn.preprocessing import MinMaxScaler

          self.X,self.y = self.data_preparation(self.dataset)
        
          self.X = self.X.values
          self.y = self.y.values.reshape(-1,1)
        
          self.scaled  = MinMaxScaler(feature_range=(0.1, 1.1))
          self.scaled_y = MinMaxScaler(feature_range=(0.1, 1.1))
          
          self.X_scaled  = self.scaled.fit_transform(self.X)
          self.y_scaled  = self.scaled_y.fit_transform(self.y)
            
          self.y_scaled  = self.y_scaled.reshape(-1)
        
          return self.X_scaled,self.y_scaled

    def data_split_train_test(self,sample_X,sample_y):
          """
          Splits the data such that 80% of the data goes for training 
          and 20% of the data goes for testing with the random state as 42.
          
          Parameters
          ----------
          X_train: 80% of the data in X.
          X_test: 20% of the data in X.
          y_train: 80% of the data in y.
          y_test: 20% of the data in y.
          
          Example
          -------
          >>> from Ensemble_Learning import Average_weight_Ensemble
          >>> awe = Average_weight_Ensemble()
          >>> X_train,X_test,y_train,y_test = awe.data_split_train_test(X,y)
          
          """
          import pandas as pd
          import numpy as np
          from sklearn.model_selection import train_test_split

          self.sample_X = sample_X
          self.sample_y = sample_y
          self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.sample_X,self.sample_y,train_size=0.8,random_state=42)
          return self.X_train, self.X_test, self.y_train, self.y_test

    def performance_evaluation(self,true,pred):
        
                import numpy as np 
                true = np.array(true).reshape(-1)
                pred = np.array(pred).reshape(-1)

                mae  = np.mean(np.abs(true-pred))
                mse  = np.mean(np.square(true-pred))
                mape = np.mean(np.abs(true-pred)/true)*100
                rmse = np.sqrt(mse)
                r2   = 1-np.mean(np.square(true-pred))/np.mean(np.square(true-np.mean(true)))

                return print("MAE: {}\nMSE: {}\nRMSE: {}\nMAPE: {}\nR^2 score: {}".format(mae,mse,rmse,mape,r2))
            
    def get_plot(self,true,pred,ascending,label):
            import pandas as pd
            import numpy as np 
            import matplotlib.pyplot as plt
            
            true = np.array(true).reshape(-1,1)
            pred = np.array(pred).reshape(-1,1)

            real   = self.scaled_y.inverse_transform(true)
            y_pred = self.scaled_y.inverse_transform(pred)

            dataset = pd.DataFrame({"real":real.reshape(-1),"predict":y_pred.reshape(-1)}).sort_values('real',ascending=ascending)
            datapoints = np.arange(1, dataset.shape[0]+1)
            #print(len(datapoints),dataset.shape)
            plt.figure(figsize=(8,4))
            plt.plot(datapoints,dataset.real,label   = "{} (Real)".format(label))
            plt.plot(datapoints,dataset.predict,label= "{} (Pred)".format(label))
            plt.xlim(np.min(datapoints),np.max(datapoints))
            plt.xlabel("Datapoints")
            plt.ylabel("Actual vs Predicted {}".format(label))
            plt.legend()
            plt.grid()
            plt.show()
            return dataset.real,dataset.predict

Preprocessing.__doc__