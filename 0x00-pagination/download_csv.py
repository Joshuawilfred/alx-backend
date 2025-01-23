#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./download_csv.py <filename>")
    exit(1)

# Get the file name
file_name = sys.argv[1]

# URL of the CSV file
url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240901T104743Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=018aed6a7d1e413df825d62ec9d4af643bcc24365803ae18a7187a03f36144bd"

res = requests.get(url)
with open(file_name, "wb") as file:
    file.write(res.content)

print(f"File content saved as '{file_name}'")
