# git command メモ

## 基本操作

gitの状態を確認する  
`git status`

Staging areaの内容をWorking directoryに戻す(unstage)する  
`git restore --staged <file>`

Working derectoryでの作業を破棄する  
`git restore <file>`

ファイル名の変更をGitで管理する  
`git mv <filename1> <filename2>`

ファイルの削除をGitで管理する  
`git rm <filename>`

コミット履歴を一覧表示する  
`git log`  
option --oneline：各コミットを一行で表示する
       --graph:各コミットの繋がりを線で表示する

特定のコミット情報を表示する  
`git show <commitID>`

## .gitignore

gitの管理から外す

- ファイル名はそのまま記述：hoge.txt
- *を使う：\*.csv
- フォルダは/を記述：logs/
