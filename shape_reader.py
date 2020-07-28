import geopandas as gpd
import matplotlib.pyplot as plt
import os

def main():
    # シェープファイルの読込
    df = gpd.read_file('shape/matome_20200526/matome_20200526.shp')

    # データタイプを取得
    print(type(df))

    # 最初の5行を取得
    print(df.head())

    # カラム指定してデータ取得
    print(df['geometry'].head)

    # 列名を取得
    print(df.columns)

    # 列の型を取得
    print(df.dtypes)

    # 座標参照系を取得
    print(df.crs)

    # 描画
    df.plot(color='white', edgecolor='black')

    # ファイル出力（拡張子はPDFでも可）
    plt.savefig('shape_reader.png')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
