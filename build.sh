#!/bin/bash

# 依存関係をインストール
pip install -r requirements.txt

# マイグレーション & 静的ファイル収集
python manage.py migrate
python manage.py collectstatic --noinput
