### Inventory Scope and Exclusions

During the initial file inventory, 79 files were detected. However, this count included Python environment files located in `data/.venv/` and a nested copy of the refresh dataset under `data/data_refresh/`.

These files were excluded from the business data inventory to avoid counting technical dependencies and duplicated source files.

After applying these exclusions, the expected inventory consists of 36 business data files: 24 files in `data/` and 12 files in `data_refresh/`.

The original files were preserved. Only the inventory selection criteria were modified.