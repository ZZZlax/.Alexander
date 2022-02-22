def ins():
    import subprocess, os
    subprocess.check_call(['apt', 'install', 'python3-pip', 'python3-tk', 'python3-vlc'], user = "root")
    subprocess.check_call(['pip3', 'install', 'googlesearch-python', 'wikipedia', 'speechrecognition', 'pyttsx3', 'gtts', 'googletrans==4.0.0-rc1'])
    dsktp = input("Create Desktop Item? [y/n]: ")
    respond = ["y","Y","Yes","yes","YEs","YES"]
    if dsktp in respond:
        cwd = os.getcwd()
        save2 = cwd+"/Desktop"
        F = open(save2+"/Alexander.desktop", 'w')
        Ins = ["[Desktop Entry]", "Type = Application", "Name = Alexander", "Encoding= UTF-8", "Exec = python3 "+cwd+"/.Alex/Alexander.py", "Icon = "+cwd+"/.Alex/Images/Logo.png", "StartupNotify = True"]
        F.writelines("%s\n" % i for i in Ins)
        F.close()
        subprocess.Popen("chmod +x "+cwd+"/Desktop/Alexander.desktop", shell=True, stdout=subprocess.PIPE).stdout.read()
    else:
        pass

def alexander():
    A = (str(locale.getdefaultlocale())).strip("( ) ' ' , _ -")
    B = (A[:2])
    key = ['af', 'sq', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ny', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'gt', 'ha', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
    defaultlang = []
    if B in key:
        defaultlang = B
    else:
        defaultlang = "zh-tw"
    translator=Translator()
    ser = translator.translate("Search", defaultlang)
    sel = translator.translate("Select Language", defaultlang)
    fil = translator.translate("File", defaultlang)
    pre = translator.translate("Prefrences", defaultlang)
    sav = translator.translate("Save", defaultlang)
    opn = translator.translate("Open", defaultlang)
    exi = translator.translate("Exit", defaultlang)
    day = translator.translate("Day Mode", defaultlang)
    nit = translator.translate("Night Mode", defaultlang)
    err = translator.translate("Error", defaultlang)
    snr = translator.translate("Speech not recognized", defaultlang)
    cnf = translator.translate("Could not fetch results", defaultlang)
    SNR = (snr.text)
    CNF = (cnf.text)
    Error = (err.text)
    Sear = (ser.text)
    SelectL = (sel.text)
    File = (fil.text)
    Prefrences = (pre.text)
    Save = (sav.text)
    Open = (opn.text)
    Exit = (exi.text)
    DayM = (day.text)
    NightM = (nit.text)

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
    save1 = cwd+'/.Alex/Images/'
    save2 = cwd+"/.Alex/Alex.mp3"
    def browsefiles():
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        f = filedialog.askopenfile(filetypes=filetypes)
        inputtxt.insert(1.0, f.readlines())
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
    menubar.add_cascade(label=File, menu=file_menu)
    menubar.add_cascade(label=Prefrences, menu=options)
    file_menu.add_command(label=Save, command=savefiles)
    file_menu.add_command(label=Open, command=browsefiles)
    file_menu.add_command(label=Exit, command=root.destroy)
    options.add_command(label=NightM, command=night)
    options.add_command(label=DayM, command=day)

    box = ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese Simplified', 'Chinese Traditional', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto',  'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',  'Luxembourgish', 'Macedonian', 'Malay', 'Malayalam', 'Malagasy', 'Maltese', 'Maori', 'Marathi',  'Mongolian',  'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish',  'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
    languages = {'Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Burmese': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese-Simplified': 'zh-cn', 'Chinese-Traditional': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian': 'gt', 'Creole': 'ha', 'Hausa': 'haw', 'Hawaiian': 'iw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malay': 'mg', 'Malayalam': 'ms', 'Malagasy': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}
    spoken = {'Arabic':'ar', 'Pashto':'ar', 'Persian':'ar', 'Punjabi':'ar', 'Sindhi':'ar', 'Somali':'ar', 'Sundanese':'ar', 'Urdu':'ar', 'Uyghur':'ar', 'Azerbaijani':'ru', 'Belarusian':'ru', 'Kazakh':'ru', 'Kyrgyz':'ru', 'Mongolian':'ru', 'Russian':'ru', 'Tajik':'ru', 'Uzbek':'ru', 'Basque':'es', 'Spanish':'es', 'Catalan':'ca', 'Galician':'ca', 'Filipino':'tl', 'Cebuano':'tl', 'Italian':'it', 'Corsican':'it', 'German':'de', 'Frisian':'de', 'Luxembourgish':'de', 'Vietnamese':'vi', 'Hmong':'vi', 'Thai':'th', 'Malay':'th', 'Latin':'la', 'Maltese':'la', 'Latvian':'lv', 'Lithuanian':'lv', 'Javanese':'jw', 'Hawaiian':'jw', 'Samoan':'jw', 'Maori':'jw', 'Slovak':'sk', 'Slovenian':'sk', 'Welsh':'cy', 'Scots Gaelic':'cy', 'Irish':'cy', 'Swahili':'sw', 'Chichewa':'sw', 'Shona':'sw', 'Xhosa':'sw', 'Zulu':'sw', 'Haitian Creole':'fr', 'French':'fr', 'Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'hy', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'Esperanto': 'eo', 'English': 'en', 'Estonian': 'et', 'French': 'fr', 'Finnish': 'fi', 'Greek': 'el', 'Gujarati': 'gu', 'Hindi': 'hi', 'Hungarian': 'hu', 'Icelandic': 'is', 'Indonesian': 'id', 'Japanese': 'ja', 'Kannada': 'kn', 'Khmer': 'km', 'Korean': 'ko', 'Lao': 'lo', 'Macedonian': 'mk', 'Malayalam': 'ml', 'Burmese': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Serbian': 'sr', 'Sinhala': 'si', 'Swedish': 'sv', 'Tamil': 'ta', 'Telugu': 'te', 'Turkish': 'tr', 'Ukrainian': 'uk'}

    combo = ttk.Combobox(frm, values = box)
    combo.set(SelectL)
    combo.pack(fill="x")

    inputtxt = scrolledtext.ScrolledText(root, height=10, width=35, fg='blue', bg='white', wrap='word', undo="true", foreground='blue', selectforeground='blue')
    inputtxt.focus()
    inputtxt.pack(fill="both", expand='true')
    inputtxt2 = tk.Text(root, height=1, fg='blue', bg='blue', wrap='word', undo="true", foreground='white', selectforeground='blue')

    def soundcall():
        inputtxt2.pack_forget()
        V = vlc.MediaPlayer(save2)
        V.play()
        inputtxt.tag_add("start", "1.0","end-1c")
        inputtxt.tag_configure("start",background="black", foreground= "white")

    def transcall():
        inputtxt2.pack_forget()
        X = combo.get()
        if X == SelectL:
            inputtxt.delete(1.0, "end-1c")
            inputtxt.insert(1.0, SelectL)
            pass
        else:
            Y = inputtxt.get(1.0, "end-1c")
            save3 = cwd+"/.Alex/Alex.mp3"
            translation=translator.translate(Y, dest=languages[X])
            NA = ['Georgian', 'Hausa', 'Hausa', 'Hebrew', 'Igbo', 'Odia', 'Yiddish', 'Yoruba', 'Kurdish', 'Malagasy', 'Marathi', 'Sesotho']
            if X in NA:
                Button.pack_forget()
            else:
                tts = gtts.gTTS((f"{translation.text}"), lang=spoken[X])
                tts.save(save3)
                Button.pack()
            inputtxt.delete(1.0, "end-1c")
            inputtxt.insert(1.0, translation.text)
            inputtxt.focus()

    def speaktext():
        inputtxt2.pack_forget()
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
                speech =(SNR)
            except speech_recognition.RequestError as e:
                speech = (CNF)
        inputtxt.delete(1.0, "end-1c")
        inputtxt.insert(1.0, speech)
        inputtxt.focus()

    def wikisearch():
        inputtxt2.pack_forget()
        try:
            X = combo.get()
            Y = languages[X]
            wikipedia.set_lang(Y)
            try:
                wiki = wikipedia.summary(inputtxt.get(1.0, "end-1c"))
            except:
                wiki = "404"
            inputtxt.delete(1.0, "end-1c")
            inputtxt.insert(1.0, wiki)
            inputtxt.focus()
        except:
            sellang = Error
            inputtxt.delete(1.0, "end-1c")
            inputtxt.insert(1.0, sellang)
            combo.focus()
            pass

    def lookup():
        query = inputtxt.get("sel.first", "sel.last")
        inputtxt2.pack(fill="x")
        for j in search(query):
            h = j.split()
            inputtxt2.delete(1.0, "end-1c")
            inputtxt2.insert(1.0, h)
            inputtxt2.focus()
        webbrowser.open((inputtxt2.get(1.0, "end-1c")), new=2)

    se = Menu(root, tearoff = 0, background='black', foreground='blue', activebackground='blue', activeforeground='white')
    se.add_command(label = Sear, command = lookup)

    def popup(event):
        try:
            se.tk_popup(event.x_root, event.y_root)
        finally:
            se.grab_release()
    inputtxt.bind("<Button-3>", popup)

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
    try:
        import gtts, googletrans, vlc, pyttsx3, os, os.path, wikipedia, speech_recognition, pprint, webbrowser, locale
        import tkinter as tk
        from tkinter import Tk, PhotoImage, ttk, Menu, filedialog, scrolledtext
        from googletrans import Translator, constants
        from googlesearch import search
        from urllib.request import urlopen
        alexander()
    except:
        ins()
        import gtts, googletrans, vlc, pyttsx3, os, os.path, wikipedia, speech_recognition, pprint, webbrowser, locale
        import tkinter as tk
        from tkinter import Tk, PhotoImage, ttk, Menu, filedialog, scrolledtext
        from googletrans import Translator, constants
        from googlesearch import search
        from urllib.request import urlopen
        alexander()
