import re
from time import sleep

from num2words import num2words
import pandas
from gtts import gTTS
import os
spainish_xls = pandas.read_excel("spainish.xls")
chinese_spainish_xls = pandas.DataFrame(columns=['index_spainish', 'chinese', 'spainish'])
if os.path.exists("chinese_spainish.xls"):
  os.remove("chinese_spainish.xls")
for index, row in spainish_xls.iterrows():
    index_chinese = str(index+1)
    index_spainish = num2words(index+1, lang='es')
    chinese = row['西班牙文']
    spainish = row['spainish']
    print(index, index_spainish, chinese, spainish)
    chinese_spainish_xls = chinese_spainish_xls.append({
                          'index_spainish':index_spainish,
                          'chinese':chinese,
                          'spainish':spainish},
                         ignore_index=True)
    # try:
    #     gTTS(str(index) + "...", lang="zh-TW").write_to_fp(f)  # a1mp3 1
    #     sleep(2)
    #     gTTS(str(index) + "...", lang="es").write_to_fp(f)
    #     sleep(2)
    #     gTTS(chinese + "...", lang="zh-TW").write_to_fp(f)  # 中文
    #     sleep(2)
    #     gTTS(spainish + "...", lang="es").write_to_fp(f) # 西班牙文
    #     sleep(2)
    # except:
    #     pass
chinese_spainish_xls.to_excel("chinese_spainish.xls", index=False) #, header=False
pass