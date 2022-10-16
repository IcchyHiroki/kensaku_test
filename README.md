# kensaku_test

## 実行環境
Pc:Mac M1
プログラム言語:python 3.9.12 

**installed module**
streamlit
httpx
 
インストール手順
1.miniconda/ anaconaをinstall
2.仮想化環境の作成
conda create -n <dev_name> python=3.9.12
3.インストール
conda install -c conda-forge httpx
conda install -c conda-forge streamlit

検索スクローラー:FESSを利用

**実行手順**
1.FESSの実行
1.1
システム > スケジューラ > Default Crawler を選択し、[今すぐ開始]
1.2
システム情報　＞　クロール情報　より確認
[クロール情報] のインデックスサイズ(ウェブ/ファイル)に検索対象としたドキュメント数を確認

1.3 
FESSの検索画面よりFESSを検索
*10/11 16:05現在、1件のみなので修正

2.streamlitによりweb UIを実行

2.1
pyファイルがあるでディレクトリに移動

2.2
streamlit run kensaku_first.py

2.3
実行後以下のURLにアクセス
http://localhost:8501/
