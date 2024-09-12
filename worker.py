import requests
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import sys
import time


security_terms = {
    "APT": {
        "中文": "APT",
        "危害度": "严重",
        "释义": "高级持续性威胁(Advanced Persistent Threat)，指隐蔽而持久的网络攻击，通常出于政治或商业动机。"
    },
    "Backdoor": {
        "中文": "后门",
        "危害度": "高",
        "释义": "后门是一类允许攻击者远程控制主机的木马病毒，一般通过构造隐蔽通道实现。"
    },
    "Exploit": {
        "中文": "漏洞利用",
        "危害度": "高",
        "释义": "包含漏洞利用代码，通常恶意软件会利用软件和系统漏洞进行攻击。"
    },
    "Keylogger": {
        "中文": "键盘记录器",
        "危害度": "高",
        "释义": "键盘记录器会记录主机上所有的键盘输入操作，可被用作监控工具，也可能被用于收集账密等敏感信息进行网络犯罪。"
    },
    "RAT": {
        "中文": "远程访问木马",
        "危害度": "高",
        "释义": "远程访问木马，有时也指远程访问工具，允许攻击者远程访问和控制目标主机。"
    },
    "Rootkit": {
        "中文": "Rootkit",
        "危害度": "高",
        "释义": "Rootkit使用各种技术来隐藏自身或执行的恶意活动，如文件、进程或网络活动。"
    },
    "Bootkit": {
        "中文": "Bootkit",
        "危害度": "高",
        "释义": "Bootkit通常会感染和修改MBR、VBR、BIOS、UEFI等进行持久化操作。"
    },
    "Stealer": {
        "中文": "窃密",
        "危害度": "高",
        "释义": "窃密类木马程序，通常会收集系统信息、隐私信息和窃取文档。"
    },
    "Trojan": {
        "中文": "木马",
        "危害度": "中",
        "释义": "木马是一类会执行未经授权操作的恶意程序，如下载其他恶意程序和窃取隐私，会破坏系统的安全性。"
    },
    "Worm": {
        "中文": "蠕虫",
        "危害度": "中",
        "释义": "蠕虫是一类能自我复制和自动传播的恶意程序。"
    },
    "Virus": {
        "中文": "病毒",
        "危害度": "中",
        "释义": "病毒包含可复制的代码，通过感染各种文件进行传播。"
    },
    "Ransomware": {
        "中文": "勒索软件",
        "危害度": "中",
        "释义": "勒索软件是一类通过加密文件或劫持资源等以此向用户勒索钱财的恶意软件。"
    },
    "Spyware": {
        "中文": "间谍软件",
        "危害度": "中",
        "释义": "间谍软件是一类未经用户授权收集用户个人信息的恶意软件。"
    },
    "Riskware": {
        "中文": "风险软件",
        "危害度": "中",
        "释义": "风险软件本身没有恶意但可能被用于恶意目的，具备一定风险。"
    },
    "PWS": {
        "中文": "密码窃取者",
        "危害度": "中",
        "释义": "密码窃取者指的是一种专门窃取用户账密的恶意程序，目标包含IM、浏览器、游戏、邮件客户端等。"
    },
    "Malware": {
        "中文": "恶意软件",
        "危害度": "中",
        "释义": "恶意软件，泛指一切具备恶意行为的软件，会对系统造成危害。"
    },
    "Hacktool": {
        "中文": "黑客工具",
        "危害度": "中",
        "释义": "黑客工具指的是自身通常没有危害行为，但可被黑客利用发起攻击的工具。"
    },
    "Adware": {
        "中文": "广告软件",
        "危害度": "低",
        "释义": "广告软件一般会通过横幅和弹窗等形式展示广告，通常还会收集系统和用户相关的信息。"
    },
    "Pack": {
        "中文": "壳",
        "危害度": "低",
        "释义": "通过加密和压缩等方式进行加壳，用于保护自身和对抗分析。"
    },
    "Rogueware": {
        "中文": "流氓软件",
        "危害度": "低",
        "释义": "流氓软件是具有一定流氓行为的程序，多包含捆绑、静默推广和频繁弹窗等行为。"
    },
    "Pornware": {
        "中文": "色情软件",
        "危害度": "低",
        "释义": "色情软件是一类包含色情内容的程序。"
    },
    "Tool": {
        "中文": "工具",
        "危害度": "低",
        "释义": "泛指工具类软件。"
    },
    "PUA": {
        "中文": "潜在有害应用",
        "危害度": "低",
        "释义": "潜在有害应用，通常是在用户不知情或不情愿的情况下被安装到主机上，多指捆绑和流氓软件。"
    },
    "PUP": {
        "中文": "潜在有害程序",
        "危害度": "低",
        "释义": "潜在有害程序，通常是在用户不知情或不情愿的情况下被安装到主机上，多指捆绑和流氓软件。"
    },
    "Joke": {
        "中文": "恶搞软件",
        "危害度": "低",
        "释义": "恶搞软件，多会通过声音或图像等吓唬用户，一般不会对系统造成危害。"
    },
    "Grayware": {
        "中文": "灰色软件",
        "危害度": "低",
        "释义": "灰色软件，通常泛指包含广告和流氓等行为的软件，一般不认为是恶意程序。"
    },
    "Susware": {
        "中文": "可疑软件",
        "危害度": "低",
        "释义": "可疑软件，泛指一切可能具备可疑行为的软件。"
    }
}


