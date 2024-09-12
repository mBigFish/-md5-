import os
import sys
from tkinter import filedialog
import pandas as pd
from PySide6.QtCore import QThread, Signal, QUrl, Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QTableWidgetItem
from main_window import Ui_Form
from config import OperateConfig
from worker import Worker
from initialize import InitializeConfig


class GuiWindow(QWidget, Ui_Form):

    def __init__(self):
        """"""
        """GUI"""
        super().__init__()
        self.setupUi(self)
        self.initialize()

        """初始化"""
        # config类
        self.operate_config = OperateConfig(self.config_path)
        self.api_dict = self.operate_config.get_api_keys()
        self.flag_dict = self.operate_config.get_flags()
        self.no_found_hint = self.operate_config.get_hint()["no_found_hint"]
        # 信号
        self.btn_start_clicked_signal = Signal()
        # 初始化
        self.checkbox_set()
        self.table_change()
        self.api_dict_len = len(self.api_dict)
        font = QFont("Courier", 9)  # 使用 Arial 字体，字号 12
        self.table.setFont(font)
        self.bind()

    def initialize(self):
        """mac"""
        # home_path = os.environ["HOME"]
        # weibu_path = home_path + '/WeibuConfig'
        # if not os.path.exists(weibu_path):
        #     os.mkdir(weibu_path)
        # self.config_path = weibu_path + "/config.ini"
        # if not os.path.exists(self.config_path):
        #     self.show_message_box("检测到本机是第一次使用，将为您在本目录下创建配置文件，完成初始化操作！")
        #     InitializeConfig.run(self.config_path)
        #     self.show_message_box("已经成功完成初始操作，欢迎使用！")

        """windows"""
        self.present_path = os.getcwd()
        self.config_path = self.present_path + "/config.ini"
        if not os.path.exists(self.config_path):
            self.show_message_box("检测到本机是第一次使用，将为您在本目录下创建配置文件，完成初始化操作！")
            InitializeConfig.run(self.config_path)
            self.show_message_box("已经成功完成初始操作，欢迎使用！")

    # 信号绑定槽函数
    def bind(self):
        """"""
        """内容"""
        self.lcd_key_count.display(len(self.api_dict))
        self.lcd_key_id.display(0)
        self.lcd_md5_id.display(0)

        """底栏"""
        self.btn_ret.clicked.connect(self.close_application)
        self.btn_start.clicked.connect(self.start_thread)
        self.btn_callback_file.clicked.connect(self.export_to_excel)
        self.btn_callback_file.setEnabled(False)

        """配置"""
        self.btn_choose_file_txt.clicked.connect(self.func_btn_choose_file_txt)
        self.btn_choose_file_excel.clicked.connect(self.func_btn_choose_file_excel)
        self.line_choose_file.setReadOnly(True)
        self.line_choose_file.setPlaceholderText("请选择文件....")

        self.box_threat_level.stateChanged.connect(self.checkbox_changed) # 威胁等级
        self.box_malware_type.stateChanged.connect(self.checkbox_changed) # 威胁分类
        self.box_malware_family.stateChanged.connect(self.checkbox_changed) #威胁家族
        self.box_file_name.stateChanged.connect(self.checkbox_changed) # 文件名称
        self.box_file_type.stateChanged.connect(self.checkbox_changed) # 文件类型
        self.box_tag.stateChanged.connect(self.checkbox_changed) # 标签
        self.box_threat_score.stateChanged.connect(self.checkbox_changed) # 评分值
        self.box_multi_engines.stateChanged.connect(self.checkbox_changed) # 检出率

    def func_btn_choose_file_txt(self):
        # file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        # 打开文件对话框并获取选择的文件路径
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Text Files (*.txt)")
        self.line_choose_file.setText(file_path)

        # 检查用户是否选择了文件
        if file_path:
            self.line_choose_file.setPlaceholderText(file_path)
            self.load_file_txt(file_path)
        else:
            print("没有选择文件")

    def func_btn_choose_file_excel(self):
        # 打开文件对话框以获取Excel文件路径
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, "选择Excel文件", "", "Excel文件 (*.xlsx *.xls);;所有文件 (*)")[0]
        # file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.line_choose_file.setText(file_path)

        # 检查用户是否选择了文件
        if file_path:
            self.line_choose_file.setPlaceholderText(file_path)
            self.load_file_excel(file_path)
        else:
            print("没有选择文件")

    # 读取文件
    def load_file_txt(self, file_path):
        with open(file_path, "r", encoding="utf-8") as fp:
            lines = fp.readlines()

        self.table.setRowCount(len(lines))
        for row, line in enumerate(lines):
            line = line.strip()  # 去掉行末尾的换行符
            # 添加序号
            # seq_item = QTableWidgetItem(str(row + 1))  # 序号从1开始
            # self.table.setItem(row, 0, seq_item)

            # 添加文本内容
            data_item = QTableWidgetItem(line)
            self.table.setItem(row, 0, data_item)  # 将内容填入第二列（A列）
            if not len(line) == 32:
                self.write_table(["md5值错误"], row)
                self.callback_info(f"第{row}行，md5值错误！")
                self.show_message_box(f"第{row}行，md5值错误！")
        self.table.setColumnWidth(0, 250)  # 设置第一列宽度为 150 像素

        self.callback_info("导入数据成功！")

    # 读取文件
    def load_file_excel(self, file_path):
        # 使用 pandas 读取 Excel 文件
        df = pd.read_excel(file_path)

        # 确定使用的列名（假设列名为 "md5" 或 "样本"）
        if 'md5' in df.columns:
            column_name = 'md5'
        elif '样本' in df.columns:
            column_name = '样本'
        else:
            self.show_message_box("找不到 'md5' 或 '样本' 列!")
            return

        # 设置表格行数
        self.table.setRowCount(len(df))
        # self.table.setColumnCount(1)  # 只显示一列，更多列可以根据需要添加

        # 填充表格数据
        for row, value in enumerate(df[column_name]):
            data_item = QTableWidgetItem(str(value))
            self.table.setItem(row, 0, data_item)

            # 检查md5值的长度是否为32
            if len(str(value)) != 32:
                self.write_table(["md5值错误"], row)
                self.callback_info(f"第{row}行，md5值错误！")
                self.show_message_box(f"第{row}行，md5值错误！")

        self.table.setColumnWidth(0, 250)  # 设置第一列宽度为 250 像素

        self.callback_info("导入数据成功！")

    @Slot(list, int)
    def write_table(self, result, md5_row):
        for column, value in enumerate(result):
            column += 1
            # self.table.setRowCount(1)
            data_item = QTableWidgetItem(value)
            self.table.setItem(md5_row, column, data_item)  # 将内容填入第二列（A列）

    # 复选框设置
    def checkbox_set(self):
        self.box_threat_level.setChecked(self.flag_dict["threat_level"])
        self.box_malware_type.setChecked(self.flag_dict["malware_type"])
        self.box_malware_family.setChecked(self.flag_dict["malware_family"])
        self.box_file_name.setChecked(self.flag_dict["file_name"])
        self.box_file_type.setChecked(self.flag_dict["file_type"])
        self.box_tag.setChecked(self.flag_dict["tag"])
        self.box_threat_score.setChecked(self.flag_dict["threat_score"])
        self.box_multi_engines.setChecked(self.flag_dict["multi_engines"])

    # 复选框点击
    def checkbox_changed(self):
        # 获取复选框的状态
        self.flag_dict["threat_level"] = True if self.box_threat_level.isChecked() else False
        self.flag_dict["malware_type"] = True if self.box_malware_type.isChecked() else False
        self.flag_dict["malware_family"] = True if self.box_malware_family.isChecked() else False
        self.flag_dict["file_name"] = True if self.box_file_name.isChecked() else False
        self.flag_dict["file_type"] = True if self.box_file_type.isChecked() else False
        self.flag_dict["tag"] = True if self.box_tag.isChecked() else False
        self.flag_dict["threat_score"] = True if self.box_threat_score.isChecked() else False
        self.flag_dict["multi_engines"] = True if self.box_multi_engines.isChecked() else False

        self.config_change(self.flag_dict)
        self.table_change()

    def config_change(self, flag_dict):
        self.operate_config.change_flags(flag_dict)
        callback_info = f"内容配置文件已修改成功"
        self.callback_info(callback_info)

    def table_change(self):
        table_column = 1
        table_header = ["md5"]
        for f_key, f_value in self.flag_dict.items():
            if f_value:
                table_column += 1
                table_header.append(f_key)
        self.table.setColumnCount(table_column)
        self.table.setHorizontalHeaderLabels(table_header)

    def export_to_excel(self):
        """将 QTableWidget 的数据导出为 Excel 文件"""
        # 获取表头
        headers = [self.table.horizontalHeaderItem(col).text() for col in range(self.table.columnCount())]

        # 获取表格数据
        row_count = self.table.rowCount()
        col_count = self.table.columnCount()

        data = []
        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = self.table.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)

        # 创建 DataFrame
        df = pd.DataFrame(data, columns=headers)

        # 打开文件对话框以选择保存位置
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx)", options=options)

        if file_name:
            # 导出到 Excel 文件
            df.to_excel(file_name, index=False, engine='openpyxl')
            # print(f"Data exported to {file_name}")
            self.callback_info(f"数据导出成功，位置：{file_name}")

    def callback(self, info):
        callback_info = info     # 设置字体颜色、背景颜色、边框颜色和边框宽度
        self.label_callback.setStyleSheet("""
            QLineEdit {
                color: green;
                background: pink;
                border: 2px solid blue;  
                padding: 5px; 
                border-radius: 5px; 
            }
            """)
        self.label_callback.setText(callback_info)

    def callback_info(self, info):
        callback_info = info  # 设置字体颜色、背景颜色、边框颜色和边框宽度
        self.label_callback.setStyleSheet("""
            QLineEdit {
                color: green;
                background: pink;
                border: 2px solid red;  
                padding: 5px; 
                border-radius: 5px; 
            }
            """)
        self.label_callback.setText(callback_info)

    def read_table(self, column_id):
        ret_dict = {}
        # 获取表格行数
        row_count = self.table.rowCount()
        # 遍历每一行，获取第一列的值
        first_column_values = [self.table.item(row, 0).text() for row in range(row_count)]

        # 打印第一列的值
        for idx, value in enumerate(first_column_values):
            ret_dict[idx] = value
        return ret_dict

    def start_thread(self):
        self.md5_dict = self.read_table(0)
        if not self.md5_dict:
            error_info = "请先导入数据！"
            self.show_message_box(error_info)
            return
        self.btn_start.setEnabled(False)
        self.btn_start.setText("正在运行")

        # 创建一个新的 QThread 对象
        self.thread = QThread()
        # 创建一个 Worker 对象
        self.worker = Worker(self)
        # 将 Worker 对象移动到新线程
        self.worker.moveToThread(self.thread)

        # 连接线程的 started 信号到 Worker 的 run 方法
        self.thread.started.connect(self.worker.run)
        # 连接 Worker 的 finished 信号到线程的 quit 方法
        self.worker.finished.connect(self.thread.quit)
        # 连接 Worker 的 finished 信号到 Worker 对象的 deleteLater 方法
        self.worker.finished.connect(self.worker.deleteLater)
        # 连接线程的 finished 信号到线程的 deleteLater 方法
        self.thread.finished.connect(self.thread.deleteLater)

        # 连接 Worker 的 progress 信号到 update_label 方法
        self.worker.progress.connect(self.report_progress)
        self.worker.callback_info.connect(self.callback)
        self.worker.callback_error.connect(self.show_message_box)
        self.worker.callback_result.connect(self.write_table)
        self.worker.label_md5_id.connect(self.handle_label_md5_id)
        self.worker.label_key_id.connect(self.handle_label_key_id)
        self.worker.finished.connect(self.finished_thread)

        # 启动线程
        self.thread.start()

        # 禁用按钮，直到任务完成
        self.btn_start.setEnabled(False)
        # 任务完成后重新启用按钮
        self.thread.finished.connect(lambda: self.btn_start.setEnabled(True))

    @Slot(int)
    def handle_label_md5_id(self, info):
        self.lcd_md5_id.display(info)

    @Slot(int)
    def handle_label_key_id(self, info):
        self.lcd_key_id.display(info)

    def show_message_box(self, error_info):
        # 创建一个QMessageBox对象
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("警告提示")  # 设置窗口标题
        msg_box.setText(error_info)  # 设置消息文本
        msg_box.setIcon(QMessageBox.Warning)  # 设置图标类型，可以是信息、警告、错误等
        msg_box.setStandardButtons(QMessageBox.Ok)  # 设置标准按钮

        # 显示弹窗并获取用户的响应
        result = msg_box.exec()

        # 处理用户的响应
        # if result == QMessageBox.Ok:
        #     print("用户点击了 OK 按钮")
        # elif result == QMessageBox.Cancel:
        #     print("用户点击了 Cancel 按钮")

    @Slot(int)
    def report_progress(self, n):
        value = (n + 1) / len(self.md5_dict) * 100
        self.progressBar.setValue(int(value))

    @Slot()
    def finished_thread(self):
        self.btn_start.setEnabled(True)
        self.btn_callback_file.setEnabled(True)
        self.btn_start.setText("开始运行")
        self.show_message_box("运行结束，请导出数据！")
        self.callback_info("运行结束，请导出数据！")

    def close_application(self):
        reply = QMessageBox.question(self, '退出确认', '你确定要退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QApplication.quit()


if __name__ == '__main__':

    app = QApplication([])
    window = GuiWindow()
    window.show()
    sys.exit(app.exec())