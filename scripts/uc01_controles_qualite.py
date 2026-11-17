
from pathlib import Path
import csv
import hashlib
import time

# ============================================================
# UC-01 — Contrôles exploratoires de qualité des données
# Retail Intelligence Platform
# Bibliothèques standard Python uniquement
# ============================================================

ROOT = Path(__file__).resolve().parent.parent

OUTPUT = ROOT / "UC01_preuves" / "05_controles_qualite"
OUTPUT.mkdir(parents=True, exist_ok=True)

# Nombre de champs observé dans les fichiers .dat
EXPECTED = {
    "store_sales": 23,
    "web_sales": 34,
    "item": 22,
    "inventory": 4,
    "customer": 18,
    "date_dim": 28,
}

SAMPLE_SIZE = 10_000

CSV_PATH = OUTPUT / "controles_qualite.csv"

FIELDNAMES = [
    "Source",
    "Table",
    "Rows",
    "Expected_Columns",
    "Invalid_Structure_Rows",
    "Rows_With_Missing",
    "Empty_Fields",
    "Negative_Fields",
    "Sample_Rows_Checked",
    "Sample_Exact_Duplicate_Rows",
]

results = []


def save_results():
    """Sauvegarder progressivement les résultats."""
    with CSV_PATH.open(
        "w", newline="", encoding="utf-8-sig"
    ) as output_file:
        writer = csv.DictWriter(
            output_file,
            fieldnames=FIELDNAMES,
            delimiter=";"
        )
        writer.writeheader()
        writer.writerows(results)


def analyze_file(source, table, expected_columns):
    """Analyser un fichier ligne par ligne, sans tout charger en RAM."""

    path = ROOT / source / table / f"{table}.dat"

    if not path.exists():
        print(f"[ABSENT] {path}", flush=True)
        return None

    total_rows = 0
    invalid_rows = 0
    rows_with_missing = 0
    empty_fields = 0
    negative_fields = 0

    sample_rows_checked = 0
    sample_duplicate_rows = 0

    # Maximum 10 000 empreintes conservées en mémoire
    seen = set()

    start = time.perf_counter()

    print(f"\n[DEBUT] {source}/{table}", flush=True)

    with path.open(
        "r",
        encoding="utf-8",
        errors="replace",
        buffering=1024 * 1024
    ) as file:

        for line in file:
            total_rows += 1

            fields = line.rstrip("\r\n").split("|")

            # 1. Vérification du nombre de colonnes
            if len(fields) != expected_columns:
                invalid_rows += 1

            # 2. Valeurs manquantes
            missing = fields.count("")

            empty_fields += missing

            if missing > 0:
                rows_with_missing += 1

            # 3. Valeurs numériques négatives
            # Contrôle exploratoire, sans jugement métier
            for value in fields:
                if value.startswith("-"):
                    try:
                        if float(value) < 0:
                            negative_fields += 1
                    except ValueError:
                        pass

            # 4. Doublons exacts sur un échantillon
            if total_rows <= SAMPLE_SIZE:
                sample_rows_checked += 1

                digest = hashlib.blake2b(
                    line.rstrip("\r\n").encode("utf-8"),
                    digest_size=16
                ).digest()

                if digest in seen:
                    sample_duplicate_rows += 1
                else:
                    seen.add(digest)

            # Afficher la progression toutes les 500 000 lignes
            if total_rows % 500_000 == 0:
                elapsed = time.perf_counter() - start

                print(
                    f"  {total_rows:,} lignes analysées "
                    f"en {elapsed:.1f} secondes",
                    flush=True
                )

    elapsed = time.perf_counter() - start

    print(
        f"[TERMINE] {source}/{table} : "
        f"{total_rows:,} lignes, "
        f"{invalid_rows} lignes mal structurées, "
        f"{sample_duplicate_rows} doublons dans l'échantillon "
        f"({elapsed:.1f} s)",
        flush=True
    )

    return {
        "Source": source,
        "Table": table,
        "Rows": total_rows,
        "Expected_Columns": expected_columns,
        "Invalid_Structure_Rows": invalid_rows,
        "Rows_With_Missing": rows_with_missing,
        "Empty_Fields": empty_fields,
        "Negative_Fields": negative_fields,
        "Sample_Rows_Checked": sample_rows_checked,
        "Sample_Exact_Duplicate_Rows": sample_duplicate_rows,
    }


def main():
    print("=" * 65)
    print("UC-01 — CONTROLES DE QUALITE")
    print("=" * 65)

    global_start = time.perf_counter()

    for source in ["data", "data_refresh"]:
        for table, expected_columns in EXPECTED.items():

            result = analyze_file(
                source,
                table,
                expected_columns
            )

            if result is not None:
                results.append(result)

                # Sauvegarde après chaque fichier terminé
                save_results()

    total_time = time.perf_counter() - global_start

    print("\n" + "=" * 65)
    print("ANALYSE TERMINEE")
    print(f"Fichiers analysés : {len(results)}")
    print(f"Durée totale : {total_time:.1f} secondes")
    print(f"Résultats : {CSV_PATH}")
    print("=" * 65)


if __name__ == "__main__":
    main()
