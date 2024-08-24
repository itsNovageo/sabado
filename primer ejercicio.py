meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "TQM": "cuando quieres algo o alguien bastante",
            "MEME": "se refiere a una imagen graciosa",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict)
else:
    print(" no se encontro la palabra")
