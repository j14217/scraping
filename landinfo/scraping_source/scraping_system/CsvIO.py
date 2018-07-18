import csv


class CsvInput:
    def __init__(self):
        self.config_path = ".\\venvtest\\Sourse\\scraping\\csv\\config.csv"

    # 設定ファイルの読み込み
    def config_reader(self, site):
        with open(self.config_path, "r", encoding="utf-8") as c:
            reader = csv.DictReader(c)
            for row in reader:
                if site in row.values():
                    config = row
            return config


class CsvOutput:
    def __init__(self, filepath):
        self.filepath = filepath
        self.header_flag = True
        self.exclusion_list_atsu = [
            " ",
            "仲介手数料",
            "その他交通",
            "販売代理",
            "物件名",
        ]
        self.exclusion_list_ya = [
            "その他費用",
            "建築条件備考",
            "最多価格帯",
            "販売区画数",
        ]

    # csvへ書き込み
    def csv_writer(self, site, data):
        with open(self.filepath, "a", encoding="utf-8") as f:
            if self.header_flag:
                keys = ""
                for k in data[0].keys():
                    if (site == "athome") or (site == "suumo"):
                        if k in self.exclusion_list_atsu:
                            pass
                        else:
                            keys += (k + ",")
                    elif (site == "yahoo"):
                        if k in self.exclusion_list_ya:
                            pass
                        else:
                            keys += (k + ",")
                f.write(keys.rstrip(",") + "\n")
                self.header_flag = False

            for d in data:
                values = ""
                for key, value in d.items():
                    if (site == "athome") or (site == "suumo"):
                        if key in self.exclusion_list_atsu:
                            pass
                        else:
                            values += (
                                value.replace("\n", " ").replace(",", "") + ","
                            )
                    elif (site == "yahoo"):
                        if key in self.exclusion_list_ya:
                            pass
                        else:
                            values += (
                                value.replace("\n", " ").replace(",", "") + ","
                            )
                f.write(values.rstrip(",") + "\n")

        # 書き込みの終了を伝える旨
        print("-> Writing data is finish")
