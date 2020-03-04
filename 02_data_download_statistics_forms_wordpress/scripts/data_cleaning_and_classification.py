 #!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np

#Reading dataframe
df = pd.read_csv("clean_mail_20190603.csv", sep=',', encoding='utf-8') 
result=df.dropna(how='all')
result.to_csv(str("wordpress.csv"), sep=',', encoding='utf-8', index=False)

