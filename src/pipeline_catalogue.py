import pandas as pd
import os

data_path = "./data"
out_path = "./out"

# Charger fichiers
catalog_fr = pd.read_csv(os.path.join(data_path, "catalog_fr.csv"))
catalog_us = pd.read_csv(os.path.join(data_path, "catalog_us.csv"))
mapping_categories = pd.read_csv(os.path.join(data_path, "mapping_categories.csv"))

# Ajouter indicateur de pays
catalog_fr["pays"] = "FR"
catalog_us["pays"] = "US"

# Conversion US → € et kg
if "price" in catalog_us.columns:
    catalog_us["price"] = catalog_us["price"] * 0.95  # $ → €
if "weight" in catalog_us.columns:
    # convertir lb → kg, laisser kg tel quel
    catalog_us.loc[catalog_us["weight_unit"].str.lower() == "lb", "weight"] *= 0.453592
    catalog_us["weight_unit"] = "kg"

# Fusionner catalogues
catalog = pd.concat([catalog_fr, catalog_us], ignore_index=True)

# Fusionner avec mapping des catégories
catalog = catalog.merge(mapping_categories, how="left", left_on="category", right_on="source_category")
catalog["categorie_finale"] = catalog["target_category"].fillna(catalog["category"])

# Supprimer doublons SKU (garder prix le plus élevé)
catalog = catalog.sort_values("price", ascending=False)
catalog = catalog.drop_duplicates(subset="sku")

# KPI qualité
kpi = pd.DataFrame({
    "total_produits_avant": [len(catalog_fr) + len(catalog_us)],
    "total_produits_apres": [len(catalog)],
    "produits_sans_categorie": [catalog["categorie_finale"].isna().sum()]
})

# Sauvegarde
catalog.to_csv(os.path.join(out_path, "catalog_canonique.csv"), index=False)
kpi.to_csv(os.path.join(out_path, "kpi_catalogue.csv"), index=False)

print("Pipeline catalogue terminé. Fichiers générés dans 'out/'")
