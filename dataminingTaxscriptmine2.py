import pandas as pd
import numpy as np

#have 2018

#2017-------------------------------------------------------------------------------------------

#Specify File location and names
fileName2017 = '/Users/annemariedonohue/Downloads/17zpallagi.csv'
cbsaFile= '/Users/annemariedonohue/Downloads/datasets/ziptocbsa2018.csv'
outputFile2017 = '/Users/annemariedonohue/Downloads/dataminingTaxes2017.csv'

#Import zip to cbsa Mapping, this has 7900 duplicate rows of duplicate zip codes
cbsa = pd.read_csv(cbsaFile)
cbsa = cbsa.sort_values(by = 'res_ratio', ascending = False) #Sort by ratio descending

#Now drop a row if the zip code has already appeared.
#Because we sorted by ratio, it will keep the row with the highest ratio
cbsa = cbsa.drop_duplicates(subset = 'zip', keep = 'first')

#Read Tax information
df = pd.read_csv(fileName2017)
df['id'] = np.arange(len(df)) #Add id column (row number). This column is unique

joinedTable1 = df.merge(cbsa, 'inner', left_on='zipcode', right_on = 'zip') #Join the two tables

#print(joinedTable.id.duplicated().sum()) #Shows no duplicate rows 
joinedTable1.to_csv(outputFile2017)

#2016-------------------------------------------------------------------------------------------
#Specify File location and names
fileName2016 = '/Users/annemariedonohue/Downloads/16zpallagi.csv'
outputFile2016 = '/Users/annemariedonohue/Downloads/dataminingTaxes2016.csv'

#Read Tax information
df = pd.read_csv(fileName2016)
df['id'] = np.arange(len(df)) #Add id column (row number). This column is unique
joinedTable2 = df.merge(cbsa, 'inner', left_on='zipcode', right_on = 'zip') #Join the two tables
#print(joinedTable.id.duplicated().sum()) #Shows no duplicate rows 
joinedTable2.to_csv(outputFile2016)



#2015-------------------------------------------------------------------------------------------
#Specify File location and names
fileName2015 = '/Users/annemariedonohue/Downloads/15zpallagi.csv'
outputFile2015 = '/Users/annemariedonohue/Downloads/dataminingTaxes2015.csv'

#Read Tax information
df = pd.read_csv(fileName2015)
df['id'] = np.arange(len(df)) #Add id column (row number). This column is unique
joinedTable3 = df.merge(cbsa, 'inner', left_on='zipcode', right_on = 'zip') #Join the two tables
#print(joinedTable.id.duplicated().sum()) #Shows no duplicate rows 
joinedTable3.to_csv(outputFile2015)



#2014-------------------------------------------------------------------------------------------
#Specify File location and names
fileName2014 = '/Users/annemariedonohue/Downloads/14zpallagi.csv'
outputFile2014 = '/Users/annemariedonohue/Downloads/dataminingTaxes2014.csv'

#Read Tax information
df = pd.read_csv(fileName2014)
df['id'] = np.arange(len(df)) #Add id column (row number). This column is unique
joinedTable4 = df.merge(cbsa, 'inner', left_on='zipcode', right_on = 'zip') #Join the two tables
#print(joinedTable.id.duplicated().sum()) #Shows no duplicate rows 
joinedTable4.to_csv(outputFile2014)


#merging all 5 tg--------------------------------------------------------------------------------
fileName2018 = '/Users/annemariedonohue/Downloads/datasets\ \(1\)/joinedData.csv'
taxesallyears= '/Users/annemariedonohue/Downloads/dataminingTaxesAllYears.csv'
filenames= [joinedTable4, joinedTable3, joinedTable2, joinedTable1]
#combining all files
combined_df = pd.concat(filenames, ignore_index=True)

print(combined_df)
"""
#dropping all columns except these (note the ID col isnt named)
cols_to_keep = [' ', 'zip', 'state', 'A00100']
df[cols_to_keep].to_hdf(taxesallyears)
df.columns = ['ID Number', 'Zip Code', 'State', 'Tax with AGI']   
df['ID Number'] = np.arange(len(df))
print(combined_df.id.duplicated().sum())
combined_df.to_csv(taxesallyears)
"""

