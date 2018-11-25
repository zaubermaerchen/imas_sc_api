THE IDOLM@STER SHINY COLORS DATA API
===============
アイドルマスターシャイニーカラーズのデータを取得する為のAPIです。

必要ミドルウェア・ライブラリ
---------------
* Python >= 3.7
* MariaDB >= 10.3.9
* [MeCab](http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html) >= 0.996
* [Groonga](http://groonga.org/ja/) >= 8.08
* [Mroonga](http://mroonga.org/ja/) >= 8.08

必要Pythonライブラリ
---------------
* Django >= 2.1.3
* djangorestframework >= 3.9.0
* django-cors-headers >= 2.4.0
* PyMySQL >= 0.9.2

ローカル環境での起動手順
---------------
1. 必要ミドルウェア・ライブラリ、必要Pythonライブラリをインストールする
1. プロジェクトのルートディレクトリで「python manage.py migrate」を実行してデータベースを初期化する
1. sql/create_table.sqlを実行してテーブルを作成する
1. sql/data.sqlを実行してデータを登録する
1. プロジェクトのルートディレクトリで「python manage.py runserver 8000」を実行してサーバーを起動する
1. 「http://localhost:8000/imas_cg/api/admin/」にアクセスして管理画面にアクセスできるか確認する

APIリファレンス
---------------
### キャラクター名取得API
#### URL
/imas_sc/api/character/names/


#### レスポンスパラメータ

    [
        {
            "name": "七草はづき"
        },
        {
            "name": "三峰結華"
        },
    ]


|パラメータ|項目名|備考|
|---|---|---|
|name|キャラクター名| |

### 4コマ漫画検索API
#### URL
/imas_sc/api/cartoon/search/

#### リクエストパラメータ

|パラメータ|項目名|必須|備考|
|---|---|---|---|
|title|検索対象タイトル| | |
|start_at|検索対象公開日(開始)| |yyyy-mm-dd形式|
|end_at|検索対象公開日(終了)| |yyyy-mm-dd形式|
|character|検索対象アイドル| |登場キャラクターのフルネームを記述 複数指定可能|
|offset|検索結果開始位置| |省略時は先頭位置から|
|limit|検索結果取得件数| |省略時は10件|

#### レスポンスパラメータ

    {
        "count": 74,
        "next": "http://127.0.0.1:8000/imas_sc/api/cartoon/search/?limit=10&offset=10",
        "previous": null,
        "results": [
            {
                "id": 10000,
                "type": 0,
                "episode": 0,
                "title": "ごあいさつ",
                "release_date": "2018-02-08",
                "characters": [
                    "櫻木真乃",
                    "風野灯織",
                    "八宮めぐる"
                ],
                "thumbnail_hash": "50b66b5f74559eaf139ba37a6484799b86edba588fe3095597b04e4482ac77d6",
                "image_hash": "f026bcda1be7def3b2e182870f3fce83318820675c588240a2d35fff5ab6d4bb",
                "tweet_id": 961544820589146000
            },
            {
                "id": 10001,
                "type": 0,
                "episode": 1,
                "title": "つまり…？",
                "release_date": "2018-02-10",
                "characters": [
                    "櫻木真乃",
                    "風野灯織",
                    "八宮めぐる"
                ],
                "thumbnail_hash": "1e2d592f3d739872957d2807b199fdb6d985d9c2b4f3d8c7891d27fee00027a3",
                "image_hash": "b03454debdc5d444fdfa4784683eaeacb763414eeb08ea70d6119ee2454fa146",
                "tweet_id": 962234684850622464
            },
        }
    }
    

|パラメータ|項目名|備考|
|---|---|---|
|count|検索結果総件数| |
|next|次ページのURL| |
|prev|前ページのURL| |
|results|検索結果| |

|パラメータ|項目名|備考|
|---|---|---|
|id|劇場ID| |
|type|種類|0:通常 1:特別 2:ゲーム内限定|
|episode|話数| |
|title|タイトル| |
|release_date|公開日|yyyy-mm-dd形式|
|characters|登場キャラクター| |
|thumbnail_hash|サムネイル画像のハッシュ| |
|image_hash|漫画画像のハッシュ| |
|tweet_id|twitterのツイートID| |