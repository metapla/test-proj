"""
インタラクティブマップの作成プログラム
T.Imaizumi
<参考にしたページ>
https://qiita.com/mamurata0924/items/23ab860f4d7429207fac
"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import geopandas as gpd
import folium
import branca

def label_encode(df, column_name):
    le = LabelEncoder()
    le = le.fit(df[column_name])
    return le.transform(df[column_name]).astype(int)

# 地形分類図の読み込み
gdf_land = gpd.read_file('shape/landform/landform.shp', encoding='shift-jis')
gdf_land = gdf_land[gdf_land['PREF']=='北海道']
gdf_land['terrain'] = label_encode(gdf_land, '地形大区分')
display(gdf_land.head(3))

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
