○land_info_scraping.py：土地情報のスクレイピング
　・selenium
　　要インストール -> pip install selenium
　　pythonの実行ファイルと同じ階層にgeckodriver.exeを配置しておく

○land_info1.csv,land_info2.csv：スクレイピングしたデータ


○dbconnection.py：dbへの接続等のクラス
　・psycopg2
　　要インストール -> pip install psycopg2

○filedatadb.py：dbへのデータの挿入など
　TODO 全要素への対応、したがってdbのカラムをすり合わせが必要

○LandInfo.py：各カラム名を参照するためのクラス