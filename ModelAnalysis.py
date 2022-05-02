import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats


data=pd.read_csv("logs/Logs.csv")
df = pd.DataFrame(data=data)

def jaro_winkler_plot():
    sns.boxplot(x="model", y="string", data=df)
    plt.savefig('jaro_winkler.png',dpi=300)

def levenshtein_plot():
    sns.boxplot(x="model", y="distance", data=df)
    plt.savefig('levenshtein.png', dpi=300)
def densityplot ():
    sns.kdeplot(data=df, x="string", hue="model", multiple="stack")
    plt.savefig('images/density_string.png', dpi=300)

dfStatesstring = df.groupby("model")['string'].describe()
dfStatesdistance = df.groupby("model")['distance'].describe()
Googledf = df[(df['model'] == 'Google')]
Sphinxdf = df[df['model'] == 'Sphinx']
Witdf = df[df['model'] == 'Wit']


print(dfStatesstring)
print(dfStatesdistance)
print(stats.levene(Googledf['string'], Witdf['string'],Sphinxdf['string'])) #homogeneity of variances is there, leveneResult(statistic=0.5496649719376462, pvalue=0.5812382860284221)
print('Google string',stats.shapiro(Googledf['string']))
print('Sphinx string',stats.shapiro(Sphinxdf['string']))
print('Wit string',stats.shapiro(Witdf['string']))
print('Google distance',stats.shapiro(Googledf['distance']))
print('Sphinx distance',stats.shapiro(Sphinxdf['distance']))
print('Wit distance',stats.shapiro(Witdf['distance']))

print('Google - Wit: string',stats.ttest_ind(Googledf['string'], Witdf['string'], equal_var=False))

print('Google - Wit: distance',stats.ttest_ind(Googledf['distance'], Witdf['distance'], equal_var=False))