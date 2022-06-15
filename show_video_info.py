# 動画ファイルからサイズ情報やサムネイルをPythonのOpenCVで取得
# https://qiita.com/suzuki-navi/items/ffe449c95fb6e1faf891

# 動画ファイルの構造
# https://qiita.com/satken2/items/d14b4113fe3fb5f5597b

# このまま実行すればオッケー

import os
import cv2
import glob

video_files = glob.glob('*.mp4')

for video_file in video_files:
    print("--------------------------------------------------------------------------")
    cap = cv2.VideoCapture(video_file)

    # ファイル名
    print(f"{video_file}")

    # 横幅
    print(f"width\t\t: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")

    # 高さ
    print(f"height\t\t: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")

    # フレームレート
    print(f"fps\t\t\t: {cap.get(cv2.CAP_PROP_FPS)}")

    # フレーム数
    print(f"frame_count\t: {cap.get(cv2.CAP_PROP_FRAME_COUNT)}")

    # 再生時間
    print(f"length\t\t: {cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)} s")

    print("fourcc\t\t: " + int(cap.get(cv2.CAP_PROP_FOURCC)).to_bytes(4, "little").decode("utf-8"))
    # fourcc: avc1
    # コーデックの種類を4文字で表すコード

    # ファイルサイズ
    print(f"size\t\t: {os.path.getsize(video_file)} BT")

