#!/usr/bin/env python3

from datetime import datetime
import argparse
import hashlib
import os
import sys

import pytz

tz = pytz.timezone('US/Pacific')


def main(target_dir, file_list):
    for fname in file_list:
        md = os.stat(fname)
        mtime = tz.localize(datetime.utcfromtimestamp(md.st_mtime))
        formatted_date = mtime.strftime('%Y/%m-%d')
        basename = os.path.basename(fname)
        
        new_path = "%s/%s/%s" % (target_dir, formatted_date, basename)
        new_dir = "%s/%s/" % (target_dir, formatted_date)

        if os.path.isfile(new_path):
            existing_md = os.stat(new_path)
            if existing_md.st_size != md.st_size:
                print("  ! Not overwriting %s with different file %s" % (new_path, fname))
                continue

            existing_file_sha1 = sha1_file(new_path)
            new_file_sha1 = sha1_file(fname)
            if existing_file_sha1 == new_file_sha1:
                print("Skipping identical files %s and %s" % (new_path, fname))
                continue
        elif not os.path.isdir(new_dir):
            print("Creating directory %s" % (new_dir,))
            os.makedirs(new_dir)

        os.rename(fname, new_path)

        print("Moved %s --> %s" % (fname, new_path))


def sha1_file(fname):

    sha1 = hashlib.sha1()
    with open(fname, 'rb') as f:
        sha1.update(f.read())
    return sha1.hexdigest()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move files based on their mtime")
    parser.add_argument('files', help='files to move', nargs='+')
    parser.add_argument('--target', dest='target', help='root directory to move files to', required=True)
    args = parser.parse_args()
    sys.exit(main(args.target, args.files))
