import easyocr

# All the languages supported by EasyOCR (I will be adding custom language selection by the user later)

languages = {'Abaza': 'abq', 'Adyghe': 'ady', 'Afrikaans': 'af', 'Angika': 'ang', 'Arabic': 'ar', 'Assamese': 'as', 'Avar': 'ava', 'Azerbaijani': 'az', 'Belarusian': 'be', 'Bulgarian': 'bg', 'Bihari': 'bh', 'Bhojpuri': 'bho', 'Bengali': 'bn', 'Bosnian': 'bs', 'Simplified Chinese': 'ch_sim', 'Traditional Chinese': 'ch_tra', 'Chechen': 'che', 'Czech': 'cs', 'Welsh': 'cy', 'Danish': 'da', 'Dargwa': 'dar', 'German': 'de', 'English': 'en', 'Spanish': 'es', 'Estonian': 'et', 'Persian (Farsi)': 'fa', 'French': 'fr', 'Irish': 'ga', 'Goan Konkani': 'gom', 'Hindi': 'hi', 'Croatian': 'hr', 'Hungarian': 'hu', 'Indonesian': 'id', 'Ingush': 'inh', 'Icelandic': 'is', 'Italian': 'it', 'Japanese': 'ja', 'Kabardian': 'kbd', 'Kannada': 'kn', 'Korean': 'ko', 'Kurdish': 'ku', 'Latin': 'la', 'Lak': 'lbe', 'Lezghian': 'lez', 'Lithuanian': 'lt', 'Latvian': 'lv', 'Magahi': 'mah', 'Maithili': 'mai', 'Maori': 'mi', 'Mongolian': 'mn', 'Marathi': 'mr', 'Malay': 'ms', 'Maltese': 'mt', 'Nepali': 'ne', 'Newari': 'new', 'Dutch': 'nl', 'Norwegian': 'no', 'Occitan': 'oc', 'Pali': 'pi', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru', 'Serbian (cyrillic)': 'rs_cyrillic', 'Serbian (latin)': 'rs_latin', 'Nagpuri': 'sck', 'Slovak': 'sk', 'Slovenian': 'sl', 'Albanian': 'sq', 'Swedish': 'sv', 'Swahili': 'sw', 'Tamil': 'ta', 'Tabassaran': 'tab', 'Telugu': 'te', 'Thai': 'th', 'Tajik': 'tjk', 'Tagalog': 'tl', 'Turkish': 'tr', 'Uyghur': 'ug', 'Ukranian': 'uk', 'Urdu': 'ur', 'Uzbek': 'uz', 'Vietnamese': 'vi'}

# Initializes the EasyOCR reader
reader = easyocr.Reader(["en"], gpu=True)
# Uses the gpu instead of the cpu for faster execution. You May set it to False

def ocr(image_location):
    text = reader.readtext(image_location, detail=0)
    return text