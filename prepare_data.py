from omegaconf import OmegaConf
import pandas as pd


def prepare_data(config):
    print('Preparing Data...')
    df = pd.read_csv(config.data.csv_file_path)
    print(df.head())


if __name__ == "__main__":
    config = OmegaConf.load("./params.yaml")
    prepare_data(config)
    
