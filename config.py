import configparser
import os


# 操作config类
class OperateConfig:
    def __init__(self, path):
        # 创建一个ConfigParser对象
        self.path = path
        self.config = configparser.ConfigParser()
        # 读取配置文件
        # self.config.read('co33nfig.ini')
        # 指定文件编码并读取配置
        with open(self.path, encoding='utf-8') as f:
            self.config.read_file(f)

    # 获取keys
    def get_api_keys(self):
        keys_dict = {}
        # 访问配置文件中的key
        keys = self.config['Keys']
        for key in keys:
            keys_dict[key] = keys[key]
        return keys_dict

    # 获取flags
    def get_flags(self):
        flag_dict = {}
        # 访问配置文件中的key
        flags = self.config['flag']
        for flag in flags:
            flag_dict[flag] = self.config.getboolean('flag', flag)
        return flag_dict

    # 修改flags
    def change_flags(self, flag_dict):
        # 检查并修改 [flag] 部分

        self.config['flag']['threat_level'] = str(flag_dict["threat_level"])
        self.config['flag']['malware_type'] = str(flag_dict["malware_type"])
        self.config['flag']['malware_family'] = str(flag_dict["malware_family"])
        self.config['flag']['file_name'] = str(flag_dict["file_name"])
        self.config['flag']['file_type'] = str(flag_dict["file_type"])
        self.config['flag']['tag'] = str(flag_dict["tag"])
        self.config['flag']['threat_score'] = str(flag_dict["threat_score"])
        self.config['flag']['multi_engines'] = str(flag_dict["multi_engines"])

        # 写回配置文件
        with open(self.path, 'w', encoding="utf-8") as configfile:
            self.config.write(configfile)

    def get_hint(self):
        hint_dict = {}
        # 访问配置文件中的key
        hints = self.config['hint']
        for hint in hints:
            hint_dict[hint] = hints[hint]
        return hint_dict


if __name__ == '__main__':
    a = OperateConfig()
    b = a.get_hint()
    print(b)
