{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   PassengerId  Survived  Pclass  \\\n",
      "0            1      Died       3   \n",
      "1            2  Survived       1   \n",
      "2            3  Survived       3   \n",
      "3            4  Survived       1   \n",
      "4            5      Died       3   \n",
      "\n",
      "                                                Name     Sex   Age  SibSp  \\\n",
      "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
      "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
      "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
      "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
      "4                           Allen, Mr. William Henry    male  35.0      0   \n",
      "\n",
      "   Parch            Ticket     Fare Cabin Embarked  \n",
      "0      0         A/5 21171   7.2500   NaN        S  \n",
      "1      0          PC 17599  71.2833   C85        C  \n",
      "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
      "3      0            113803  53.1000  C123        S  \n",
      "4      0            373450   8.0500   NaN        S  \n"
     ]
    }
   ],
   "source": [
    "import numpy as pd\n",
    "import pandas as pd\n",
    "titanic_df = pd.read_csv('titanictrain.csv')\n",
    "titanic_df ['Survived'] = titanic_df ['Survived'].map({\n",
    "0: 'Died',\n",
    "1: 'Survived'\n",
    "})\n",
    "titanic_df.drop(['Parch','PassengerId','Name','Ticket','Embarked'], axis=1,inplace=False)\n",
    "titanic_df[\"Embarked\"]=titanic_df[\"Embarked\"].fillna(\"S\")\n",
    "print(titanic_df.head(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   PassengerId  Survived          Pclass  \\\n",
      "0            1      Died  Business Class   \n",
      "1            2  Survived         Economy   \n",
      "2            3  Survived  Business Class   \n",
      "3            4  Survived         Economy   \n",
      "4            5      Died  Business Class   \n",
      "\n",
      "                                                Name     Sex   Age  SibSp  \\\n",
      "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
      "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
      "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
      "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
      "4                           Allen, Mr. William Henry    male  35.0      0   \n",
      "\n",
      "   Parch            Ticket     Fare Cabin Embarked  \n",
      "0      0         A/5 21171   7.2500   NaN        S  \n",
      "1      0          PC 17599  71.2833   C85        C  \n",
      "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
      "3      0            113803  53.1000  C123        S  \n",
      "4      0            373450   8.0500   NaN        S  \n"
     ]
    }
   ],
   "source": [
    "titanic_df ['Pclass'] = titanic_df ['Pclass'].map({\n",
    "    1: 'Economy',\n",
    "    2: 'Luxury',\n",
    "    3: 'Business Class'\n",
    "})\n",
    "print(titanic_df.head(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
