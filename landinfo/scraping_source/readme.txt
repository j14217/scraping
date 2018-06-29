○land_info_scraping.pyを実行で、
 スクレイピングからDBへの挿入処理が行われます

 ○必要なライブラリ
 　○selenium
 　　・要インストール -> pip install selenium
 　　・他にWebDriverをpythonの実行ファイルと同じ階層に配置しておく
 　　　WebDriverはfirefoxのものを以下からダウンロードする
 　　　　→https://github.com/mozilla/geckodriver/releases
 
 　○psycopg2
 　　・要インストール -> pip install psycopg2
 
 ○各ファイルの説明
 　○land_info_scraping.py：土地情報のクローリングとスクレイピング
    ・csvファイルのパス(csvpath1, csvpath2)は任意のパスを指定してください
 
 　○land_info1.csv,land_info2.csv：スクレイピングしたデータ
    ・この2つのファイルは上書きで開くので、再実行する場合は2ファイルを削除、あるいは中身のテキストを消してください
