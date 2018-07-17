import csv


class CsvInput:
    def __init__(self):
        pass

    # 設定ファイルの読み込み
    def config_reader(self, site, config_path):
        with open(config_path, "r", encoding="utf-8") as c:
            reader = csv.DictReader(c)
            for row in reader:
                if site in row.values():
                    config = row
            return config

    def csv_reader(self):
        pass


class CsvOutput:
    def __init__(self, filepath, data):
        self.filepath = filepath
        self.data = data
        self.header_flag = True
        self.exclusion_list = [
            " ",
            "仲介手数料",
            "その他交通",
            "販売代理",
            "物件名",
        ]

    # csvへ書き込み
    def csv_writer(self):
        with open(self.filepath, "a", encoding="utf-8") as f:
            if self.header_flag:
                keys = ""
                for k in self.data[0].keys():
                    if k in self.exclusion_list:
                        pass
                    else:
                        keys += (k + ",")
                f.write(keys.rstrip(",") + "\n")
                self.header_flag = False

            for d in self.data:
                values = ""
                for key, value in d.items():
                    if key in self.exclusion_list:
                        pass
                    else:
                        values += (
                            value.replace("\n", " ").replace(",", "") + ",")
                f.write(values.rstrip(",") + "\n")

        # 書き込みの終了を伝える旨
        print("-> Writing data is finish")