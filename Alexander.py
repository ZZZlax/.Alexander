def alexander():
    import gtts, googletrans, vlc, pyttsx3, os, os.path, wikipedia, speech_recognition, pprint
    import tkinter as tk
    from tkinter import Tk, PhotoImage, ttk, Menu, filedialog, scrolledtext
    from googletrans import Translator, constants

    translator=Translator()
    root = Tk()
    menubar = Menu(root, fg='white', bg='blue')
    root.title('Вавилонска кула')
    root.config(menu=menubar)
    root.resizable(True, True)
    frm = ttk.Frame(root, padding=10).pack()

    style= ttk.Style()
    style.theme_use('alt')
    root['bg']='black'
    style.configure("TCombobox", arrowcolor='blue', background='black', bordercolor='blue', darkcolor='black', focusfill='blue', foreground='white', fieldbackground='black', selectforeground='blue')
    style.configure("TButton", arrowcolor='blue', background='black', bordercolor='blue', darkcolor='black', focusfill='blue', foreground='white', fieldbackground='black', selectforeground='blue')
    style.configure("TFrame", arrowcolor='blue', background='black', bordercolor='blue', darkcolor='black', focusfill='blue', foreground='blue', fieldbackground='black', selectforeground='blue')
    style.configure("TScrollbar", arrowcolor='blue', background='black', bordercolor='blue', darkcolor='black', focusfill='blue', foreground='blue', fieldbackground='black', selectforeground='blue', highlight='blue')
    style.configure("TLabel", arrowcolor='blue', background='black', bordercolor='blue', darkcolor='black', focusfill='blue', foreground='blue', fieldbackground='black', selectforeground='blue', highlight='blue')
    root.option_add('*TCombobox*Listbox.selectBackground', 'blue')
    root.option_add('*TCombobox*Listbox.selectForeground', 'white')
    style.configure("TScrollbar", troughcolor="blue")

    cwd = os.getcwd()
    save1 = cwd+'/Alex/Images/'
    save2 = cwd+"/Alex/Alex.mp3"

    def browsefiles():
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        f = filedialog.askopenfile(filetypes=filetypes)
        inputtxt.insert('1.0', f.readlines())
    def savefiles():
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        f.write(inputtxt.get(1.0, "end-1c"))

    def night():
        style= ttk.Style()
        style.theme_use('alt')
        root['bg']='black'
        file_menu = Menu(menubar, background='black', activeforeground='black')
        style.configure("TCombobox", background='black', foreground='white', fieldbackground='black')
        style.configure("TButton", background='black', foreground='white', fieldbackground='black')
        style.configure("TFrame", background='black', fieldbackground='black')
        style.configure("TScrollbar", background='black', fieldbackground='black')
        style.configure("TLabel", background='black', fieldbackground='black')
        root.option_add('*TCombobox*Listbox.selectBackground', 'blue')
        root.option_add('*TCombobox*Listbox.selectForeground', 'black')
    def day():
        style= ttk.Style()
        style.theme_use('alt')
        root['bg']='white'
        menubar = Menu(root, fg='white', bg='blue')
        file_menu = Menu(menubar, background='white', activeforeground='white')
        style.configure("TCombobox", background='white', foreground='blue', fieldbackground='white')
        style.configure("TButton", background='white', foreground='blue', fieldbackground='white')
        style.configure("TFrame", background='white', fieldbackground='white')
        style.configure("TScrollbar", background='white', fieldbackground='white')
        style.configure("TLabel", background='white', fieldbackground='white')
        root.option_add('*TCombobox*Listbox.selectBackground', 'blue')
        root.option_add('*TCombobox*Listbox.selectForeground', 'white')

    file_menu = Menu(menubar, background='black', foreground='blue', activebackground='blue', activeforeground='white')
    options = Menu(menubar, background='black', foreground='blue', activebackground='blue', activeforeground='white')
    menubar.add_cascade(label="File", menu=file_menu)
    menubar.add_cascade(label="Prefrences", menu=options)
    file_menu.add_command(label='Save', command=savefiles)
    file_menu.add_command(label='Open', command=browsefiles)
    file_menu.add_command(label='Exit', command=root.destroy)
    options.add_command(label='Night Mode', command=night)
    options.add_command(label='Day Mode', command=day)

    box = ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese Simplified', 'Chinese Traditional', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto',  'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',  'Luxembourgish', 'Macedonian', 'Malay', 'Malayalam', 'Malagasy', 'Maltese', 'Maori', 'Marathi',  'Mongolian',  'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish',  'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
    combo = ttk.Combobox(frm, values = box)
    combo.set("Select Language")
    combo.pack(fill="x")

    inputtxt = scrolledtext.ScrolledText(root, height=10, width=35, fg='blue', bg='white', wrap='word', undo="true", foreground='blue', selectforeground='blue')
    inputtxt.focus()
    inputtxt.pack(fill="both", expand='true')

    Buttonvar = []

    def soundcall():
        V = vlc.MediaPlayer(save2)
        V.play()

    def transcall():
        X = combo.get()
        Y = inputtxt.get(1.0, "end-1c")
        save3 = cwd+"/Alex/Alex.mp3"
        Buttonvar = True
        if X == 'Georgian' or X == 'Hausa' or X == 'Hausa' or X == 'Hebrew' or X == 'Igbo' or X == 'Odia' or X == 'Yiddish' or X == 'Yoruba' or X == 'Kurdish' or X == 'Malagasy' or X == 'Marathi' or X == 'Sesotho':
            NA = {'Georgian': 'ka', 'Hausa': 'ha', 'Hebrew': 'he', 'Igbo': 'ig', 'Odia': 'or', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Kurdish': 'ku', 'Malagasy' : 'mg', 'Marathi' : 'mr', 'Sesotho' : 'st'}
            translation=translator.translate(Y, dest=NA[X])
            Buttonvar = False
        elif X == 'Arabic' or X == 'Pashto' or X == 'Persian' or X == 'Punjabi' or X == 'Sindhi' or X == 'Somali' or X == 'Sundanese'  or X == 'Urdu' or X == 'Uyghur':
            AR = {'Arabic': 'ar', 'Pashto': 'ps', 'Persian': 'fa', 'Punjabi': 'pa', 'Sindhi': 'sd', 'Somali': 'so', 'Sundanese': 'su', 'Urdu': 'ur', 'Uyghur': 'ug'}
            translation=translator.translate(Y, dest=AR[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='ar')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Azerbaijani' or X == 'Belarusian' or X == 'Kazakh' or X == 'Kyrgyz' or X == 'Mongolian' or X == 'Russian' or X ==   'Tajik' or X == 'Uzbek':
            RU = {'Azerbaijani': 'az', 'Belarusian': 'be', 'Kazakh': 'kk', 'Kyrgyz': 'ky', 'Mongolian': 'mn', 'Russian': 'ru', 'Tajik': 'tg', 'Uzbek': 'uz'}
            translation=translator.translate(Y, dest=RU[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='ru')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Basque' or X == 'Spanish':
            ES = {'Basque': 'eu', 'Spanish': 'es'}
            translation=translator.translate(Y, dest=ES[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='es')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Catalan' or X == 'Galician':
            CA = {'Catalan': 'ca', 'Galician': 'gl'}
            translation=translator.translate(Y, dest=CA[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='ca')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Filipino' or X == 'Cebuano':
            TL = {'Filipino': 'tl', 'Cebuano': 'ceb'}
            translation=translator.translate(Y, dest=TL[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='tl')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Italian' or X == 'Corsican':
            IT = {'Italian': 'it', 'Corsican': 'co'}
            translation=translator.translate(Y, dest=IT[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='it')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'German' or X == 'Frisian' or X == 'Luxembourgish':
            DE = {'German': 'de', 'Frisian': 'fy', 'Luxembourgish': 'lb'}
            translation=translator.translate(Y, dest=DE[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='de')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Vietnamese' or X == 'Hmong':
            VI = {'Vietnamese': 'vi', 'Hmong': 'hmn'}
            translation=translator.translate(Y, dest=VI[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='vi')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Thai' or X == 'Malay':
            TH = {'Thai': 'th', 'Malay': 'ms'}
            translation=translator.translate(Y, dest=TH[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='th')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Latin' or X == 'Maltese':
            LA = {'Latin': 'la', 'Maltese': 'mt'}
            translation=translator.translate(Y, dest=LA[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='la')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Latvian' or X == 'Lithuanian':
            LV = {'Latvian': 'lv', 'Lithuanian': 'lt'}
            translation=translator.translate(Y, dest=LV[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='lv')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Javanese' or X == 'Hawaiian' or X == 'Samoan' or X == 'Maori':
            JW = {'Javanese': 'jw', 'Hawaiian': 'haw', 'Samoan': 'sm', 'Maori': 'mi'}
            translation=translator.translate(Y, dest=JW[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='jw')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Slovak' or X == 'Slovenian':
            SK = {'Slovak': 'sk', 'Slovenian': 'sl'}
            translation=translator.translate(Y, dest=SK[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='sk')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Welsh' or X == 'Scots Gaelic' or X == 'Irish':
            CY = {'Welsh': 'cy', 'Scots Gaelic': 'gd', 'Irish': 'ga'}
            translation=translator.translate(Y, dest=CY[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='cy')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Swahili' or X == 'Chichewa' or X == 'Shona' or X == 'Xhosa' or X == 'Zulu':
            SW = {'Swahili': 'ny', 'Chichewa': 'sw', 'Shona': 'sn', 'Xhosa': 'xh', 'Zulu': 'zu'}
            translation=translator.translate(Y, dest=SW[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='sw')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        elif X == 'Haitian Creole' or X == 'French':
            SK = {'French': 'fr', 'Haitian Creole': 'ht'}
            translation=translator.translate(Y, dest=SK[X])
            tts = gtts.gTTS((f"{translation.text}"), lang='fr')
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        else:
            ISO = {'Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'hy', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'Esperanto': 'eo', 'English': 'en', 'Estonian': 'et', 'French': 'fr', 'Finnish': 'fi', 'Greek': 'el', 'Gujarati': 'gu', 'Hindi': 'hi', 'Hungarian': 'hu', 'Icelandic': 'is', 'Indonesian': 'id', 'Japanese': 'ja', 'Kannada': 'kn', 'Khmer': 'km', 'Korean': 'ko', 'Lao': 'lo', 'Macedonian': 'mk', 'Malayalam': 'ml', 'Burmese': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Serbian': 'sr', 'Sinhala': 'si', 'Swedish': 'sv', 'Tamil': 'ta', 'Telugu': 'te', 'Turkish': 'tr', 'Ukrainian': 'uk'}
            translation=translator.translate(Y, dest=ISO[X])
            tts = gtts.gTTS((f"{translation.text}"), lang=ISO[X])
            tts.save(save3)
            V = vlc.MediaPlayer(save3)
        if X == 'Georgian' or X == 'Hausa' or X == 'Hausa' or X == 'Hebrew' or X == 'Igbo' or X == 'Odia' or X == 'Yiddish' or X == 'Yoruba' or X == 'Kurdish' or X == 'Malagasy' or X == 'Marathi' or X == 'Sesotho':
            Button.pack_forget()
        else:
            Button.pack()
        inputtxt.delete(1.0, "end-1c")
        inputtxt.insert('1.0', translation.text)

    def speaktext():
        engine = pyttsx3.init('espeak')
        engine.runAndWait()
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            r.adjust_for_ambient_noise(source, 2)
            audio = r.listen(source)
            try:
                speech = r.recognize_google(audio)
                engine.say(speech)
            except speech_recognition.UnknownValueError:
                speech =("Speech not recognized")
            except speech_recognition.RequestError as e:
                speech = ("Could not fetch results")
        inputtxt.delete(1.0, "end-1c")
        inputtxt.insert('1.0', speech)

    def wikisearch():
        languages = {'Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'ar', 'Azerbaijani': 'hy', 'Basque': 'az', 'Belarusian': 'eu', 'Bengali': 'be', 'Bosnian': 'bn', 'Bulgarian': 'bs', 'Burmese': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese-Simplified': 'zh-cn', 'Chinese-Traditional': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian': 'gt', 'Creole': 'ha', 'Hausa': 'haw', 'Hawaiian': 'iw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malay': 'mg', 'Malayalam': 'ms', 'Malagasy': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Nepali': 'my', 'Norwegian': 'ne', 'Odia': 'no', 'Pashto': 'or', 'Persian': 'ps', 'Polish': 'fa', 'Portuguese': 'pl', 'Punjabi': 'pt', 'Romanian': 'pa', 'Russian': 'ro', 'Samoan': 'ru', 'Scots': 'sm', 'Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}
        X = combo.get()
        Y = languages[X]
        wikipedia.set_lang(Y)
        try:
            wiki = wikipedia.summary(inputtxt.get(1.0, "end-1c"))
        except:
            wiki = "404"
        inputtxt.delete(1.0, "end-1c")
        inputtxt.insert('1.0', wiki)

    btn1 = PhotoImage(file = save1+"Alex.png")
    btn2 = PhotoImage(file = save1+"speak.png")
    btn3 = PhotoImage(file = save1+"record.png")
    btn4 = PhotoImage(file = save1+"wiki.png")
    ttk.Button(image = btn1, command=transcall).pack()
    Button = ttk.Button(image = btn2, command=soundcall)
    ttk.Button(image = btn3, command=speaktext).pack()
    ttk.Button(image= btn4, command=wikisearch).pack()

    root.mainloop()

if __name__ == "__main__":
    alexander()