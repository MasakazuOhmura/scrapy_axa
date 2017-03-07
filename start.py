from scrapy import cmdline
from datetime import datetime

name = "axa_sitemap"

# To output folder
now = datetime.now().strftime("%Y%m%d-%H_%M_%S")
extension = ".csv"
filename = "output/" + now + extension

cmds = ["scrapy", "crawl", name, "-o", filename]
cmdline.execute(cmds)
