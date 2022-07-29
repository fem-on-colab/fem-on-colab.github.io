import pandas as pd
from datetime import date

from release_download_count import release_download_count

df = pd.read_csv("stats.csv")

counts_dict = release_download_count("fem-on-colab/fem-on-colab", "", 50)

date_header = date.today().strftime("count_%Y_%m_%d")
if date_header not in df.columns:
    df[date_header] = [0] * len(df)
new_row_base = {header: (0 if header.startswith("count_") else "") for header in df.columns}

for (name_asset, count) in counts_dict.items():
    expected_id = " ".join(name_asset).replace(" ", "_")
    condition = df.id.str.startswith(expected_id)
    if len(df[condition]) == 0:
        package, version = name_asset[0].split(" ", 1)
        new_row = new_row_base.copy()
        new_row["id"] = expected_id
        new_row["package"] = package
        new_row["version"] = version
        new_row["asset"] = name_asset[1]
        new_row[date_header] = count
        df = df.append(new_row, ignore_index=True)
    else:
        df.loc[condition, date_header] = count

df.to_csv("stats.csv", index=False)
