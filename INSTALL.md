# インストールガイド

デスクトップファイル整理アプリのインストール方法を説明します。

## 必要な環境

- Python 3.6以上
- Windows / macOS / Linux

## インストール方法

### Linux / macOS の場合

#### 方法1: セットアップスクリプトを使用（推奨）

```bash
cd /path/to/git-practice
./setup.sh
```

対話形式で以下の3つの方法から選択できます：
1. シンボリックリンクを作成（推奨）
2. エイリアスを作成
3. 現在の場所から直接実行

#### 方法2: 手動セットアップ

**シンボリックリンクを作成:**
```bash
mkdir -p ~/.local/bin
ln -s /path/to/git-practice/desktop_organizer.py ~/.local/bin/organize-desktop
chmod +x /path/to/git-practice/desktop_organizer.py

# PATHに追加（まだの場合）
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**エイリアスを作成:**
```bash
echo 'alias organize-desktop="python3 /path/to/git-practice/desktop_organizer.py"' >> ~/.bashrc
source ~/.bashrc
```

### Windows の場合

#### 方法1: バッチファイルを使用

1. `organize-desktop.bat` を作成（例：デスクトップに保存）

```batch
@echo off
python "C:\path\to\git-practice\desktop_organizer.py" %*
```

2. ダブルクリックで実行、またはコマンドプロンプトから呼び出し

#### 方法2: Python を直接呼び出し

```cmd
python C:\path\to\git-practice\desktop_organizer.py --dry-run
```

#### 方法3: PATHに追加

1. システム環境変数を開く
2. `Path` 変数を編集
3. `C:\path\to\git-practice` を追加
4. コマンドプロンプトを再起動

```cmd
python desktop_organizer.py --dry-run
```

## 使い方

### 基本的な使い方

```bash
# 確認モード（実際には移動しない）
organize-desktop --dry-run

# 実際に整理を実行
organize-desktop

# 任意のフォルダを指定
organize-desktop --path /path/to/folder
```

### Windowsの場合

```cmd
REM 確認モード
python desktop_organizer.py --dry-run

REM 実際に整理
python desktop_organizer.py

REM カスタムパス
python desktop_organizer.py --path "C:\Users\YourName\Downloads"
```

## トラブルシューティング

### Python が見つからない

**Linux / macOS:**
```bash
# Python 3がインストールされているか確認
python3 --version

# インストールされていない場合
# Ubuntu / Debian
sudo apt update && sudo apt install python3

# macOS (Homebrew)
brew install python3
```

**Windows:**
1. [Python公式サイト](https://www.python.org/downloads/)からダウンロード
2. インストール時に「Add Python to PATH」にチェック

### 権限エラー

```bash
# Linux / macOS
chmod +x desktop_organizer.py
```

### PATHが通らない

```bash
# 現在のPATHを確認
echo $PATH

# ~/.local/bin が含まれていない場合
export PATH="$HOME/.local/bin:$PATH"

# 恒久的に設定
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## アンインストール

### シンボリックリンクを削除

```bash
rm ~/.local/bin/organize-desktop
```

### エイリアスを削除

```bash
# ~/.bashrc または ~/.zshrc から該当行を削除
nano ~/.bashrc
# 保存後
source ~/.bashrc
```

### スクリプト自体を削除

```bash
cd /path/to/git-practice
git checkout desktop_organizer.py
# または完全に削除
rm desktop_organizer.py
```

## サポート

問題が発生した場合は、リポジトリのIssueセクションで報告してください。
