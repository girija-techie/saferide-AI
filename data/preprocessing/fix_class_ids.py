import os

LABEL_BASE = "processed/labels"
# LABEL_BASE = os.path.join("data", "processed", "labels")

for split in ["train", "val", "test"]:
    folder = os.path.join(LABEL_BASE, split)

    for file in os.listdir(folder):
        if not file.endswith(".txt") or file == "classes.txt":
            continue

        path = os.path.join(folder, file)
        new_lines = []

        with open(path, "r") as f:
            for line in f:
                parts = line.strip().split()
                cls = int(parts[0])

                # Helmet dataset fix
                if cls == 0:
                    new_cls = 1  # no_helmet
                elif cls == 1:
                    new_cls = 0  # helmet
                else:
                    new_cls = 2  # accident

                parts[0] = str(new_cls)
                new_lines.append(" ".join(parts))

        with open(path, "w") as f:
            f.write("\n".join(new_lines))

print("Class IDs standardized")
