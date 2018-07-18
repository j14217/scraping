 ○必要なライブラリ
 　○selenium：ブラウザ操作や要素の抽出
 　　・要インストール -> pip install selenium
 　　・他にWebDriverをpythonの実行ファイルと同じ階層に配置しておく
 　　　WebDriverはfirefoxのものを以下からダウンロードする
 　　　　→https://github.com/mozilla/geckodriver/releases
 
 　○psycopg2：postgresqlを扱うためのライブラリ
 　　・要インストール -> pip install psycopg2

 　○SQLAlchemy：SQL文の生成
 　　・要インストール -> pip install SQLAlchemy

 ○scraping_systemフォルダ
    ○実行する際はこのリポジトリ(scraping)に移動してから実行してください
    ○複数サイトへ対応するためにシステム化を行っているソース郡
    ○3サイトに対応出来るように変更、追加を行いました

    ○land_scraping.py：土地情報のスクレイピング
    　・csvファイルのパス(csvpath*)は任意の場所にcsvフォルダを作成し
    　そのフォルダのパスを指定してください

    ○DbContoller.py：dbへの接続等のクラス
　
    ○insert_db.py：csvファイルを読み込みdbへのデータの挿入
　
    ○LandInfo.py：各カラム名を参照するためのクラス

    ○SiteScraping.py：スクレイピングの処理等をまとめたクラス

    ○CsvIO.py：ファイルの読み書きをまとめたクラス

    ○csvフォルダ：読み込みや書き込みをするcsvファイルの置き場所

○archiveフォルダ
    ・使用しない今まで書いたソースをまとめたフォルダ
