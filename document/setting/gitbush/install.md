# Git Bush インストール&初期設定手順

1. ダウンロード  
https://gitforwindows.org/
- ダウンロード を選択 
  - <img src="images/gitbush_download_01.png" width="50%">
2. インストール
- Only show new options にチェックをいれて install
  - <img src="images/gitbush_install_01.png" width="50%">
- チェックをすべて外し Finish
  - <img src="images/gitbush_install_02.png" width="50%">
3. 初期設定
- 作業用に適当なフォルダ (今回は step_repos) を作成する
  - <img src="images/gitbush_setting_01.png" width="50%">
- フォルダ内で右クリック → Open Git Bush here を選択 で Git Bush を起動
  - <img src="images/gitbush_setting_02.png" width="50%">
- ユーザとメールアドレスを登録する。
  - <img src="images/gitbush_setting_03.png" width="50%">
```
  git config --global user.name [gitに登録したメールアドレス]
  git config --global user.email　[gitに登録したメールアドレス]
```
- 編集対象のリポジトリのURLをコピーする  
https://github.com/HirobumiNakamura/step_repos
  - <img src="images/gitbush_setting_04.png" width="50%">
- git clone [コピーしたリポジトリのURL]を 実行する
  - <img src="images/gitbush_setting_05.png" width="50%">
- step_repos の フォルダ内に github上のファイルがコピーされるので、今後はこのファイルを編集していきます
  - <img src="images/gitbush_setting_06.png" width="50%">


