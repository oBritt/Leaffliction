
import os
import sys
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception:
        return False


def get_all_dirs(p):
    files = [f for f in os.listdir(p)
             if os.path.isdir(os.path.join(p, f)) and f[0] != '.']
    return files


def get_amount_of_pics(dir):
    counter = 0
    for file in os.listdir(dir):
        counter += is_image(os.path.join(dir, file))
    return counter


def main():
    if len(sys.argv) != 2:
        print("Format [distrubition.py] [path to dir]")
        exit(1)
    path_to = sys.argv[1]
    if not os.path.isdir(path_to):
        print(path_to + " is not a dir")
        exit(1)
    files = get_all_dirs(path_to)
    if files == 0:
        print("Couldnt find any dirs inside")
        exit(1)
    complete_path = [os.path.join(path_to, f) for f in files]
    result = [get_amount_of_pics(f) for f in complete_path]
    final_dirs = [files[i] for i, r in enumerate(result) if r > 0]
    final_result = [r for r in result if r > 0]
    colors = plt.cm.viridis(np.linspace(0, 1, len(final_result)))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(len(final_dirs) * 3, 7))
    ax2.bar(final_dirs, final_result, color=colors)
    ax2.tick_params(axis='x', rotation=45)

    wedges, _, _ = ax1.pie(final_result, colors=colors, autopct='%1.1f%%')
    ax1.legend(wedges, final_dirs, title="Directories", loc="lower left",
               bbox_to_anchor=(-0.15, -0.15))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
