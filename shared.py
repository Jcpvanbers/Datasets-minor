#Gedeelde file voor functies gebruikt in de notebook
import pandas as pd
from IPython.display import display

def init_analyse(df) -> None:
    print("informatie over dataframe:")
    df.info()
    print()
    print(f"aantal gedupliceerde rijen: {df.duplicated().sum()}")
    print()
    print("Overzicht van lege waarden:")
    display(df.isna().sum())
    print()
    print("Eerste 20 rijen:")
    display(df.head(20))
    print()
    print("Laatste 20 rijen:")
    display(df.tail(20))