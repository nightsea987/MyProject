from PyQt5.QtWidgets import QWidget, QApplication, QAction
import sys
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl
from MyProject.design.ringtons_design import Ui_Form


class GetRington(QWidget, Ui_Form):

    def __init__(self, path):
        super().__init__()
        self.setupUi(self)
        self.path = path
        self.set_rington_settings.clicked.connect(self.get_rington)
        self.melody_paths = {self.melodies_lst[0]: 'other_files/melody1.mp3',
                             self.melodies_lst[1]: 'other_files/melody2.mp3',
                             self.melodies_lst[2]: 'other_files/melody3.mp3',
                             self.melodies_lst[3]: 'other_files/melody4.mp3',
                             self.melodies_lst[4]: 'other_files/melody5.mp3'}

        quit = QAction(self)
        quit.triggered.connect(self.closeEvent)
        self.player = QMediaPlayer()

        for i in range(5):
            if self.melody_paths[self.melodies_lst[i]] == path:
                self.melodies_lst[i].setChecked(True)

        for i in range(5):
            self.melodies_lst[i].clicked.connect(self.play_melody)

    def play_melody(self):
        for i in range(5):
            if self.melodies_lst[i].isChecked():
                self.current_path = self.melody_paths[self.melodies_lst[i]]
        self.player.setMedia(QMediaContent(QUrl(self.current_path)))
        self.player.play()

    def get_rington(self):
        self.result_path = ''
        for i in range(len(self.melodies_lst)):
            if self.melodies_lst[i].isChecked():
                self.result_path = self.melody_paths[self.melodies_lst[i]]
        self.closeEvent()
        return self.result_path

    def closeEvent(self, a0=None):
        self.close()
        self.player.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = GetRington()
    form.show()
    sys.exit(app.exec())
