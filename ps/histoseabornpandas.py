import seaborn as sns
import pandas as pd
dat=['I', 'I', 'DE', 'T', 'O','M','M','M', 'DE', 'T', 'M', 'F', 'DE', 'N', 'N', 'N', 'O', 'F', 'I', 'M', 'T', 'O', 'N', 'I', 'I', 'F', 'F', 'T', 'T', 'N', 'DE']
df = pd.DataFrame(dat, columns=["Sintomas"])
sns.histplot(data=df,x='Sintomas',stat="frequency",kde=True)
