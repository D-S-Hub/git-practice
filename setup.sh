#!/bin/bash
# デスクトップファイル整理アプリのセットアップスクリプト

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_NAME="desktop_organizer.py"
SCRIPT_PATH="$SCRIPT_DIR/$SCRIPT_NAME"

echo "=================================="
echo "デスクトップファイル整理アプリ"
echo "セットアップスクリプト"
echo "=================================="
echo ""

# スクリプトが存在するか確認
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "エラー: $SCRIPT_NAME が見つかりません"
    exit 1
fi

# Python 3がインストールされているか確認
if ! command -v python3 &> /dev/null; then
    echo "エラー: Python 3がインストールされていません"
    echo "Python 3.6以上をインストールしてください"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "Python バージョン: $PYTHON_VERSION"
echo ""

# セットアップ方法の選択
echo "セットアップ方法を選択してください："
echo ""
echo "1) シンボリックリンクを作成（推奨）"
echo "   ~/.local/bin/ にリンクを作成します"
echo "   コマンド名: organize-desktop"
echo ""
echo "2) エイリアスを作成"
echo "   ~/.bashrc または ~/.zshrc にエイリアスを追加します"
echo "   コマンド名: organize-desktop"
echo ""
echo "3) 現在の場所から直接実行"
echo "   セットアップは不要です"
echo ""

read -p "選択 (1/2/3): " choice

case $choice in
    1)
        # シンボリックリンクを作成
        BIN_DIR="$HOME/.local/bin"
        LINK_NAME="organize-desktop"

        # ディレクトリが存在しない場合は作成
        if [ ! -d "$BIN_DIR" ]; then
            mkdir -p "$BIN_DIR"
            echo "作成: $BIN_DIR"
        fi

        # 実行権限を付与
        chmod +x "$SCRIPT_PATH"

        # シンボリックリンクを作成
        ln -sf "$SCRIPT_PATH" "$BIN_DIR/$LINK_NAME"
        echo ""
        echo "✅ セットアップ完了！"
        echo ""
        echo "次のコマンドでPATHに追加してください（まだの場合）："
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
        echo ""
        echo "シェル設定ファイルに追加する場合："
        echo "  echo 'export PATH=\"\$HOME/.local/bin:\$PATH\"' >> ~/.bashrc"
        echo "  source ~/.bashrc"
        echo ""
        echo "使い方："
        echo "  organize-desktop --dry-run  # 確認モード"
        echo "  organize-desktop            # 実行"
        ;;

    2)
        # エイリアスを作成
        SHELL_RC=""
        if [ -n "$ZSH_VERSION" ]; then
            SHELL_RC="$HOME/.zshrc"
        elif [ -n "$BASH_VERSION" ]; then
            SHELL_RC="$HOME/.bashrc"
        else
            echo "シェル設定ファイルを手動で指定してください："
            read -p "パス (例: ~/.bashrc): " SHELL_RC
        fi

        ALIAS_LINE="alias organize-desktop='python3 $SCRIPT_PATH'"

        # すでにエイリアスが存在するか確認
        if grep -q "organize-desktop" "$SHELL_RC" 2>/dev/null; then
            echo "⚠️  エイリアスは既に存在します"
        else
            echo "" >> "$SHELL_RC"
            echo "# デスクトップファイル整理アプリ" >> "$SHELL_RC"
            echo "$ALIAS_LINE" >> "$SHELL_RC"
            echo ""
            echo "✅ セットアップ完了！"
        fi

        echo ""
        echo "次のコマンドで設定を反映してください："
        echo "  source $SHELL_RC"
        echo ""
        echo "使い方："
        echo "  organize-desktop --dry-run  # 確認モード"
        echo "  organize-desktop            # 実行"
        ;;

    3)
        # 直接実行
        chmod +x "$SCRIPT_PATH"
        echo ""
        echo "✅ 実行権限を付与しました！"
        echo ""
        echo "使い方："
        echo "  cd $SCRIPT_DIR"
        echo "  python3 desktop_organizer.py --dry-run  # 確認モード"
        echo "  python3 desktop_organizer.py            # 実行"
        echo ""
        echo "または："
        echo "  ./desktop_organizer.py --dry-run"
        ;;

    *)
        echo "無効な選択です"
        exit 1
        ;;
esac

echo ""
echo "詳しい使い方は README.md をご覧ください"
