Evidence — Representative Data Samples

Representative samples were extracted from the main dataset to examine the structure and content of the source files.

The selected files cover store sales, web sales, products, customers, inventory, dates, and returns.

The samples were used to inspect field delimiters, record structure, and example values. A sample from data_refresh/store_sales/ was also extracted to support an initial comparison between the main and refresh datasets.

These samples provide evidence of the source structure but do not constitute a complete data quality assessment.


observations

An initial inspection was performed on representative records from the main and refresh datasets.

The store_sales.dat file contains 23 fields per record in the inspected sample, while web_sales.dat contains 34 fields. The item.dat and inventory.dat files contain 22 and 4 fields respectively.

The inspected record from data_refresh/store_sales/store_sales.dat also contains 23 fields, suggesting that the main and refresh store sales files share a similar structure.

A negative value (-1902.80) was observed in the final field of the first refresh store sales record. This value has been flagged for further investigation, as its business meaning and validity have not yet been confirmed.

These findings are preliminary and will be validated against the reference schema and additional data quality checks.

Evidence location: UC01_preuves/03_apercu_fichiers/.