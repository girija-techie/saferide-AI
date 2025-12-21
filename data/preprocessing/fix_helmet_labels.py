import os

# Paths
LABEL_BASE = "processed/helmet_2/labels"

# Mapping from OLD class IDs → NEW class IDs
# helmet → 0, no_helmet → 1
CLASS_MAP = {
    1: 1,  # driver_with_helmet → helmet
    3: 0  # passenger_with_helemt → helmet
}

for split in ["train", "val", "test"]:
    folder = os.path.join(LABEL_BASE, split)

    for file in os.listdir(folder):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(folder, file)
        new_lines = []

        with open(path, "r") as f:
            for line in f:
                parts = line.strip().split()
                old_cls = int(parts[0])

                # Keep only helmet / no_helmet
                if old_cls in CLASS_MAP:
                    parts[0] = str(CLASS_MAP[old_cls])
                    new_lines.append(" ".join(parts))

        # Overwrite label file
        with open(path, "w") as f:
            f.write("\n".join(new_lines))

print("✅ Helmet labels cleaned and remapped")
