"""
ディレクトリを作成するツール
"""
import os
areas = ['10_アフリカ', '20_アメリカ', '30_アジア', '40_ヨーロッパ', '50_オセアニア']
for area in areas:
    os.mkdir(area)
