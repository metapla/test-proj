"""
shapelyを使用してオブジェクトの位置関係を調べるプログラム
札幌管区気象台予報課　洪水情報係長　今泉
<参考にしたページ>
https://qiita.com/mamurata0924/items/23ab860f4d7429207fac
"""
import geopandas as gpd
import pyproj
from pyproj import CRS
from shapely.geometry import Point
import matplotlib.pyplot as plt
import os

def main():
    # 札幌市のポイントを含むGeoDataFrameを作成
    sapporo_lon = 141.34694
    sapporo_lat = 43.06417
    sapporo = gpd.GeoDataFrame([[Point(sapporo_lon, sapporo_lat)]],
                               geometry='geometry', crs=CRS('epsg:4326'), columns=['geometry'])

    # 地球楕円体から正距方位図法への変換（proj='aepd':正距方位図法、ellips='WGS84':地球楕円体、datum:測地基準系）
    aeqd = pyproj.Proj(proj='aeqd', ellps='WGS84', datum='WGS84',
                       lat_0=sapporo_lat, lon_0=sapporo_lon).srs
    sapporo = sapporo.to_crs(crs=aeqd)
    print(sapporo)
    print('\nCRS:\n', sapporo.crs)

    # 市町村等をまとめた地域のシェープファイルを正距方位図法に変換する
    fp = 'shape/matome_20200526/matome_20200526.shp'
    matome_aeqd = gpd.read_file(fp)
    matome_aeqd = matome_aeqd.to_crs(crs=aeqd)
    print(matome_aeqd.head(2))

    # 市町村等をまとめた地域と札幌市をプロット
    fig, ax = plt.subplots(figsize=(10, 10))
    matome_aeqd.plot(ax=ax)
    sapporo.plot(ax=ax, color='#e41a1c', markersize=10)
    plt.savefig('distance_study.png')

    # 各ポリゴンの重心をcentroidで計算
    matome_aeqd['centroid'] = matome_aeqd.centroid
    print(matome_aeqd.head(2))

    # 札幌の中心点の座標を取得
    sapporo_geom = sapporo.loc[0, 'geometry']
    print(sapporo_geom)

    # 各市町村等をまとめた地域と札幌間の距離を計算
    matome_aeqd = matome_aeqd.apply(
        calculate_distance, dest_geom=sapporo_geom, src_col='centroid', target_col='dist_to_Sap', axis=1)
    print(matome_aeqd.head(10))

    # 各市町村等をまとめた地域から札幌までの最長距離及び平均距離を取得
    max_dist = matome_aeqd['dist_to_Sap'].max()
    mean_dist = matome_aeqd['dist_to_Sap'].mean()

    print("Maximum distance to Sapporo is %.0f km, and the mean distance is %.0f km." % (max_dist, mean_dist))



# 距離を計算するための関数
def calculate_distance(row, dest_geom, src_col='geometry', target_col='distance'):
    dist = row[src_col].distance(dest_geom)
    dist_km = dist / 1000
    row[target_col] = dist_km
    return row


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
