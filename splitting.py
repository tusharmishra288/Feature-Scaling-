
import pandas as pd
import sklearn.model_selection as sk
#reading data and storing to a dataframe
Read_csv_filename = 'realEstate_trans.csv'
Read_csv_data = pd.read_csv(Read_csv_filename)

# specify what proportion of data to hold out for testing
test_size = 0.33

# select the independent and dependent variables
x = Read_csv_data[['zip', 'beds', 'sq__ft']]
y = Read_csv_data['price']

x_train, x_test, y_train, y_test = sk.train_test_split(x, y, test_size=0.33)

#creating Dataframe for training data
X_train = pd.DataFrame(x_train)
X_train['price'] = y_train
print("Printing Training data", X_train.head(10))

#creating Dataframe for testing_data
X_test =  pd.DataFrame(x_test)
X_test['price'] = y_test
print("Printing Testing data", X_test.head(10))

# output the samples to files
# names of the files to output the samples
w_filenameTrain = 'output/realEstate_train.csv'
w_filenameTest  = 'output/realEstate_test.csv'
with open(w_filenameTrain,'w+') as write_csv:
    write_csv.write(X_train.to_csv(sep=',', index=False))

with open(w_filenameTest,'w+') as write_csv:
    write_csv.write(X_test.to_csv(sep=',', index=False))
