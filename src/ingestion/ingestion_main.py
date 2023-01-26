import yaml

from src.ingestion.ingest_bronze_tables import IngestMergeLoanTables
from src.validation.schema import bronze_merge_schema

if __name__ == '__main__':
    with open('C:/Users/valerie.bauman/Documents/GitHub/sample-work-loan-application/ingestion_config.yml', 'r') as stream:
        cf= yaml.safe_load(stream)

    ingest_merger= IngestMergeLoanTables(cf= cf, cf_m= cf['ingest'])
    bronze_merged= ingest_merger.get_silver_table(schema= bronze_merge_schema)



        