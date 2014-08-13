import sys
import argparse

from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection()

def download_file(bucket, keystr, filename):
    try:
        key = Key(bucket=bucket, name=keystr)
        key.get_contents_to_filename(filename)
    except Exception, e:
	print "Attempted to fetch {} from {} as {}".format(keystr, bucket, filename)
        print "Download failed: {}".format(e)

if __name__ == "__main__":
    """ argv1: bucketname
        argv2: keystr
        argv3: destination filename
    """
    parser = argparse.ArgumentParser(description="Process bucket name, key name, and output filename")
    parser.add_argument('bucket_name', type=str, help="a bucket name")
    parser.add_argument('key_name', type=str, help="an s3 key/file name")
    parser.add_argument('filename', type=str, help="filename to output")
    args = parser.parse_args()

    bucket = conn.get_bucket(args.bucket_name, validate=False)
    download_file(bucket, args.key_name, args.filename)
