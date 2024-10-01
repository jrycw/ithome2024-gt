import csv

columns = [
    "類別",
    "品名",
    "總熱量(Kcal)",
    "標準糖量(g)",
    "咖啡因總含量(mg)",
    "過敏原_麩質製品",
    "過敏原_牛奶製品",
    "售價(大杯)",
]

data = [
    dict(
        zip(
            columns,
            ("原葉茶", "鮮萃大麥紅茶", 91.8, 21.5, 118.1, "Y", "N", 40),
        )
    ),
    dict(
        zip(
            columns,
            ("原葉茶", "海神", 183.6, 43.1, 148.8, "N", "N", 45),
        )
    ),
    dict(
        zip(
            columns,
            ("奶茶", "鮮萃大麥奶茶", 525.4, 50.1, 177.1, "Y", "Y", 60),
        )
    ),
    dict(
        zip(
            columns,
            ("奶茶", "海神奶茶", 525.4, 50.1, 223.2, "N", "Y", 65),
        )
    ),
    dict(
        zip(
            columns,
            ("鮮奶茶", "四季春拿鐵", 298.1, 52.3, 216.0, "N", "Y", 65),
        )
    ),
    dict(
        zip(
            columns,
            ("鮮奶茶", "玫瑰普洱拿鐵", 298.1, 52.3, 294.8, "N", "Y", 70),
        )
    ),
]


with open("comebuy.csv", "w", encoding="utf-8", newline="\n") as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(data)
