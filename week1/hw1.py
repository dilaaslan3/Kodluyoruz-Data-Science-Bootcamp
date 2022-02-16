import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataOperations:
    ''' DataOperations class gets different 
        types of data and transforms 
        it to the Pandas Dataframe.
    '''

    def __init__(self, data=None):
        self.data = data
        self.df = self.get_data()


    def get_data(self):
        ''' Check the data type and 
            if data type is a numpy array 
            converts it to pandas dataframe.

            If the data type is pandas
            dataframe, do not perfom any operation.

            If json or csv file is given
            check their extensions and save 
            them as a pandas dataframe.

            If no data is given, 
            generate random pandas dataframe.

            Returns: Dataframe
        '''
        if isinstance(self.data, np.ndarray):
            df = self.numpy_to_df()
        
        elif isinstance(self.data, pd.DataFrame):
            df = self.data
        
        elif type(self.data) == str:

            if self.data.endswith(".csv"):
                df= pd.read_csv(self.data)
                
            elif self.data.endswith(".json"):
                df = pd.read_json(self.data)
            
        else:   
            df = self.generate_random_df()
            
        return df


    def numpy_to_df(self):
        ''' Converts the numpy array to the dataframe

            Returns: Dataframe
        '''
        index = ['Row_' + str(i) for i in range(1, len(self.data) + 1)]
        columns = ['Column_' + str(i) for i in range(1, len(self.data[0]) + 1)]
        return pd.DataFrame(self.data ,index = index, columns = columns)

    
    def generate_random_df(self):
        ''' Generate random numpy array 
            and convert it to the pandas dataframe.
            
            Returns: Dataframe 
        '''
        random_data = np.random.randint(100, size=(100, 10))
        columns = ['Column_' + str(i) for i in range(1, len(random_data[0]) + 1)]
        return pd.DataFrame(random_data, columns = columns)


    def analyze_data(self):
        ''' Analyze the dataframe.
        '''
        print("Shape of the data: \n", self.df.shape)
        print("\nChecking null values: \n", self.df.isnull().sum())
        #print("\nGeneral information of the data: \n", df.info())
        print("\nNumeric features distribution: \n", self.df.describe())
    

    def visualize_data(self):
        ''' Visualize the dataframe.
        '''
        self.scatter_plot()    
        self.line_plot()
        self.box_plot()
        self.hist_plot()
    
    
    def scatter_plot(self):
        ''' Visualize the dataframe as scatter plot.
        '''
        plt.figure(figsize=(10,8))
        sns.scatterplot(data=self.df, x=self.df.columns[0], y=self.df.columns[1], hue=self.df.columns[-1])
        plt.show()


    def line_plot(self):
        ''' Visualize the dataframe as line plot.
        '''
        colum_len = self.df.shape[1]
        self.df.plot(subplots=True, layout=(colum_len,2), figsize=(16,8))
        plt.show()


    def box_plot(self):
        ''' Visualize the dataframe as box plot.
        '''
        plt.figure(figsize=(10,8))
        sns.boxplot(data=self.df)
        plt.show()


    def hist_plot(self):
        ''' Visualize the dataframe as histogram plot.
        '''
        plt.figure(figsize=(10,8))
        sns.histplot(data=self.df)
        plt.show()


def main():
    #data_op = DataOperations(np.array([[15, 22, 43], [33, 24, 56]]))
    #data_op = DataOperations(pd.read_csv("test_data.csv"))
    #data_op = DataOperations("test_data.json")
    #data_op = DataOperations("test_data.csv")
    data_op = DataOperations()
    data_op.analyze_data()
    data_op.visualize_data()


if __name__ == "__main__":
    main()
