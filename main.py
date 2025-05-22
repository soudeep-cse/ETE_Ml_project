from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation_pipeline import DataTransformationTrainingPipeline


# ----------------------- Data Ingestion -------------------------
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>01 stage{STAGE_NAME} started.........<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>stage{STAGE_NAME} completed.........<<\n")
except Exception as e:
    raise e

# -------------------------- Data validation ------------------------

STAGE_NAME = "Data validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# --------------------------- Data Transformation -------------------------
STAGE_NAME = "Data Transformation stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    raise e