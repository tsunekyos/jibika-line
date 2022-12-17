# jibika-line
近所の耳鼻科の予約状況をラインに送信するアプリ

## env値 について
- `$ cp .env.template .env` して、必要な値を `.env` に記載
  - 記載すべき値については、 https://developers.line.biz/ja/reference/messaging-api/#send-push-message を参照

## pipからインストールしたパッケージ
- request
- python-dotenv
- selenium
- ※ これらをlambda上で使うためには、以下の `aws-layer` の操作も必要

## aws-layer
- LambdaのLayerを作成するためのzipを保管するディレクトリ
- 使用したいパッケージが増えたら以下を実行
```shell
$ cd aws-layer
$ pip install -t python <任意のパッケージ名>
$ zip -r9 layer.zip python
```