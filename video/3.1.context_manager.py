import os
url = "https://python.sdv.univ-paris-diderot.fr/data-files/english-common-words.txt"
file_name = "english-common-words.txt"

os.system(f"curl {url} > {file_name}")
