import lingtreemaps
import pandas as pd
from Bio import Phylo
from pathlib import Path
from lingtreemaps.cli import load_conf

dic = {1: "A", 2: "B", 3: "C"}

w = "newc1243"

for f in Path(".").glob("*.csv"):
    name = f.stem
    if name != w: continue
    df = pd.read_csv(f"{name}.csv")
    df.sort_values(by="ID", inplace=True)
    data = []
    i = 1
    for lg in df.to_dict("records"):
        data.append({"Clade": lg["ID"], "Value": dic[i]})
        if i == 3:
            i = 1
        else:
            i += 1
    feature_df = pd.DataFrame.from_dict(data)
    tree = Phylo.read(f"{name}.nwk", "newick")
    conf = load_conf(f"{name}.yaml")
    conf["filename"] = name+".svg"
    lingtreemaps.plot(df, tree, feature_df, **conf)
