#!/usr/bin/env bash
set -euo pipefail
vendor_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
runtime_bin="$vendor_root/../.runtime/busco-env/bin"
if [[ -x "$runtime_bin/busco" ]]; then
  export PATH="$runtime_bin:$PATH"
fi
busco_bin=${BUSCO_BIN:-busco}
"$busco_bin" \
  --in "$vendor_root/extracted_results/OPL_mRNA_3_24201_Analysis_Results/Transcriptome DeNovo Assembly/Dinoponera gigantea Assembly.fa" \
  --mode transcriptome \
  --lineage_dataset eukaryota_odb12.2 \
  --out busco_results \
  --out_path "$vendor_root/data/qc" \
  --download_path "$vendor_root/data/qc/busco_downloads" \
  --cpu 12 \
  --opt-out-run-stats "$@"
