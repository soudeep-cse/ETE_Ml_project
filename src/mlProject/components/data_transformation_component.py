import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_dir)

    def CheckEda(self):
        try:
            df = self.data.copy()  # work on copy to keep original safe

            # 1. Missing values check
            missing = df.isnull().sum()
            logger.info("Missing values per column:\n%s", missing)
            print("Missing values per column:\n", missing)

            # 2. Duplicate rows check
            duplicates = df.duplicated().sum()
            logger.info("Number of duplicate rows: %d", duplicates)
            print("Number of duplicate rows:", duplicates)

            # 3. Categorical columns detection and encoding (if any)
            cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
            if cat_cols:
                logger.info("Categorical columns detected: %s", cat_cols)
                print("Categorical columns detected:", cat_cols)
                # Convert categorical columns to numeric using pd.get_dummies (one-hot encoding)
                df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
            else:
                logger.info("No categorical columns detected.")
                print("No categorical columns detected.")

            # 5. Plot histograms of original features
            df.hist(figsize=(12, 10), bins=30)
            plt.suptitle("Feature Distributions Before Scaling")
            plt.tight_layout()
            plt.show()

            # 6. Scaling numeric features (excluding target)
            target_col = 'quality'
            features = df.drop(columns=[target_col])
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)

            df_scaled = pd.DataFrame(scaled_features, columns=features.columns)
            df_scaled[target_col] = df[target_col].values

            # 7. Log mean and std of scaled features
            logger.info("Scaled features mean:\n%s", df_scaled.mean())
            logger.info("Scaled features std dev:\n%s", df_scaled.std())
            print("Scaled features mean:\n", df_scaled.mean())
            print("Scaled features std dev:\n", df_scaled.std())

            # 8. Plot histograms after scaling
            df_scaled.drop(columns=[target_col]).hist(figsize=(12, 10), bins=30)
            plt.suptitle("Feature Distributions After Scaling")
            plt.tight_layout()
            plt.show()

            # 9. Correlation heatmap on scaled data
            plt.figure(figsize=(12, 10))
            corr = df_scaled.corr()
            sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
            plt.title("Correlation Heatmap")
            plt.show()

            return df_scaled  # return scaled data for downstream use
        except Exception as e:
            raise e

    def train_test_spliting(self):
        try:
            data = self.data
            train, test = train_test_split(data, test_size=0.2)

            train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

            logger.info("Splited data into training and test sets")
            logger.info(train.shape)
            logger.info(test.shape)

            print(train.shape)
            print(test.shape)
            
        except Exception as e:
            raise e