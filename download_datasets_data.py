import os
import requests
import json

# 设定 API URL
url = "https://materials.hybrid3.duke.edu/materials/datasets/?page=1&page_size=3000"

# 指定保存文件的文件夹路径
save_dir = r"E:\H3"  # 使用 r"" 避免转义字符问题
file_name = "all_datasets_data.json"

# 创建文件夹（如果不存在）
os.makedirs(save_dir, exist_ok=True)

# 组合完整路径
file_path = os.path.join(save_dir, file_name)

# 发送 GET 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()
    # 保存数据到指定路径
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"数据已成功下载并保存至 {file_path}")
else:
    print("请求失败，状态码:", response.status_code)
