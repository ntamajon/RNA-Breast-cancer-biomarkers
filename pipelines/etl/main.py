from pipelines.etl import import_parse, cleaning, merging, export
from src.utils.path_utils import p
from src.utils.logger import get_logger

logger = get_logger(__name__, log_file="pipeline.log")

def main():
    #from import_parse
    gene_df = import_parse.read_gene(p("raw", "GSE96058.csv.gz"))
    metadata_1 = import_parse.parse_series_matrix(p("raw", "GSE96058-GPL11154_series_matrix.txt.gz"))
    metadata_2 = import_parse.parse_series_matrix(p("raw", "GSE96058-GPL18573_series_matrix.txt.gz"))

    #from cleaning
    gene_df = cleaning.sample_cleaner(gene_df=gene_df)
    metadata_1 = cleaning.metadata_cleaner(metadata_1)
    metadata_2 = cleaning.metadata_cleaner(metadata_2)
    
    logger.info("Checking metadata files have same amount of variables...")
    if metadata_1.shape[1] == metadata_2.shape[1]:
        logger.info(f"OK {metadata_1.shape[1]} columns on both datasets")
    else:
        raise ValueError("Warning - No match on metadata columns!")

    #from merging
    gene_pam50 = merging.data_merge(metadata_1=metadata_1, 
                            metadata_2=metadata_2, 
                            gene_df=gene_df)
    
    #from export
    export.data_export(merged_file=gene_pam50)


if __name__ == "__main__":
    main()