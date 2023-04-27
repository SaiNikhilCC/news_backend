from googletrans import Translator

translator = Translator()
data = translator.translate('යුනිකෝඩ් ', dest='ec', src='si').text()


print(data)