import pandas as pd
import os
from utils_cleaning import nettoyer_email, uniformiser_pays, normaliser_telephone, supprimer_doublons

#  Définir les chemins
data_path = "./data"
out_path = "./out"



# Charger le fichier clients.csv


df_clients = pd.read_csv(os.path.join(data_path, "clients.csv"))
print(df_clients.head())


# KPI avant nettoyage
kpi = pd.DataFrame({
    "total_clients_avant": [len(df_clients)],
    "emails_vides_avant": [df_clients['email'].isna().sum()],
    "telephones_vides_avant": [df_clients['telephone'].isna().sum()]
})

#  Nettoyage
df_clients = nettoyer_email(df_clients)
df_clients = uniformiser_pays(df_clients)
df_clients['telephone'] = df_clients['telephone'].apply(normaliser_telephone)
df_clients = supprimer_doublons(df_clients)

#  KPI après nettoyage
kpi['total_clients_apres'] = len(df_clients)
kpi['emails_vides_apres'] = df_clients['email'].isna().sum()
kpi['telephones_vides_apres'] = df_clients['telephone'].isna().sum()

#  Sauvegarde des fichiers
df_clients.to_csv(os.path.join(out_path, "clients_clean.csv"), index=False)
kpi.to_csv(os.path.join(out_path, "kpi_qualite.csv"), index=False)

print(" Nettoyage terminé. Fichiers générés dans 'out/'")
