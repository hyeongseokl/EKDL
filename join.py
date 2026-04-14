import pandas as pd

unrate = pd.read_csv("UNRATE.csv")
gdp = pd.read_csv("A191RL1Q225SBEA.csv")
cusr = pd.read_csv("CUSR0000SAC.csv")

unrate["observation_date"] = pd.to_datetime(unrate["observation_date"])
gdp["observation_date"] = pd.to_datetime(gdp["observation_date"])
cusr["observation_date"] = pd.to_datetime(cusr["observation_date"])

unrate["quarter"] = unrate["observation_date"].dt.to_period("Q")
unrate_quarterly = (
    unrate.groupby("quarter", as_index=False)["UNRATE"]
    .mean()
)
unrate_quarterly["observation_date"] = unrate_quarterly["quarter"].dt.start_time
unrate_quarterly = unrate_quarterly[["observation_date", "UNRATE"]]

cusr["quarter"] = cusr["observation_date"].dt.to_period("Q")
cusr_quarterly = (
    cusr.groupby("quarter", as_index=False)["CUSR0000SAC"]
    .mean()
)
cusr_quarterly["observation_date"] = cusr_quarterly["quarter"].dt.start_time
cusr_quarterly = cusr_quarterly[["observation_date", "CUSR0000SAC"]]

merged = pd.merge(gdp, unrate_quarterly, on="observation_date", how="inner")
merged = pd.merge(merged, cusr_quarterly, on="observation_date", how="inner")
merged = merged.sort_values("observation_date")

merged.to_csv("joined_data.csv", index=False)

print(merged.head())
print(f"Joined dataset saved as joined_data.csv with {len(merged)} rows.")