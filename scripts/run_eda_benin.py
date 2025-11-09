# scripts/run_eda_benin.py
import sys
from pathlib import Path
from src.cleaning import load_standard, basic_profile, impute_median, flag_outliers_z

def main(raw_path, out_path):
    df = load_standard(raw_path)
    print("Rows:", len(df))
    profile = basic_profile(df)
    print("Top missing cols:", sorted(profile['missing_counts'].items(), key=lambda x:-x[1])[:10])
    df, imputed = impute_median(df)
    print("Imputed cols:", imputed)
    flags = flag_outliers_z(df)
    print("Outlier counts:", flags.filter(like='_outlier').sum().to_dict())
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print("Saved cleaned CSV to", out_path)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python scripts/run_eda_benin.py <raw.csv> <out_clean.csv>")
    else:
        main(sys.argv[1], sys.argv[2])
