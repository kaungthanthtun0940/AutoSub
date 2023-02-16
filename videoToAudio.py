from moviepy.video.io.VideoFileClip import VideoFileClip
from audioToText import getAudioToText
import os
from secondToHourMinuteSecond import getHourMinuteSecond
from writeFile import getWriteFile
from languageData import getLanguageData
from translateText import getTranslateText

def getVideoToAudio(filePath,folderPath,input_lang,output_lang):

    video = VideoFileClip(filePath)

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
        subClip = video.subclip(startTime, endTime)
        audio = subClip.audio
        audio.write_audiofile(os.path.join(folderPath,"running", f"{m}.wav"))
        path = os.path.join(folderPath,"running", f"{m}.wav")
        speech_text = getAudioToText(path,get_input_lang)
        print(get_input_lang)
        print(get_output_lang)
        tran_text = getTranslateText(speech_text,get_input_lang,get_output_lang)
        start_vtt_time = getHourMinuteSecond(startTime)
        end_vtt_time = getHourMinuteSecond(endTime)
        video_name = os.path.splitext(os.path.basename(filePath))[0]
        vtt_file_path = os.path.join(folderPath,f"{video_name}.vtt")
        getWriteFile(vtt_file_path, tran_text, start_vtt_time, end_vtt_time)


    video.close()

