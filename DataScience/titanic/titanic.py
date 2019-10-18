import numpy as pd
import pandas as pd
titanic_df = pd.read_csv('titanictrain.csv')
titanic_df ['Survived'] = titanic_df ['Survived'].map({
0: 'Died',
1: 'Survived'
})
