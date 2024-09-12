import sys
from PySide6.QtWidgets import QApplication
from gui import GuiWindow  # 导入 MyWidget 类


class WeibuApi:
    def __init__(self):
        self.app = QApplication(sys.argv)
        # 创建 MyWidget 实例
        self.widget = GuiWindow()
        self.widget.show()

    def run(self):
        try:
            sys.exit(self.app.exec())
        except Exception as e:
            self.widget.show_message_box(e)


if __name__ == "__main__":
    app_instance = WeibuApi()
    app_instance.run()
