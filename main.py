import os
import argparse
import subprocess
import time

def scurl(URL, delay=3):
    proc = subprocess.Popen(["curl", URL], stdout=subprocess.PIPE)

    time.sleep(delay)
    (out, err) = proc.communicate()
    
    if len(out) == 0 or err != None:
        print("There has been an error:", err)
    else:
        return out

parser = argparse.ArgumentParser(
                    prog='NY Times Paywall Bypass',
                    description='This program scrapes any NY Times article by bypassing the paywall. It downloads a webpage to your system.',
                    epilog='Location of download file')

# parser.add_argument('python_script')
parser.add_argument('link_to_article')
# parser.add_argument('download_file_location')

args = parser.parse_args()

out = scurl(args.link_to_article)
print(out)
