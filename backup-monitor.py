#!/usr/bin/env python3.9

import os
import time
import json
import sys

BACKUP_DIR = "/home/pi/influx/backup"

last_backup_file = max((os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR) if f.endswith('.tar.gz')), default=None)
if last_backup_file:
    last_backup_file_size = os.path.getsize(last_backup_file)
else:
    last_backup_file_size = 0

last_modified = max((os.path.getmtime(os.path.join(BACKUP_DIR, f)) for f in os.listdir(BACKUP_DIR)), default=0)
last_modified_date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(last_modified))
last_modified_unix = int(time.mktime(time.localtime(last_modified)))
elapsed = time.time() - last_modified
interval = 4 * 24 * 60 * 60

if elapsed < interval:
    result = {"status": 0, "last_modified_date": last_modified_unix, "last_backup_file_size": last_backup_file_size}
else:
    result = {"status": 1, "last_modified_date": last_modified_unix, "last_backup_file_size": last_backup_file_size}

print(json.dumps(result))
