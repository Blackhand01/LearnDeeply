import json

in_path = "ThinkDeep/6_DL_confidence_assignment-2.ipynb"
out_path = "ThinkDeep/6_DL_confidence_assignment-2_fixed.ipynb"

with open(in_path, "r") as f:
    notebook = json.load(f)

# Rimuovi il campo "widgets" se presente
if "widgets" in notebook.get("metadata", {}):
    print("🔧 Rimozione del blocco 'widgets' dai metadata...")
    del notebook["metadata"]["widgets"]

with open(out_path, "w") as f:
    json.dump(notebook, f, indent=2)

print(f"✅ Notebook corretto salvato in: {out_path}")
