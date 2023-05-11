pip install bs4 lxml
python3 main.py
for FILE in sitemap/*
do 
    echo $FILE
    python3 code.py "$FILE"
    git add -A --verbose
    git commit -m "$FILE"
    git push
    rm $FILE
done

