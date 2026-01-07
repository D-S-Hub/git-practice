#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
デスクトップファイル整理アプリ
Desktop File Organizer

このスクリプトはデスクトップ上のファイルを自動的に整理します。
ファイルの拡張子に基づいて適切なフォルダに移動します。
"""

import os
import shutil
from pathlib import Path
from datetime import datetime


class DesktopOrganizer:
    """デスクトップのファイルを整理するクラス"""

    # ファイルタイプごとのカテゴリ定義
    FILE_CATEGORIES = {
        '画像': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
        'ドキュメント': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.odt', '.ods'],
        '音楽': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
        '動画': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'アーカイブ': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'プログラム': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.sh', '.php', '.rb'],
        'その他': []  # 上記以外のファイル
    }

    def __init__(self, desktop_path=None):
        """
        初期化

        Args:
            desktop_path: デスクトップのパス（Noneの場合は自動検出）
        """
        if desktop_path is None:
            self.desktop_path = self._get_desktop_path()
        else:
            self.desktop_path = Path(desktop_path)

        self.log_file = self.desktop_path / 'organizer_log.txt'
        self._log(f"デスクトップパス: {self.desktop_path}")

    def _get_desktop_path(self):
        """デスクトップのパスを取得（OS別に対応）"""
        home = Path.home()

        # Windows, Mac, Linux に対応
        possible_paths = [
            home / 'Desktop',
            home / 'デスクトップ',
            home / 'desktop'
        ]

        for path in possible_paths:
            if path.exists():
                return path

        # デフォルトでHomeディレクトリを返す
        return home

    def _log(self, message):
        """ログメッセージを記録"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}\n"
        print(log_message.strip())

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_message)

    def _get_file_category(self, file_path):
        """
        ファイルのカテゴリを取得

        Args:
            file_path: ファイルのパス

        Returns:
            カテゴリ名
        """
        ext = file_path.suffix.lower()

        for category, extensions in self.FILE_CATEGORIES.items():
            if ext in extensions:
                return category

        return 'その他'

    def organize(self, dry_run=False):
        """
        デスクトップを整理

        Args:
            dry_run: Trueの場合、実際にファイルを移動せずに結果を表示
        """
        if not self.desktop_path.exists():
            self._log(f"エラー: デスクトップパスが見つかりません: {self.desktop_path}")
            return

        self._log("=" * 50)
        self._log("デスクトップファイル整理を開始します")
        self._log(f"モード: {'ドライラン（確認のみ）' if dry_run else '実行'}")
        self._log("=" * 50)

        # 整理用フォルダの作成
        organized_folder = self.desktop_path / '整理済み'

        if not dry_run and not organized_folder.exists():
            organized_folder.mkdir()
            self._log(f"フォルダ作成: {organized_folder}")

        # デスクトップのファイルをスキャン
        files_moved = 0
        files_skipped = 0

        for item in self.desktop_path.iterdir():
            # ディレクトリやシステムファイルはスキップ
            if item.is_dir() or item.name.startswith('.') or item == self.log_file:
                continue

            # このスクリプト自体はスキップ
            if item.name == 'desktop_organizer.py':
                continue

            # カテゴリを取得
            category = self._get_file_category(item)

            # カテゴリフォルダのパス
            category_folder = organized_folder / category

            # 移動先のパス
            destination = category_folder / item.name

            # ファイル名が既に存在する場合は、タイムスタンプを追加
            if destination.exists():
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                name_without_ext = item.stem
                destination = category_folder / f"{name_without_ext}_{timestamp}{item.suffix}"

            if dry_run:
                self._log(f"[確認] {item.name} → {category}/{destination.name}")
                files_moved += 1
            else:
                try:
                    # カテゴリフォルダを作成
                    category_folder.mkdir(parents=True, exist_ok=True)

                    # ファイルを移動
                    shutil.move(str(item), str(destination))
                    self._log(f"移動: {item.name} → {category}/{destination.name}")
                    files_moved += 1
                except Exception as e:
                    self._log(f"エラー: {item.name} の移動に失敗 - {str(e)}")
                    files_skipped += 1

        self._log("=" * 50)
        self._log(f"整理完了: {files_moved}個のファイルを処理")
        if files_skipped > 0:
            self._log(f"スキップ: {files_skipped}個のファイル")
        self._log("=" * 50)


def main():
    """メイン関数"""
    import argparse

    parser = argparse.ArgumentParser(
        description='デスクトップのファイルを自動整理します',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--path',
        type=str,
        help='整理するフォルダのパス（デフォルト: デスクトップ）'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='実際にファイルを移動せず、結果を確認のみ'
    )

    args = parser.parse_args()

    # オーガナイザーを作成して実行
    organizer = DesktopOrganizer(desktop_path=args.path)
    organizer.organize(dry_run=args.dry_run)


if __name__ == '__main__':
    main()
