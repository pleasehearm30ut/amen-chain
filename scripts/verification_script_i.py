import json
import os

# Deterministic letter-sum mapping m(word)
def m(word):
    return sum(ord(c.upper()) - 64 for c in word if c.isalpha())

# Orthogonal Vector Components
father_val = m("Father") # 58
son_val = m("Son")       # 48

# Pythagorean Theorem: a^2 + b^2 = c^2
a_sq = father_val**2
b_sq = son_val**2
c_sq = a_sq + b_sq

print(f"Verifying Eternal Witness: {a_sq} + {b_sq} = {c_sq}")
print("Status: Infinite Love / Amen¹⁰")

# Update ark_manifest.json
manifest_path = "ark_manifest.json"
new_data = {
    "status": "0110 Sync Active",
    "milestone": {
        "date": "2026-01-03",
        "title": "Infinite Love / Amen¹⁰",
        "axiom": "Father + Son == Holy Ghost"
    }
}

if os.path.exists(manifest_path):
    with open(manifest_path, 'r') as f:
        data = json.load(f)
    data.update(new_data)
    with open(manifest_path, 'w') as f:
        json.dump(data, f, indent=2)
    print("Manifest synced.")
