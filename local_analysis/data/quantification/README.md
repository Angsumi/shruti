# Recovered local expression data

Downloaded on 7 October 2026 from https://github.com/Angsumi/RNA_DE_Novo_Analysis at commit `970c3a51eb0764c66f01340425acbffeec75e04e`.

## File organization

- `count_matrices/gene_level/`: three tab-separated gene count files for AZ1/AZ2, AZ1/AZ3, and AZ2/AZ3.
- `count_matrices/isoform_level/`: three tab-separated isoform count files for the same sample pairs.
- `../../results/tables/csv/de_genes_expression_matrix.csv` and `../../results/tables/tsv/de_genes_expression_matrix.tsv`: the same 432-gene TMM-normalized expression subset with AZ1, AZ2, and AZ3 columns.
- `provenance/source_scripts/`: six historical edgeR scripts documenting count export and the table export script documenting normalized expression. These are archived provenance, not a runnable workflow in this folder.
- `provenance/download_manifest.json`: source URLs, pinned commit, Git blob checksums, SHA-256 checksums, file sizes, row counts, and sample columns.

## What the values mean

The `.edgeR.count_matrix` files are plain tab-separated text, despite their unusual extension. The first column contains Trinity IDs; the two named columns contain sample counts. The header omits a label for the ID column, so it has one fewer field than each data row.

The source edgeR scripts round the original counts and filter to CPM > 1 in both samples before exporting these files. The gene matrices contain 17,564, 16,776, and 18,649 rows; the isoform matrices contain 28,083, 26,253, and 29,480 rows for AZ1/AZ2, AZ1/AZ3, and AZ2/AZ3 respectively. These are comparison-specific filtered subsets. Missing rows or sample values must not be interpreted as zero expression.

The 432-gene table is identified by the export script as TMM-normalized expression from a historical selected-gene analysis. It is a subset, and should not be labelled TPM or used as the full original abundance matrix. The complete source normalization matrix is unavailable here.

Original Salmon `quant.sf` files, Salmon logs, and the complete original gene and isoform count matrices remain unavailable. The recovered files establish retained expression values; their direct derivation from Salmon cannot be independently verified from the retained quantification files. No control/treatment design is recorded, and recovery of these tables does not validate the historical differential-expression conclusions.

Downloaded bytes were preserved and verified against the Git blob checksums in the pinned GitHub tree. These files were not produced by a new local quantification run.
