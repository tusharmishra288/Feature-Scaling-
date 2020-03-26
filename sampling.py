

import pandas as pd
bed_nos = [2,3,4]
Read_csv_filename = 'realEstate_trans.csv'
Read_csv_data = pd.read_csv(Read_csv_filename)

# select  zip, city, price, beds,sq__ft from Read_csv_data  where bed < 5
Read_csv_query_data = Read_csv_data.query('beds' == 'bed_nos')[['zip', 'city', 'price', 'beds', 'sq__ft']]

strata_frac = 0.2

# calculate the expected counts
strata_expected_counts = Read_csv_query_data['beds'].value_counts() * strata_frac

# and select the sample
sample = pd.DataFrame()
data=Read_csv_query_data.sample(frac=strata_frac)
for bed in bed_nos:
    sample = sample.append(
        Read_csv_query_data.query('beds' == 'bed').sample(frac=strata_frac),
        ignore_index=True
    )

# check if the counts selected match those expected
strata_sampled_counts = sample['beds'].value_counts()
print('Expected: ', strata_expected_counts)
print('Sampled: ', strata_sampled_counts)

# output to the file
with open('output/realEstate_trans_sampling.csv','w+') as write_csv:
    write_csv.write(sample.to_csv(sep=',', index=False))