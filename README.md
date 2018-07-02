# scraping
DBに土地情報を入れたテーブルをpostgresql上から抽出し、
検索が行えるようなサイトの作成のためのファイル

・/landinfo/search/templates/search/base.html
  {% extends "base.html" %}　
  と他のhtmlに記載することで他のhtmlに<html>タグや<body>タグを記載する必要がなくなります。
