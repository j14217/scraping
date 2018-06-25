class LandInfo:
    def __init__(self):
        self.title = "title"
        self.location = "所在地"
        self.traffic = "交通"
#        self.land_area = "土地面積"
#        self.floor_space = "坪数"
#        self.price = "価格"
#        self.geograpy = "地目"
#        self.usage_area = "用途地域"
        self.url = "url"
        self.columns_list = "title, location, traffic, url"
        self.list = [""] * 4

    def info_list_add(self, num, info):
        self.list[num] = info

    def info_list_clear(self):
        self.list = [""] * 4
