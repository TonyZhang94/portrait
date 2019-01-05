# -*- coding:utf-8 -*-


class ClearMethod(object):
    def __init__(self):
        self.blanks = ["\\xa"]

    def clear(self, df):
        return df

    def no_blank(self, text):
        for blank in self.blanks:
            text = text.replace(blank, "")
        return text.strip()


class CombineBrandModel(ClearMethod):
    def clear(self, df):
        super().clear(df)
        df["serial"] = ""
        for k, v in df.iterrows():
            brand = self.no_blank(v["brand"])
            model = self.no_blank(v["model"])
            df.at[k, ["serial"]] = "%s-%s" % (brand, model)
        return df


class ClearNone(ClearMethod):
    def clear(self, df):
        """Fill None"""
        return df


if __name__ == '__main__':
    pass
