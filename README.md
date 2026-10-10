# Dinoponera gigantea transcriptome project

This repository contains two analysis collections for samples AZ1, AZ2, and AZ3. The original vendor delivery and a separate local Trinity workflow are kept in dedicated folders. The [vendor_analysis/index.html](vendor_analysis/index.html) reviews the vendor workflow; [local_analysis/index.html](local_analysis/index.html) reviews the local workflow; [comparison.html](comparison.html) compares their shared steps.

There is no control/treatment design recorded for these samples. The comparison presents no differential-expression conclusions. Historical filtered count matrices and a selected normalized expression table have been recovered from the related GitHub repository as expression evidence.

## Folder map

| Location | Contents |
| --- | --- |
| `vendor_analysis/OPL_mRNA_3_24201_Analysis_Results.zip` | Original vendor results archive. |
| `vendor_analysis/extracted_report/` | Original vendor HTML report. |
| `vendor_analysis/extracted_results/` | Vendor assembly FASTA, predicted peptides, GFF3, functional annotation, per-sample expressed-gene spreadsheets, and AMP results. |
| `vendor_analysis/vendor_deliverables/` | Copies of selected vendor annotation, expression, and AMP files used by the root overview page. |
| `vendor_analysis/data/qc/busco_results/` | New BUSCO assessment of the original vendor FASTA; summary text and JSON. |
| `vendor_analysis/results/` | New BUSCO marker table, comparison CSV, and comparison figure. |
| `vendor_analysis/scripts/` | BUSCO run command, environment specification, and result export script. |
| `vendor_analysis/report_assets/` | Vendor QC images and report assets used by the root overview page. |
| `local_analysis/data/qc/` | TrinityStats and BUSCO results from the separate local assembly. |
| `local_analysis/scripts/` | Historical Trinity assembly, per-sample Salmon quantification, full-assembly annotation, and QC commands. |
| `local_analysis/data/quantification/` | Recovered gene/isoform count matrices, file guide, source scripts, and download checksums. |
| `local_analysis/results/` | BUSCO figure and percentage tables; recovered 432-gene normalized expression CSV/TSV. |
| `local_analysis/index.html` | Source-linked local analysis review. |

## Assembly provenance

The vendor FASTA contains **318,934 transcript records and 149,464,614 bases**. The local `local_analysis/data/qc/TrinityStats.txt` reports **2,944,151 transcripts and 1,069,772,028 bases**. These are different assembly outputs from the same sample project; the full local FASTA is not stored here. Do not apply local QC statistics to the vendor FASTA without verifying their provenance.

The historical local scripts reference `/home/angsuman/rna_pipeline`, which is not part of this repository. They document previous commands but are not standalone reproducible workflows here.

## Vendor BUSCO assessment

The vendor FASTA was assessed locally with BUSCO 6.1.0 in transcriptome mode and the same `eukaryota_odb12.2` release (13 May 2026) as the saved local result: **35.2% complete (44/125)**, compared with **68.0% (85/125)** in the saved local summary. This assessment was added after the original vendor delivery. See [comparison.html](comparison.html#busco) and [run provenance](vendor_analysis/data/qc/busco_run_provenance.json).
