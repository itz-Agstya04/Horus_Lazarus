from src.pipeline import build_dataset
from src.pipeline_scoring import run_scoring

def main():
    df = build_dataset()
    df = run_scoring(df)
    df.to_csv("final_output.csv", index=False)
    print("Pipeline executed. Output saved to final_output.csv")

if __name__ == "__main__":
    main()
