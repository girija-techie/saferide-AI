import os
import shutil

SRC_BASE = "processed"
DST_BASE = "processed/final"

datasets = ["helmet_5"]
splits = ["train", "val", "test"]

for split in splits:
    os.makedirs(os.path.join(DST_BASE, "images", split), exist_ok=True)
    os.makedirs(os.path.join(DST_BASE, "labels", split), exist_ok=True)

    for ds in datasets:
        img_src = os.path.join(SRC_BASE, ds, "images", split)
        lbl_src = os.path.join(SRC_BASE, ds, "labels", split)

        if not os.path.exists(img_src):
            continue

        for f in os.listdir(img_src):
            shutil.copy(
                os.path.join(img_src, f),
                os.path.join(DST_BASE, "images", split, f)
            )

        for f in os.listdir(lbl_src):
            shutil.copy(
                os.path.join(lbl_src, f),
                os.path.join(DST_BASE, "labels", split, f)
            )

print("✅ Final dataset merged safely")
