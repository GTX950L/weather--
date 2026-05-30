"""
天气查询小工具
通过免费 API 查询任意城市的实时天气。
不需要 API Key，开箱即用。
"""

import urllib.request
import json


def 查询天气(城市):
    """
    通过 wttr.in 免费 API 查询指定城市的天气信息。
    返回格式化的天气数据字典，失败则返回 None。
    """
    # wttr.in 是一个免费的天气 API，返回 JSON 格式数据
    接口地址 = f"https://wttr.in/{城市}?format=j1"

    try:
        # 发送请求
        请求 = urllib.request.Request(接口地址)
        请求.add_header("User-Agent", "WeatherChecker/1.0")

        with urllib.request.urlopen(请求, timeout=10) as 响应:
            原始数据 = json.loads(响应.read().decode("utf-8"))

        # 提取当前天气
        当前 = 原始数据["current_condition"][0]

        天气信息 = {
            "城市": 城市,
            "温度": f"{当前['temp_C']}°C",
            "体感温度": f"{当前['FeelsLikeC']}°C",
            "天气": 当前["weatherDesc"][0]["value"],
            "湿度": f"{当前['humidity']}%",
            "风速": f"{当前['windspeedKmph']} km/h",
            "风向": 当前["winddir16Point"],
            "能见度": f"{当前['visibility']} km",
            "紫外线指数": 当前["uvIndex"],
        }

        return 天气信息

    except urllib.error.HTTPError:
        print(f"❌ 找不到城市「{城市}」，请检查城市名是否正确")
        return None
    except urllib.error.URLError:
        print("❌ 网络连接失败，请检查网络后重试")
        return None
    except Exception as e:
        print(f"❌ 查询出错：{e}")
        return None


def 显示天气(信息):
    """格式化显示天气信息"""
    if not 信息:
        return

    print(f"""
╔══════════════════════════════╗
║  🌤️  {信息['城市']} 实时天气
╠══════════════════════════════╣
║  天气：{信息['天气']}
║  温度：{信息['温度']}（体感 {信息['体感温度']}）
║  湿度：{信息['湿度']}
║  风速：{信息['风速']}（{信息['风向']}）
║  能见度：{信息['能见度']}
║  紫外线指数：{信息['紫外线指数']}
╚══════════════════════════════╝
""")


def 主程序():
    """主循环"""
    print("=" * 36)
    print("     🌤️  天气查询小工具")
    print("     输入城市名查天气")
    print("     输入 quit 退出")
    print("=" * 36)

    常用城市 = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "南京"]
    print(f"\n常用城市：{' | '.join(常用城市)}")

    while True:
        城市 = input("\n请输入城市名：").strip()

        if 城市.lower() == "quit":
            print("再见！👋")
            break

        if not 城市:
            print("请输入城市名！")
            continue

        print(f"正在查询 {城市} 的天气...")
        天气信息 = 查询天气(城市)
        显示天气(天气信息)


if __name__ == "__main__":
    主程序()
