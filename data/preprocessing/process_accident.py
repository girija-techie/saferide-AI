import shutil
import os

SRC = "raw/accident_dataset"
DST = "processed/accident"

split_map = {
    "train": "train",
    "valid": "val",
    "test": "test"
}

for src_split, dst_split in split_map.items():
    img_src = os.path.join(SRC, src_split, "images")
    lbl_src = os.path.join(SRC, src_split, "labels")

    img_dst = os.path.join(DST, "images", dst_split)
    lbl_dst = os.path.join(DST, "labels", dst_split)

    os.makedirs(img_dst, exist_ok=True)
    os.makedirs(lbl_dst, exist_ok=True)

    for img in os.listdir(img_src):
        shutil.copy(
            os.path.join(img_src, img),
            os.path.join(img_dst, img)
        )

    for lbl in os.listdir(lbl_src):
        shutil.copy(
            os.path.join(lbl_src, lbl),
            os.path.join(lbl_dst, lbl)
        )

print("✅ Accident dataset copied successfully")
