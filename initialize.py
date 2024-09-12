import configparser


class InitializeConfig:
    def __init__(self):
        self.run()

    @staticmethod
    def run(path):
        # 字典数据
        key_data = {
            'key1': '',
        }

        # [flag] 部分数据
        flag_data = {
            'threat_level': 'True',
            'malware_type': 'True',
            'malware_family': 'True',
            'file_name': 'False',
            'file_type': 'False',
            'tag': 'False',
            'threat_score': 'False',
            'multi_engines': 'False'
        }

        hint_data = {
            'no_found_hint': '"未查询到数据"'
        }

        # 创建ConfigParser对象
        config = configparser.ConfigParser()

        # 添加数据到配置文件
        config['Keys'] = key_data
        config['flag'] = flag_data
        config['hint'] = hint_data

        # 写入配置文件
        print(path)
        with open(path, 'w', encoding="utf-8") as configfile:
            config.write(configfile)
        # print("config.ini 文件已创建并写入成功")


if __name__ == '__main__':
    InitializeConfig()
