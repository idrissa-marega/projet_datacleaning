import pandas as pd
import re

def nettoyer_email(df, col="email"):
    """Nettoyer et standardiser les emails"""
    df[col] = (
        df[col].astype(str)
        .str.strip()
        .str.replace(r"\s+", "", regex=True)
        .str.lower()
    )
    return df

def uniformiser_pays(df, col="pays"):
    """Uniformiser les noms de pays selon un mapping"""
    pays_map = {'fr':'France', 'FR':'France', 'ch':'Switzerland', 'be':'Belgium', 'usa':'USA'}
    df[col] = (
        df[col].astype(str)
        .str.strip()
        .str.lower()
        .map(pays_map)
        .fillna(df[col])
    )
    return df

def normaliser_telephone(numero):
    """Mettre les numéros de téléphone au format international"""
    numero = re.sub(r"\D+", "", str(numero))
    if numero.startswith("0") and len(numero) == 10:
        return "+33" + numero[1:]
    return numero

def supprimer_doublons(df):
    """Supprimer les doublons en gardant la ligne la plus complète"""
    df['completude'] = df[['email','telephone','pays','naissance']].notna().sum(axis=1)
    df = df.sort_values('completude', ascending=False)
    df = df.drop_duplicates(subset=['nom','prenom','email'])
    df = df.drop(columns='completude')
    return df
