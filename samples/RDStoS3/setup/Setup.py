from RDStoS3Sample import RDStoS3Sample
from Utilities import check_working_directory

import argparse
import sys


if __name__ == '__main__':
    check_working_directory()
    parser = argparse.ArgumentParser(description='Setup for RDS to S3 pipeline sample')
    parser.add_argument('--s3-path', action="store", dest="s3_bucket_path")
    args = parser.parse_args()
    s3_bucket_path = args.s3_bucket_path

    sample = RDStoS3Sample()

    if s3_bucket_path is None:
        sample.create_s3_bucket()
    elif not sample.validate_s3_bucket_path(s3_bucket_path):
        sys.exit(0) 

    sample.create_rds_instance()
    sample.run_setup_datapipeline()
    sample.print_setup_results()
