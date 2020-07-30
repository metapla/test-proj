"""
座標参照系を変換するプログラム
T.Imaizumi
<参考にしたページ>
https://qiita.com/mamurata0924/items/23ab860f4d7429207fac
"""
import geopandas as gpd
import matplotlib.pyplot as plt
import os

def main():
    fp = 'shape/matome_20200526/matome_20200526.shp'
    # シェープファイルの読み込み
    data = gpd.read_file(fp)
    # オリジナルデータとして複製
    orig = data.copy()
    # 座標参照系の表示
    print(data.crs)
    # 最初の2行を出力
    print(data['geometry'].head(2))
    # 座標参照系の変換(epsg:4612 to epsg:900913)
    data = data.to_crs(epsg=900913)
    # 座標参照系の表示
    print(data.crs)
    # 最初の2行を表示
    print(data['geometry'].head(2))
    # 座標参照系の変更前後をプロット
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,8))
    # JGD2000（epsg:4612）
    orig.plot(ax=ax1, facecolor='gray');
    ax1.set_title('JGD2000');
    # Google Maps(epsg:900913)
    data.plot(ax=ax2, facecolor='blue');
    ax2.set_title('Google Maps Global Mercator');
    # プロットする
    plt.tight_layout()
    plt.savefig('crs_study.png')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
