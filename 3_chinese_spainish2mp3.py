import re
from time import sleep

from num2words import num2words
import pandas
from gtts import gTTS
import os
chinese_spainish_xls = pandas.read_excel("chinese_spainish.xls")
# chinese_spainish = pandas.DataFrame(columns=['index_spainish', 'chinese', 'spainish'])
start_index = 2
end_index = 1238
if os.path.exists("spainish_1_1238.mp3"):
  os.remove("spainish_1_1238.mp3")
with open('spainish_1_1238.mp3', 'wb') as f:
    for index, row in chinese_spainish_xls.iterrows():
        if index >= start_index-2 and index <= end_index-2:
            index_chinese = str(index+2)
            index_spainish = str(row[0])
            chinese = str(row[1])
            spainish = str(row[2])
            print(index_chinese, index_spainish, chinese, spainish)
            # chinese_spainish = chinese_spainish.append({
            #                       'index_spainish':index_spainish,
            #                       'chinese':chinese,
            #                       'spainish':spainish},
            #                      ignore_index=True)
            try:
                gTTS(index_chinese + "...", lang="zh-TW").write_to_fp(f)  # a1mp3 1
                sleep(2)
                gTTS(index_spainish + "...", lang="es").write_to_fp(f)
                sleep(2)
                gTTS(chinese + "...", lang="zh-TW").write_to_fp(f)  # 中文
                sleep(2)
                gTTS(spainish + "...", lang="es").write_to_fp(f) # 西班牙文
                sleep(2)
            except:
                pass
    # chinese_spainish.to_excel("chinese_spainish.xls", index=False, header=False)
pass