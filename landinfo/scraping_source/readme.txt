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
 
 ○各ファイルの説明
 　○land_info_at.py、land_info_su.py：土地情報のクローリングとスクレイピング
    ・csvファイルのパス(csvpath*)は任意の場所にcsvフォルダを作成し
    　そのフォルダのパスを指定してください

 　○dbconnection.py：dbへの接続等のクラス
　
 　○filedatadb.py：csvファイルを読み込みdbへのデータの挿入
　
 　○LandInfo.py：各カラム名を参照するためのクラス