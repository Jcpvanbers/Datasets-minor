#Gedeelde file voor functies gebruikt in de notebook
import pandas as pd
from IPython.display import display

def init_analyse(df) -> None:
    print("informatie over dataframe:")
    df.info()
    #.info geeft informatie over het aantal records, kolommen en de datatypes.
    # Geeft een goed eerste idee van de dataset en eventuele afwijkingen in de verwachtingen.
    print()
    print(f"aantal gedupliceerde rijen: {df.duplicated().sum()}")
    #df. duplicated controleert de dataset op rijen binnen de set die exact dezelde waarden hebben.
    print()
    print("Overzicht van lege waarden:")
    display(df.isna().sum())
    #df.isna controleert alle kolommen binnen de dataframe op lege waarden. 
    print()
    print("Aantal unieke waarden:")
    display(df.nunique())
    print()
    print("Eerste 20 rijen:")
    display(df.head(20))
    #Laat de eerste 20 records zien, geeft een beeld van hoe data wordt weergeven en samenhangt.
    print()
    print("Laatste 20 rijen:")
    display(df.tail(20))
    #Hetzelfde als head, maar dan voor de laatste 20 records. Afhankelijk van sortering kan dit andere inzichten geven.