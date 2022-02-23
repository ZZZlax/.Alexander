def ins():
    import subprocess, os
    subprocess.check_call(['apt', 'install', 'python3-pip', 'python3-tk', 'python3-vlc'], user = "root")
    subprocess.check_call(['pip3', 'install', 'googlesearch-python', 'wikipedia', 'speechrecognition', 'pyttsx3', 'gtts', 'googletrans==4.0.0-rc1'])
    d = input("Create Desktop Item? [y/n]: ")
    r = ["y","Y","Yes","yes","YEs","yES","YES","Ye","YE","ye","Yess","YEss","yess","YESs"]
    if d in r:
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
    dfl = []
    if B in key:
        dfl = B
    else:
        dfl = "zh-tw"

    root = Tk()
    bl = "#000000"
    bu = "#1f9dff"
    wh = "#ffffff"
    gr = "#727272"
    cwd = os.getcwd()
    save1 = cwd+'/.Alex/Images/'
    save2 = cwd+"/.Alex/Alex.mp3"
    btn1 = PhotoImage(file = save1+"Alex.png")
    btn2 = PhotoImage(file = save1+"speak.png")
    btn3 = PhotoImage(file = save1+"record.png")
    btn4 = PhotoImage(file = save1+"wiki.png")
    root.title('Вавилонска кула')
    root.resizable(True, True)
    root.iconphoto(False, btn1)
    menubar = Menu(root, fg=wh, bg=bu)
    root.config(menu=menubar)

    frm = ttk.Frame(root, padding=10).pack()
    style= ttk.Style()
    style.theme_use('alt')
    root['bg']=bl
    style.configure(".", arrowcolor=bu, bordercolor=bu, darkcolor=bl, focusfill=bu, foreground=bu, selectforeground=bu, highlight=bu)
    root.option_add('*TCombobox*Listbox.selectBackground', bu)
    style.configure("TScrollbar", troughcolor=bu)

    def nightmode():
        root['bg']= bl
        file_menu = Menu(menubar, background=bl, activeforeground=gr)
        style.configure(".", background=bl, foreground=wh, fieldbackground=bl)
    def daymode():
        root['bg']= wh
        file_menu = Menu(menubar, background=wh, activeforeground=wh)
        style.configure(".", background=wh, foreground=bu, fieldbackground=wh)
    nightmode()

    def browsefiles():
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        f = filedialog.askopenfile(filetypes=filetypes)
        inputtxt.insert(1.0, f.readlines())
    def savefiles():
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        f.write(inputtxt.get(1.0, "end-1c"))
    def lookup():
        try:
            query = inputtxt.get("sel.first", "sel.last")
        except:
            query = inputtxt.get(1.0,"end-1c")
        inputtxt2.pack(fill="x")
        for j in search(query):
            h = j.split()
            inputtxt2.delete(1.0, "end-1c")
            inputtxt2.insert(1.0, h)
            inputtxt2.focus()
            root.clipboard_clear()
            root.clipboard_append(h)
        webbrowser.open(inputtxt2.get(1.0, "end-1c"), new=2)

    def copy(self):
        try:
            copy = inputtxt.get("sel.first", "sel.last")
        except:
            copy = inputtxt.get(1.0, "end-1c")
        root.clipboard_clear()
        root.clipboard_append(copy)
    def cut(self):
        cut = inputtxt.get("sel.first", "sel.last")
        inputtxt.delete("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(cut)
    def paste(self):
        root.clipboard_get()
    def select_all(self):
        inputtxt.tag_add('sel', '1.0', 'end')
    def exit():
        root.destroy

    tra=Translator()
    fil = tra.translate("File", dfl)
    sav = tra.translate("Save", dfl)
    opn = tra.translate("Open", dfl)
    ext = tra.translate("Exit", dfl)
    File = (fil.text)
    Save = (sav.text)
    Open = (opn.text)
    Exit = (ext.text)
    pre = tra.translate("Prefrences", dfl)
    day = tra.translate("Day Mode", dfl)
    nit = tra.translate("Night Mode", dfl)
    Prefrences = (pre.text)
    DayM = (day.text)
    NightM = (nit.text)
    ser = tra.translate("Search", dfl)
    Sear = (ser.text)
    snr = tra.translate("Speech not recognized", dfl)
    cnf = tra.translate("Could not fetch results", dfl)
    err = tra.translate("Error", dfl)
    sel = tra.translate("Select Language", dfl)
    SNR = (snr.text)
    CNF = (cnf.text)
    Error = (err.text)
    SelectL = (sel.text)

    file_menu = Menu(menubar, background=bl, foreground=bu, activebackground=bu, activeforeground=wh)
    options = Menu(menubar, background=bl, foreground=bu, activebackground=bu, activeforeground=wh)
    se = Menu(root, tearoff = 0, background=bl, foreground=bu, activebackground=bu, activeforeground=wh)
    menubar.add_cascade(label=File, menu= file_menu)
    menubar.add_cascade(label=Prefrences, menu= options)
    file_menu.add_command(label=Save, command= savefiles)
    file_menu.add_command(label=Open, command= browsefiles)
    file_menu.add_command(label=Exit, command= exit)
    options.add_command(label=NightM, command= nightmode)
    options.add_command(label=DayM, command= daymode)
    se.add_command(label = Sear, command = lookup)

    def popup(event):
        try:
            se.tk_popup(event.x_root, event.y_root)
        finally:
            se.grab_release()

    box = ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese Simplified', 'Chinese Traditional', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto',  'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',  'Luxembourgish', 'Macedonian', 'Malay', 'Malayalam', 'Malagasy', 'Maltese', 'Maori', 'Marathi',  'Mongolian',  'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish',  'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']

    languages = {'Arabic':'ar','Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Burmese': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian': 'gt', 'Creole': 'ha', 'Hausa': 'haw', 'Hawaiian': 'iw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malay': 'mg', 'Malayalam': 'ms', 'Malagasy': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}

    spoken = {'Arabic':'ar', 'Pashto':'ar', 'Persian':'ar', 'Punjabi':'ar', 'Sindhi':'ar', 'Somali':'ar', 'Sundanese':'ar', 'Urdu':'ar', 'Uyghur':'ar', 'Azerbaijani':'ru', 'Belarusian':'ru', 'Kazakh':'ru', 'Kyrgyz':'ru', 'Mongolian':'ru', 'Russian':'ru', 'Tajik':'ru', 'Uzbek':'ru', 'Basque':'es', 'Spanish':'es', 'Catalan':'ca', 'Galician':'ca', 'Filipino':'tl', 'Cebuano':'tl', 'Italian':'it', 'Corsican':'it', 'German':'de', 'Frisian':'de', 'Luxembourgish':'de', 'Vietnamese':'vi', 'Hmong':'vi', 'Thai':'th', 'Malay':'th', 'Latin':'la', 'Maltese':'la', 'Latvian':'lv', 'Lithuanian':'lv', 'Javanese':'jw', 'Hawaiian':'jw', 'Samoan':'jw', 'Maori':'jw', 'Slovak':'sk', 'Slovenian':'sk', 'Welsh':'cy', 'Scots Gaelic':'cy', 'Irish':'cy', 'Swahili':'sw', 'Chichewa':'sw', 'Shona':'sw', 'Xhosa':'sw', 'Zulu':'sw', 'Haitian Creole':'fr', 'French':'fr', 'Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'hy', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'Esperanto': 'eo', 'English': 'en', 'Estonian': 'et', 'French': 'fr', 'Finnish': 'fi', 'Greek': 'el', 'Gujarati': 'gu', 'Hindi': 'hi', 'Hungarian': 'hu', 'Icelandic': 'is', 'Indonesian': 'id', 'Japanese': 'ja', 'Kannada': 'kn', 'Khmer': 'km', 'Korean': 'ko', 'Lao': 'lo', 'Macedonian': 'mk', 'Malayalam': 'ml', 'Burmese': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Serbian': 'sr', 'Sinhala': 'si', 'Swedish': 'sv', 'Tamil': 'ta', 'Telugu': 'te', 'Turkish': 'tr', 'Ukrainian': 'uk'}

    combo = ttk.Combobox(frm, values = box)
    combo.set(SelectL)
    combo.pack(fill="x")

    inputtxt = scrolledtext.ScrolledText(root, height=10, width=35, fg=bu, bg=wh, wrap='word', undo="true", foreground=bu, selectbackground=bu)
    inputtxt.focus()
    inputtxt.pack(fill="both", expand='true')
    inputtxt2 = tk.Text(root, height=1, fg=bu, bg=bu, wrap='word', undo="true", foreground=bl, selectforeground=gr, selectbackground= bl)

    def soundcall():
        inputtxt2.pack_forget()
        V = vlc.MediaPlayer(save2)
        V.play()
        inputtxt.tag_add("start", "1.0","end-1c")
        inputtxt.tag_configure("start", foreground=bl)

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
            translation=tra.translate(Y, dest=languages[X])
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
        inputtxt.tag_add("start", "1.0","end-1c")
        inputtxt.tag_configure("start", foreground=bu)
        inputtxt.insert(1.0, speech)
        inputtxt.focus()

    def wiki_search():
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
            sln = Error
            inputtxt.delete(1.0, "end-1c")
            inputtxt.insert(1.0, sln)
            combo.focus()

    inputtxt.bind("<Button-3>", popup)
    root.bind("<Control_L><v>", paste)
    root.bind("<Control_L><x>", cut)
    root.bind("<Control_L><c>", copy)
    root.bind("<Control_L><a>", select_all)

    ttk.Button(image = btn1, command=transcall).pack()
    Button = ttk.Button(image = btn2, command=soundcall)
    ttk.Button(image = btn3, command=speaktext).pack()
    ttk.Button(image= btn4, command=wiki_search).pack()

    root.mainloop()

if __name__ == "__main__":
    try:
        import gtts, googletrans, vlc, pyttsx3, os, os.path, wikipedia, speech_recognition, pprint, webbrowser, locale, sys
        import tkinter as tk
        from tkinter import Tk, PhotoImage, ttk, Menu, filedialog, scrolledtext
        from googletrans import Translator, constants
        from googlesearch import search
        from urllib.request import urlopen
        alexander()
    except:
        ins()
        yn = print("Launch Alexander?: [y/n]")
        res = ['yes', 'YES', 'Yes', 'y', 'Y']
        if yn in res:
            import gtts, vlc, pyttsx3, os, os.path, wikipedia, speech_recognition, pprint, webbrowser, sys, googletrans, locale
            import tkinter as tk
            from tkinter import Tk, PhotoImage, ttk, Menu, filedialog, scrolledtext
            from googletrans import Translator, constants
            from googlesearch import search
            from urllib.request import urlopen
            alexander()
        else:
            pass
