# AmazonBot_for_Python
Amazonで人気商品等のページを監視し、Amazon本体からの出品が認識されると自動的に商品を購入するプログラムとなります。

# 概要
本プログラムで実行される流れは以下の通りです。

①　ブラウザの起動(Microsoft Edge)

②　Amazonで購入したい商品ページにアクセス

③　ログイン画面に移動し、メールアドレス、パスワードを入力

④　10秒ごとに在庫の確認(販売元の確認)

⑤　目的の在庫があれば注文確定(住所やクレジットカードなどのアカウント情報はあらかじめ手動で入力しておいてください)

本コードを使用する際はAmazonへのログイン情報として”LOGIN_ID”と”LOGIN_PASSWORD”の変数にご自身のログイン情報を入力してください。また、”ITEM_URL”の変数には自分が購入したい商品のurlを入力してください。“ACCEPT_SHOP”で出品元を変更することも可能です。

# おわりに
本コードは商品の注文が確定するところまで実証済みですが、万が一、損害や不都合なことが生じましても当方は一切の責任を負いませんので、ご理解の程よろしくお願い致します。
