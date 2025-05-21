from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>01 stage{STAGE_NAME} started.........<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>stage{STAGE_NAME} completed.........<<\n")
except Exception as e:
    raise e