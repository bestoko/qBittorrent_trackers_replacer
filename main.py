import sys
from PyQt5.QtWidgets import *
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('qBittorrent trackers replacer')

        bt_backup_path_label = QLabel('BT Backup path:')
        old_tracker_label = QLabel('old tracker:')
        new_tracker_label = QLabel('new tracker:')
        confirm_btn = QPushButton('Confirm')
        bt_backup_path_line = QLineEdit()
        old_tracker_line = QLineEdit()
        new_tracker_line = QLineEdit()


        f_layout = QFormLayout()
        f_layout.addRow(bt_backup_path_label, bt_backup_path_line)
        f_layout.addRow(old_tracker_label, old_tracker_line)
        f_layout.addRow(new_tracker_label, new_tracker_line)
        f_layout.addRow(confirm_btn)
        self.setLayout(f_layout)

        confirm_btn.clicked.connect(lambda: confirm_btn.setText('Confirmed'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())