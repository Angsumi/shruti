"""Export the vendor BUSCO categories and a comparison with the saved local run."""
import csv
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

VENDOR = Path(__file__).resolve().parents[1]
ROOT = VENDOR.parent
vendor_summary = next((VENDOR / "data/qc/busco_results").glob("short_summary.specific.*.json"))
local_summary = next((ROOT / "local_analysis/data/qc/busco_results").glob("short_summary.specific.*.json"))
documents = [json.loads(p.read_text()) for p in (vendor_summary, local_summary)]
categories = [
    ("Complete single-copy", "Single copy BUSCOs", "Single copy percentage", "#1c7554"),
    ("Complete duplicated", "Multi copy BUSCOs", "Multi copy percentage", "#64ac8b"),
    ("Fragmented", "Fragmented BUSCOs", "Fragmented percentage", "#e5b94c"),
    ("Missing", "Missing BUSCOs", "Missing percentage", "#b4bec0"),
]
tables = VENDOR / "results/tables"
figures = VENDOR / "results/figures"
tables.mkdir(parents=True, exist_ok=True)
figures.mkdir(parents=True, exist_ok=True)
marker_table = next((VENDOR / "data/qc/busco_results").glob("run_*/full_table.tsv"))
shutil.copyfile(marker_table, tables / "busco_full_table.tsv")
input_fasta = Path(documents[0]["parameters"]["in"])
digest = hashlib.sha256()
with input_fasta.open("rb") as handle:
    for chunk in iter(lambda: handle.read(1024 * 1024), b""):
        digest.update(chunk)
provenance = {
    "assessment": "New local BUSCO assessment of the original vendor nucleotide FASTA",
    "part_of_original_vendor_delivery": False,
    "input_relative_path": str(input_fasta.relative_to(ROOT)),
    "input_sha256": digest.hexdigest(),
    "command": "bash vendor_analysis/scripts/run_busco.sh --offline",
    "software_versions": documents[0]["versions"],
    "lineage_dataset": documents[0]["lineage_dataset"],
    "mode": documents[0]["parameters"]["mode"],
    "summary_relative_path": str(vendor_summary.relative_to(ROOT)),
    "exported_at_utc": datetime.now(timezone.utc).isoformat(),
    "comparison_source": str(local_summary.relative_to(ROOT)),
    "same_lineage_release": documents[0]["lineage_dataset"] == documents[1]["lineage_dataset"],
}
(VENDOR / "data/qc/busco_run_provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
with (tables / "busco_comparison.csv").open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["Assembly", "Category", "BUSCO_groups", "Percentage"])
    for name, doc in zip(["Vendor assembly (new assessment)", "Local assembly (saved result)"], documents):
        result = doc["results"]
        assert sum(result[c[1]] for c in categories) == result["n_markers"]
        for label, count, percent, _ in categories:
            writer.writerow([name, label, result[count], result[percent]])

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
fig, ax = plt.subplots(figsize=(10, 4.2))
left = [0, 0]
for label, _, percent, color in categories:
    values = [d["results"][percent] for d in documents]
    ax.barh([1, 0], values, left=left, color=color, height=.46, label=label)
    for y, start, width in zip([1, 0], left, values):
        if width >= 5:
            ax.text(start + width / 2, y, f"{width:.1f}%", ha="center", va="center", color="white" if color == "#1c7554" else "#17251f", fontsize=9)
    left = [start + width for start, width in zip(left, values)]
ax.set(yticks=[1, 0], yticklabels=["Vendor assembly", "Local assembly"], xlim=(0, 100), xlabel="Percentage of the 125 BUSCO groups")
ax.set_title("BUSCO completeness · eukaryota_odb12.2", loc="left", weight="bold", pad=18)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_xlabel("Percentage of the 125 BUSCO groups", labelpad=12)
fig.subplots_adjust(left=.18, right=.98, top=.82, bottom=.31)
fig.legend(*ax.get_legend_handles_labels(), loc="lower center", bbox_to_anchor=(.57, .02), ncol=2, frameon=False, fontsize=9)
fig.savefig(figures / "busco_comparison.png", dpi=200, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(tables / "busco_comparison.csv")
print(figures / "busco_comparison.png")
