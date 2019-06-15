THE IDOLM@STER SHINY COLORS DATA API
===============
アイドルマスターシャイニーカラーズのデータを取得する為のAPIです。

必要ミドルウェア・ライブラリ
---------------

* Python >= 3.7
* MariaDB >= 10.3.15
* [MeCab](http://taku910.github.io/mecab/) >= 0.996
* [Groonga](http://groonga.org/ja/) >= 9.03
* [Mroonga](http://mroonga.org/ja/) >= 9.03

必要Pythonライブラリ
---------------

* Django >= 2.2.2
* djangorestframework >= 3.9.4
* django-cors-headers >= 3.0.2
* mysqlclient >= 1.4.2.post1

ローカル環境での起動手順
---------------

1. docker-compose up
1. 「http://localhost:8000/admin/」にアクセスして管理画面にアクセスできるか確認する
