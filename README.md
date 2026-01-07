# git-practice

このリポジトリはGit動画講座用です．
ローカルリポで更新
re a-se-practice上で更新(2回目)
stashでコンフリクト発生
複数内容のスタッシュ2加盟

---

## デスクトップファイル整理アプリ 📁

デスクトップ上のファイルを自動的に整理するPythonアプリケーションです。

### 機能

- ファイルの拡張子に基づいて自動分類
- 以下のカテゴリに整理：
  - 📷 画像（.jpg, .png, .gif など）
  - 📄 ドキュメント（.pdf, .docx, .txt など）
  - 🎵 音楽（.mp3, .wav, .flac など）
  - 🎬 動画（.mp4, .avi, .mkv など）
  - 📦 アーカイブ（.zip, .rar, .7z など）
  - 💻 プログラム（.py, .js, .html など）
  - 📎 その他
- ドライランモードで事前確認可能
- 整理ログの自動記録

### インストール

#### クイックスタート（Linux / macOS）

```bash
# セットアップスクリプトを実行
./setup.sh
```

対話形式で選択できます：
1. シンボリックリンク作成（推奨） - `organize-desktop` コマンドで実行
2. エイリアス作成 - シェル設定に追加
3. 直接実行 - セットアップ不要

#### Windows の場合

`organize-desktop.bat` をダブルクリックして実行するか、以下のコマンドを使用：

```cmd
python desktop_organizer.py --dry-run
```

詳しいインストール方法は [INSTALL.md](INSTALL.md) をご覧ください。

### 使い方

#### 基本的な使い方

```bash
# デスクトップを整理（実行前に確認）
python3 desktop_organizer.py --dry-run

# デスクトップを実際に整理
python3 desktop_organizer.py
```

#### カスタムパスを指定

```bash
# 任意のフォルダを整理
python3 desktop_organizer.py --path /path/to/folder

# ドライランで確認
python3 desktop_organizer.py --path /path/to/folder --dry-run
```

### 必要な環境

- Python 3.6以上
- 標準ライブラリのみ使用（追加インストール不要）

### 注意事項

- 実行前に必ず `--dry-run` オプションで確認することをお勧めします
- 整理されたファイルは「整理済み」フォルダ内にカテゴリ別に配置されます
- 整理ログは `organizer_log.txt` に保存されます
- 同名ファイルが存在する場合、タイムスタンプが自動的に追加されます

### ライセンス

このプロジェクトはMITライセンスの下で公開されています。