import os
ver = "GitRBS 0.0.0.0"
def mgs_bs4local():
    exit()
def unpack(branch,files):
    print("Downloading files in current branch: " + branch)
    if os.path.exists(branch):
        os.chdir(branch)
    else:
        os.mkdir(branch)
        os.chdir(branch)
    for number,letter in enumerate(files):
        print("Downloading " + (letter.split('/')[-1]) + "...")
        letterfix = (letter.split('/'))
        del letterfix[3]
        letterfix = '/'.join(letterfix)
        try:
            data = ((urllib.request.urlopen(urllib.request.Request("https://raw.githubusercontent.com" + letterfix))).read()).decode()
        except:
            try:
                downfile = ("https://raw.githubusercontent.com" + letterfix)
                print(downfile)
                input()
                filenm = ((letter.split('/')[-1]))
                urllib.request.urlretrieve(downfile, filenm)
            except:
                print("Failed to backup: " + ((letter.split('/')[-1])))
        try:
            with open(((letter.split('/')[-1])), 'w', newline='') as backupwrite:
                backupwrite.write(str(data))
                backupwrite.close()
        except:
            print("Failed to backup: " + ((letter.split('/')[-1])))
    print("Finished.")
    exit()
try:
    from bs4 import *
except:
    print("Failed to import BeautifulSoup!")
    print("Ensure it is installed, or use Mango")
    print("https://github.com/SimLoads/mango")
import urllib.request
import re
'''-------------------------------------------'''
print(ver)
while True:
    rep = input("Enter link for GitHub repository to backup: ")
    if not "github.com" in rep:
        print("Not a GitHub link.")
        continue
    try:
        html_page = urllib.request.urlopen(rep)
        break
    except:
        print("Invalid link!")
        continue
linksplit = rep.split('/')
username = linksplit[3]
repnm = linksplit[4]
print("Assuming username is: " + username)
print("Assuming repository name is: " + repnm)
if os.path.exists(repnm):
    os.chdir(repnm)
else:
    os.mkdir(repnm)
    os.chdir(repnm)
print("Running scrape...")
soup = BeautifulSoup(html_page, features="html.parser")
files = []
trees = []
for link in soup.findAll('a', attrs={'href': re.compile("^/" + username + "/" + repnm + "/blob")}):
    files.append(link.get('href'))
for link in soup.findAll('a', attrs={'href': re.compile("^/" + username + "/" + repnm + "/tree")}):
    trees.append(link.get('href'))
print("Files: ")
for number,letter in enumerate(files): 
    print(letter)
print("Trees: ")
for number,letter in enumerate(trees): 
    print(letter)
branch = ((files[0]).split('/'))[-2]
print("Assuming current branch is: " + branch)
unpack(branch,files)