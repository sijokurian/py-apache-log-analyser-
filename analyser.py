""" Parse apache log using panda  """

import pandas as pd
import glob, os
#elb_log = pd.read_csv("elb.log", sep='\s+',header=None)

column_names = ['timestamp', 'elb', 'client:port', 'backend:port', 'request_processing_time',\
'backend_processing_time', 'response_processing_time', 'elb_status_code', 'backend_status_code', \
'received_bytes', 'sent_bytes', 'request', 'user_agent', 'ssl_cipher', 'ssl_protocol']
# use your path
all_files = glob.glob(os.path.join("data/live", "*.log"))     # advisable to use os.path.join as this makes concatenation OS independent
print(all_files);
df_from_each_file = (pd.read_csv(f, sep='\s+',names = column_names) for f in all_files)
elb_log = pd.concat(df_from_each_file,ignore_index=True)


print(elb_log.describe())
#print(elb_log.head())
