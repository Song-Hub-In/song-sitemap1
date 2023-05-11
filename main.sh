pip install bs4 lxml
python3 main.py
for FILE in sitemap/*; do echo python3 code.py "$FILE"; git add -A --verbose; git commit -m "test"; git push; done

