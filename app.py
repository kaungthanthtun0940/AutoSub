from PySide6 import QtWidgets
from design import Ui_MainWindow
from PySide6.QtWidgets import QFileDialog
from languageData import getKeyList
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip
from audioToText import getAudioToText
import os
from secondToHourMinuteSecond import getHourMinuteSecond
from writeFile import getWriteFile
from languageData import getLanguageData
from translateText import getTranslateText

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Add any additional code for your main window here
        self.pushButton.clicked.connect(self.open_folder)
        self.pushButton_2.clicked.connect(self.open_file)

    def open_file(self):
        global file_path
        file_path, _ = QFileDialog.getOpenFileName(None, "Open video file", "", "Video Files (*.mp4 *.avi *.mkv *.wmv)")
        input_lang = self.lineEdit.text()
        output_lang = self.lineEdit_2.text()
        folder_path = self.lineEdit_3.text()
        if file_path and input_lang and output_lang and folder_path:
            lang_list = getKeyList()
            input_lang = input_lang.lower()
            output_lang = output_lang.lower()
            if input_lang in lang_list:
                if output_lang in lang_list:
                    try:
                        print(file_path)
                        print(input_lang)
                        print(output_lang)
                        print(folder_path)
                        path1 = folder_path
                        path2 = "running"

                        full_path = os.path.join(path1, path2)
                        print(full_path)
                        try:
                            os.makedirs(full_path)
                            self.label.setText("Progressing")
                            self.progressBar.setValue(2)

                        except OSError:
                            print("Creation of the directory %s failed" % full_path)
                        else:
                            print("Successfully created the directory %s " % full_path)

                        video = VideoFileClip(file_path)

                        get_input_lang = getLanguageData(input_lang)
                        get_output_lang = getLanguageData(output_lang)
                        print(get_input_lang)
                        print(get_output_lang)

                        duration = video.duration

                        print("The duration of the video is:", duration, "seconds")
                        startList = []
                        endList = []
                        count = 0
                        while count < duration - 5:
                            startList.append(count)
                            count = count + 5
                            endList.append(count)

                        last = duration % 5

                        last_end_list_item = startList[-1] + 5
                        startList.append(last_end_list_item)
                        endList.append(duration)

                        print(startList)
                        print(endList)

                        list_len = len(startList)



                        for m in range(list_len):
                            startTime = startList[m]
                            endTime = endList[m]
                            print(startTime)
                            print(endTime)

                            num_to_divided = m + 1
                            divided = list_len / num_to_divided
                            percent = 98 / divided

                            self.progressBar.setValue(percent)


                            subClip = video.subclip(startTime, endTime)
                            audio = subClip.audio
                            audio.write_audiofile(os.path.join(folder_path, "running", f"{m}.wav"))
                            path = os.path.join(folder_path, "running", f"{m}.wav")
                            speech_text = getAudioToText(path, get_input_lang)
                            print(get_input_lang)
                            print(get_output_lang)
                            tran_text = getTranslateText(speech_text, get_input_lang, get_output_lang)
                            if tran_text:
                                start_vtt_time = getHourMinuteSecond(startTime)
                                end_vtt_time = getHourMinuteSecond(endTime)
                                video_name = os.path.splitext(os.path.basename(file_path))[0]
                                vtt_file_path = os.path.join(folder_path, f"{video_name}.vtt")
                                getWriteFile(vtt_file_path, tran_text, start_vtt_time, end_vtt_time)

                        video.close()

                        path = os.path.join(folder_path, "running")

                        folder_path = path
                        if os.path.exists(folder_path):
                            try:
                                shutil.rmtree(folder_path)
                                print(f"{folder_path} and its contents have been deleted.")
                                self.label.setText("Complete")
                                self.progressBar.setValue(100)
                            except OSError as e:
                                print(f"Error: {folder_path} and its contents could not be deleted - {e}")
                        else:
                            print(f"{folder_path} does not exist.")
                    except:
                        self.label.setText("Please Try Again")
                else:
                    self.label.setText("Check The Output Language")
            else:
                self.label.setText("Check The Input Language")
        else:
            self.label.setText("Please Check The All Input")
    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select a folder")
        if folder_path:
            self.lineEdit_3.setText(folder_path)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
