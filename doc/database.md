# オンラインテストクリエイター
CODEGYMのチーム開発 by チームA02(!nop)

## DB設計

|ユーザー情報|
|:-|
|UID|
|名前|
|メアド|
|ハッシュ化したPW|

|ユーザーが作ったテスト|
|:-|
|テストNo|
|作った人のUID|
|受験PW(ハッシュ化済み)|
|送る人のクラスIDorUID|
|受験期間|
|制限時間|

|問題ID|
|:-|
|問題ID|
|テストNo|
|大問|
|問題|

|問題|
|:-|
|問題ID|
|問題のJSON|
問題のJSONの内容は↓
|本文|
|解答のタイプ|
|解答(選択肢も)|
|解説|
|得点|
|即時採点の有無|
|画像|
|問題につけたタグ|

この方法を使う場合、試験時には解答解説を空白に置き換える

|タグ一覧|
|:-|
|作った人のUID|
|タグ一覧|

|解答|
|:-|
|問題ID|
|ユーザーの回答|

以下のDBは予備プラン
|回答|
|:-|
|問題ID|
|回答(選択肢含む)|
|解説|

試験開始時に空白にする方法でない場合、不正防止用に回答は隔離する

|タグ管理|
|:-|
|問題ID|
|問題のタグ|
