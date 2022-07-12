import os, datetime

os.system("del index.md")

contents_str = "---\ntitle: 某奇怪的目录\ndate: 最后更新于 " + str(datetime.date.today()) + "\n---\n## 目录\n"
for file_name in os.listdir():
    if ".md" in file_name:
        realFilename = file_name.split(".m")[0]
        contents_str += "1. [ " + realFilename + " ](" + realFilename + ".html)\n"

with open("index.md", mode="w", encoding="UTF-8") as file_obj:
    file_obj.write(contents_str)

pandoc_path = "C:\\Users\\xsjcy\\Videos\\Pandoc\\pandoc.exe"

for file_name in os.listdir():
    if ".md" in file_name:
        os.system(pandoc_path + " -s \"" + file_name + "\" -o \"" + file_name.split(".m")[0] + ".html\"")
