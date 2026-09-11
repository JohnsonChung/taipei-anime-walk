"""
台北動漫散步指南 - Google My Maps (KML/KMZ) 種子資料解析與清洗腳本
執行方式: python scripts/parse_kml_seed.py [path_to_kml_or_kmz]
"""

import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# 依據 AI 指引 03 (Data Cleanser) 定義之剔除詞
EXCLUDE_KEYWORDS = [
    "麥當勞", "肯德基", "星巴克", "屈臣氏", "康是美", "家樂福",
    "全家", "7-ELEVEN", "娃娃機", "選物販賣", "停車場", "加油站"
]

def parse_kml_file(kml_path: Path):
    if not kml_path.exists():
        print(f"[!] 找不到圖資檔案: {kml_path}")
        return []

    xml_content = None
    if kml_path.suffix.lower() == ".kmz":
        with zipfile.ZipFile(kml_path, 'r') as z:
            for filename in z.namelist():
                if filename.endswith(".kml"):
                    xml_content = z.read(filename)
                    break
    else:
        with open(kml_path, "r", encoding="utf-8") as f:
            xml_content = f.read()

    if not xml_content:
        print("[!] 無法讀取 KML 內容")
        return []

    root = ET.fromstring(xml_content)
    # KML 命名空間處理
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    
    placemarks = []
    for pm in root.findall(".//kml:Placemark", ns) or root.findall(".//Placemark"):
        name_elem = pm.find("kml:name", ns) or pm.find("name")
        name = name_elem.text.strip() if name_elem is not None and name_elem.text else "未命名點位"

        # 關鍵字過濾
        if any(bad in name for bad in EXCLUDE_KEYWORDS):
            continue

        desc_elem = pm.find("kml:description", ns) or pm.find("description")
        desc = desc_elem.text.strip() if desc_elem is not None and desc_elem.text else ""

        coord_elem = pm.find(".//kml:coordinates", ns) or pm.find(".//coordinates")
        coords = [0.0, 0.0]
        if coord_elem is not None and coord_elem.text:
            parts = coord_elem.text.strip().split(",")
            if len(parts) >= 2:
                try:
                    lng = round(float(parts[0]), 4)
                    lat = round(float(parts[1]), 4)
                    coords = [lng, lat]
                except ValueError:
                    pass

        # 聚落初步歸納 (商圈拓撲)
        cluster = "獨立散點"
        if 121.503 <= coords[0] <= 121.512 and 25.040 <= coords[1] <= 25.048:
            cluster = "西門商圈"
        elif 121.510 <= coords[0] <= 121.520 and 25.046 <= coords[1] <= 25.052:
            cluster = "台北地下街"
        elif 121.528 <= coords[0] <= 121.536 and 25.042 <= coords[1] <= 25.048:
            cluster = "光華三創"
        elif 121.528 <= coords[0] <= 121.540 and 25.010 <= coords[1] <= 25.020:
            cluster = "公館台大"

        placemarks.append({
            "name": name,
            "coordinates": coords,
            "cluster": cluster,
            "raw_description": desc
        })

    return placemarks

def main():
    target_path = Path("scripts/seeds/raw_map.kml")
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])

    print(f"[*] 正在解析種子圖資: {target_path}")
    spots = parse_kml_file(target_path)
    print(f"[+] 成功解析並保留 {len(spots)} 個二次元潛在候選點位")

    out_file = Path("scripts/seeds/extracted_spots.json")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(spots, f, ensure_ascii=False, indent=2)
    print(f"[+] 中繼資料已存入: {out_file}")

if __name__ == "__main__":
    main()