class Worker(QObject):
    # 定义信号，用于通知任务进度
    progress = Signal(int)
    # 定义信号，用于通知任务完成
    finished = Signal()

    callback_info = Signal(str) # str
    callback_error = Signal(str) # str
    label_md5_id = Signal(int) # str
    label_key_id = Signal(int)
    callback_result = Signal(list, int) # list

    def __init__(self, mainwindow):
        super().__init__()
        self.widget = mainwindow  # 保存 MainWindow 实例

        self.api_times = 0
        self.api_id = 1
        self.no_found_hint = self.widget.no_found_hint

    @Slot()
    def run(self):
        # self.widget.md5_dict
        for md5_row, md5 in self.widget.md5_dict.items():
            self.api_times = 0
            # self.widget.label_md5_id.setText(str(md5_row))
            self.label_md5_id.emit(md5_row)
            flag = self.__get_request(md5_row, md5)
            if flag:
                break
            md5_row += 1
        self.finished.emit()
    def __get_api_key(self):
        self.api_id += 1
        if self.api_id > self.widget.api_dict_len:
            self.api_id = 1
        self.label_key_id.emit(self.api_id)
        return self.widget.api_dict[f"key{self.api_id}"]

    def __get_request(self, md5_row, md5):
        # url = "https://api.threatbook.cn/v3/file/report/multiengines"
        url = 'https://api.threatbook.cn/v3/file/report'
        api_key = self.__get_api_key()
        data = {
            "apikey": api_key,
            "resource": md5
        }
        try:
            response = requests.post(url, data=data).json()
            response_code = response['response_code']
            if response_code == -1:
                # self.widget.callback_error(f"错误key,{api_key}")
                self.callback_error.emit(f"权限受限或请求出错，行数：{md5_row}")
            elif response_code == -4:
                if self.api_times >= 60:
                    self.callback_error.emit("api_key已全无额度")
                    self.finished.emit()  # 任务完成后发送完成信号
                    return True
                self.callback_info.emit('请求过快，已切换apikey')
                return self.__get_request(md5_row, md5)
            elif response_code == 0 or response_code == 1:
                self.__parse(response, md5_row)
            else:
                # self.callback_info.emit(response)
                self.rep_callback(None, md5_row)
            return False
        except requests.exceptions.RequestException as e:
            self.callback_error.emit(f"网络请求出现异常：{e}")
            return True

    def rep_callback(self, summarySet, md5_row):
        result = []
        for f_key, f_value in self.widget.flag_dict.items():
            if f_value:
                if summarySet:
                    result.append(summarySet[f_key])
                else:
                    result.append(self.no_found_hint)
                # self.callback_info.emit(str(result))
                self.progress.emit(md5_row)
                self.callback_result.emit(result, md5_row)

    def __parse(self, response, md5_row):
        # 获取summary数据
        summary = response['data']['summary']
        # 威胁等级
        threat_level = summary.get('threat_level', '')
        if threat_level == "malicious":
            threat_level = "恶意"
        elif threat_level == "suspicious":
            threat_level = "可疑"
        elif threat_level == "clean":
            threat_level = "安全"
        # 威胁分类
        malware_type = summary.get('malware_type', '')
        if malware_type:
            malware_type = security_terms[malware_type]['中文']
        # md5 = summary.get('md5', '')
        # 病毒家族
        malware_family = summary.get('malware_family', '')
        # 文件名称
        file_name = summary.get('file_name', '')
        # 文件类型
        file_type = summary.get('file_type', '')
        # 反病毒扫描引擎检出率
        multi_engines = summary.get('multi_engines', '')
        # 威胁评分值
        threat_score = summary.get('threat_score', '')
        # 标签
        tag = summary.get('tag', {})  # 如果没有 'tag' 键，则赋值为一个空字典
        # 检测标签
        tag_x = ''
        x = tag.get('x', '')
        if isinstance(x, list):
            if len(x) > 1:
                tag_x = '|'.join(x)
            else:
                tag_x = x[0]
        elif isinstance(x, str):
            tag_x = x

        # 静态标签
        tag_s = ''
        s = tag.get('s', '')  # 如果没有 's' 键，则赋值为空字符串
        if isinstance(s, list):
            if len(s) > 1:
                tag_s = '|'.join(s)
            elif len(s) == 1:
                tag_s = s[0]
            else:
                tag_s = ''
        elif isinstance(s, str):
            tag_s = s
        tag = tag_s + '，' + tag_x
        summary_dict = {
            'threat_level': threat_level,
            'malware_type': malware_type,
            'malware_family': malware_family,
            'file_name': file_name,
            'file_type': file_type,
            'multi_engines': multi_engines,
            'threat_score': threat_score,
            'tag': tag
        }
        self.callback_info.emit(str(summary_dict))
        self.rep_callback(summary_dict, md5_row)