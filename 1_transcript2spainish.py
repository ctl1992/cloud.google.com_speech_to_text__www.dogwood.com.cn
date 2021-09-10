import pandas
transcriptCsv = pandas.read_csv("transcripts_spainishABCDEFGHIJKLMNOPQRSTUVWXZ.mp3-20210909020937.csv")
spainish = transcriptCsv[['results/alternatives/0/transcript']]
spainish.to_excel("spainish.xls", index=False)
pass