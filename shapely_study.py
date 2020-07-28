"""
shapelyを使用してオブジェクトの位置関係を調べるプログラム
札幌管区気象台予報課　洪水情報係長　今泉
"""
from shapely.geometry import Point, Polygon

# Point オブジェクトの作成
p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)

# Polygon オブジェクトの作成
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)

# 確認
print(p1)
print(p2)
print(poly)

# ポイントがポリゴン内にあるかどうかを確認
print(p1.within(poly))
print(p2.within(poly))

# ポイントとポリゴンの重心を比較
print(p1)
print(poly.centroid)

# ポリゴンにポイントが含まれているかどうかを確認
print(poly.contains(p1))
print(poly.contains(p2))
