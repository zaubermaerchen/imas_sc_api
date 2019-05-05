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
### ユニットリスト取得API
#### URL
/imas_sc/api/unit/list/

#### レスポンスパラメータ

    [
        {
            "id": 1,
            "name": "イルミネーションスターズ"
        },
        {
            "id": 2,
            "name": "アンティーカ"
        },
    ]


|パラメータ|項目名|備考|
|---|---|---|
|id|ユニットID| |
|name|ユニット名| |

### アイドルリスト取得API
#### URL
/imas_sc/api/idol/list/

#### レスポンスパラメータ

    [
        {
            "id": 1,
            "name": "櫻木真乃"
        },
        {
            "id": 2,
            "name": "風野灯織"
        },
    ]

|パラメータ|項目名|備考|
|---|---|---|
|id|ユニットID| |
|name|ユニット名| |

### プロデュースカード検索API
#### URL
/imas_sc/api/card/produce/search

#### リクエストパラメータ

|パラメータ|項目名|必須|備考|
|---|---|---|---|
|idol_id|アイドルID| |複数指定可能|
|rarity|レアリティ| |1:N 2:R 3:SR 4:SSR 複数指定可能|
|offset|検索結果開始位置| |省略時は先頭位置から|
|limit|検索結果取得件数| |省略時は10件|

#### レスポンスパラメータ

    {
        "count": 96,
        "next": "http://127.0.0.1:8000/imas_sc/api/card/produce/search/?limit=10&offset=10",
        "previous": null,
        "results": [
            {
                "id": 31,
                "name": "【ほわっとスマイル】櫻木真乃",
                "rarity": 4,
                "idol_id": 1,
                "release_date": "2018-04-24",
                "icon_hash": "ba08928b10e4bc65ccd500629b85e6b02a70f8b7abf8801b39c83f888423e1b9",
                "card_hash": "1f18dc539daf5f2e5b59b0eb75ed65ebdae848ec83d9094202ab3636593f0034",
                "fes_card_hash": "e6f23075a39ce9c9e4164e3b91019a8d14cb99ef66d914de8d0d628b46e84582"
            },
            {
                "id": 78,
                "name": "【ハ♡トフェルトゥギフト】櫻木真乃",
                "rarity": 4,
                "idol_id": 1,
                "release_date": "2019-01-31",
                "icon_hash": "b2ed477452cf281663d5ed938a2a329918e5c1bc66454273148c162d5d451936",
                "card_hash": "6ce91f73f44c1e155db1077139c032d3477a1a70e274e46098fe18187af58561",
                "fes_card_hash": "70547eae59e6a0473c6f8e82672607af358dd3e59a5163fd00e626235d261384"
            },
        ]
    }


|パラメータ|項目名|備考|
|---|---|---|
|count|検索結果総件数| |
|next|次ページのURL| |
|prev|前ページのURL| |
|results|検索結果| |

|パラメータ|項目名|備考|
|---|---|---|
|id|カードID| |
|name|カード名| |
|rarity|レアリティ|1:N 2:R 3:SR 4:SSR|
|idol_id|アイドルID| |
|release_date|登場日|yyyy-mm-dd形式|
|icon_hash|アイコン画像ハッシュ|画像ファイル名|
|card_hash|カード画像ハッシュ|画像ファイル名|
|fes_card_hash|フェスカード画像ハッシュ|画像ファイル名|

### サポートカード検索API
#### URL
/imas_sc/api/card/support/search

#### リクエストパラメータ

|パラメータ|項目名|必須|備考|
|---|---|---|---|
|idol_id|アイドルID| |複数指定可能|
|rarity|レアリティ| |1:N 2:R 3:SR 4:SSR 複数指定可能|
|offset|検索結果開始位置| |省略時は先頭位置から|
|limit|検索結果取得件数| |省略時は10件|

#### レスポンスパラメータ

    {
        "count": 99,
        "next": "http://127.0.0.1:8000/imas_sc/api/card/support/search/?limit=10&offset=10",
        "previous": null,
        "results": [
            {
                "id": 38,
                "name": "【トリプルイルミネーション】櫻木真乃",
                "rarity": 4,
                "idol_id": 1,
                "release_date": "2018-04-26",
                "icon_hash": "210257d4a8f989fbfc8c0251e907a7a31eca482887d7798d2a61c02dd8e2889e",
                "card_hash": "7c177a6dbcc7296001eab870e7443591b72635623939bb8e151c6b536fb838f0",
                "vocal": 64,
                "dance": 56,
                "visual": 60,
                "mental": 44,
                "max_vocal": 200,
                "max_dance": 175,
                "max_visual": 187,
                "max_mental": 138,
                "idea": 4
            },
            {
                "id": 52,
                "name": "【お揃いスナップ】櫻木真乃",
                "rarity": 4,
                "idol_id": 1,
                "release_date": "2018-06-30",
                "icon_hash": "0b103ae3488c51c71afd4c5a3c850abfbf44142db9aad19ecf93f18f3b6f942c",
                "card_hash": "7c0599e83c953523122b4c30654f4bf5c271c60f8ac3e02130bf13bee6c532db",
                "vocal": 66,
                "dance": 66,
                "visual": 60,
                "mental": 48,
                "max_vocal": 206,
                "max_dance": 206,
                "max_visual": 188,
                "max_mental": 150,
                "idea": 1
            },
        ]
    }

|パラメータ|項目名|備考|
|---|---|---|
|count|検索結果総件数| |
|next|次ページのURL| |
|prev|前ページのURL| |
|results|検索結果| |

|パラメータ|項目名|備考|
|---|---|---|
|id|カードID| |
|name|カード名| |
|rarity|レアリティ|1:N 2:R 3:SR 4:SSR|
|idol_id|アイドルID| |
|release_date|登場日|yyyy-mm-dd形式|
|icon_hash|アイコン画像ハッシュ|画像ファイル名|
|card_hash|カード画像ハッシュ|画像ファイル名|
|vocal|ボーカル初期値| |
|dance|ダンス初期値| |
|visual|ビジュアル初期値| |
|mental|メンタル初期値| |
|max_vocal|ボーカル最大値| |
|max_dance|ダンス最大値| |
|max_visual|ビジュアル最大値| |
|max_mental|メンタル最大値| |
|idea|アイデア|1:ボーカル 2:ダンス 3:ビジュアル 4:トーク 5:アピール|

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