def alexander():

    ## determine default language by extracting first two letters from os language setting.
    ## issues: unable to resolve languages beyond 2 characters therefore excluding Cebuano: ceb, Chinese Traditional: zh-tw, or Chinese Simplified: zh-cn and Hmong: hmn

    A = str(locale.getdefaultlocale()).strip("( ) ' ' , _ -")[:2]
    key = {'af', 'sq', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ny', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'gt', 'ha', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'}
    dfl = []
    if A in key:
        dfl = A
    else:
        dfl = "zh-tw"

    ## initialize window and declare saves

    root = Tk()
    bl = "#000000"
    bu = "#1f9dff"
    wh = "#ffffff"
    gr = "#727272"

    cwd = os.getcwd()
    save1 = cwd+'/.Alex/Images/'
    btn1 = PhotoImage(file = save1+"Alex.png")
    btn2 = PhotoImage(file = save1+"speak.png")
    btn3 = PhotoImage(file = save1+"record.png")
    btn4 = PhotoImage(file = save1+"wiki.png")
    tempmp3file = tempfile.mktemp('.mp3')

    ## styling

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

    ## and defining night_mode and day_mode

    def night_mode():
        root['bg']= bl
        style.configure(".", background=bl, foreground=wh, fieldbackground=bl)

    def day_mode():
        root['bg']= wh
        style.configure(".", background=wh, foreground=bu, fieldbackground=wh)

    night_mode()

    ## setting up menu definitions

    def browse_files():
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        f = filedialog.askopenfile(filetypes=filetypes)
        input_text.insert(1.0, f.readlines())

    def save_files():
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        f.write(input_text.get(1.0, "end-1c"))

    def google_it():
        try:
            query = input_text.get("sel.first", "sel.last")
        except:
            query = input_text.get(1.0,"end-1c")
        input_text2.pack(fill="x")
        for j in search(query):
            h = j.split()
            input_text2.delete(1.0, "end-1c")
            input_text2.insert(1.0, h)
            input_text2.focus()
            root.clipboard_clear()
            root.clipboard_append(h)
        webbrowser.open(inputtxt2.get(1.0, "end-1c"), new=2)

    def copy(self):
        try:
            copy = input_text.get("sel.first", "sel.last")
        except:
            copy = input_text.get(1.0, "end-1c")
        root.clipboard_clear()
        root.clipboard_append(copy)

    def cut(self):
        cut = input_text.get("sel.first", "sel.last")
        input_text.delete("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(cut)

    def paste(self):
        root.clipboard_get()

    def select_all(self):
        input_text.tag_add('sel', '1.0', 'end')

    def exit():
        root.destroy

    ## localizing text
    ## issues: I haven't figured out a way to localize the values in box besides unquoting entries and translating them here, which severely increases read time.

    translator=Translator()
    fil = translator.translate("File", dfl)
    sav = translator.translate("Save", dfl)
    opn = translator.translate("Open", dfl)
    ext = translator.translate("Exit", dfl)
    File = (fil.text)
    Save = (sav.text)
    Open = (opn.text)
    Exit = (ext.text)

    pre = translator.translate("Prefrences", dfl)
    day = translator.translate("Day Mode", dfl)
    nit = translator.translate("Night Mode", dfl)
    Prefrences = (pre.text)
    DayM = (day.text)
    NightM = (nit.text)

    ser = translator.translate("Search", dfl)
    Search = (ser.text)

    snr = translator.translate("Speech not recognized", dfl)
    cnf = translator.translate("Could not fetch results", dfl)
    err = translator.translate("Error", dfl)
    sel = translator.translate("Select Language", dfl)
    SNR = (snr.text)
    CNF = (cnf.text)
    Error = (err.text)
    SelectL = (sel.text)

    ## setting up menu

    file_menu = Menu(menubar, background=bl, foreground=bu, activebackground=bu, activeforeground=wh)
    options = Menu(menubar, background=bl, foreground=bu, activebackground=bu, activeforeground=wh)
    se = Menu(root, tearoff = 0, background=bl, foreground=bu, activebackground=bu, activeforeground=wh)
    menubar.add_cascade(label=File, menu= file_menu)
    menubar.add_cascade(label=Prefrences, menu= options)
    file_menu.add_command(label=Save, command= save_files)
    file_menu.add_command(label=Open, command= browse_files)
    file_menu.add_command(label=Exit, command= exit)
    options.add_command(label=NightM, command= night_mode)
    options.add_command(label=DayM, command= day_mode)
    se.add_command(label = Search, command = google_it)

    def popup_menu(event):
        try:
            se.tk_popup(event.x_root, event.y_root)
        finally:
            se.grab_release()

    ## values for combobox (box), language keys for googletrans (languages) and gtts (spoken)

    box = (['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Burmese', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese Simplified', 'Chinese Traditional', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Esperanto',  'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',  'Luxembourgish', 'Macedonian', 'Malay', 'Malayalam', 'Malagasy', 'Maltese', 'Maori', 'Marathi',  'Mongolian',  'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian', 'Polish',  'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese', 'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu'])

    languages = {'Arabic':'ar','Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'hy', 'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Burmese': 'bg', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw', 'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian': 'gt', 'Creole': 'ha', 'Hausa': 'haw', 'Hawaiian': 'iw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malay': 'mg', 'Malayalam': 'ms', 'Malagasy': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}

    spoken = {'Arabic':'ar', 'Pashto':'ar', 'Persian':'ar', 'Punjabi':'ar', 'Sindhi':'ar', 'Somali':'ar', 'Sundanese':'ar', 'Urdu':'ar', 'Uyghur':'ar', 'Azerbaijani':'ru', 'Belarusian':'ru', 'Kazakh':'ru', 'Kyrgyz':'ru', 'Mongolian':'ru', 'Russian':'ru', 'Tajik':'ru', 'Uzbek':'ru', 'Basque':'es', 'Spanish':'es', 'Catalan':'ca', 'Galician':'ca', 'Filipino':'tl', 'Cebuano':'tl', 'Italian':'it', 'Corsican':'it', 'German':'de', 'Frisian':'de', 'Luxembourgish':'de', 'Vietnamese':'vi', 'Hmong':'vi', 'Thai':'th', 'Malay':'th', 'Latin':'la', 'Maltese':'la', 'Latvian':'lv', 'Lithuanian':'lv', 'Javanese':'jw', 'Hawaiian':'jw', 'Samoan':'jw', 'Maori':'jw', 'Slovak':'sk', 'Slovenian':'sk', 'Welsh':'cy', 'Scots Gaelic':'cy', 'Irish':'cy', 'Swahili':'sw', 'Chichewa':'sw', 'Shona':'sw', 'Xhosa':'sw', 'Zulu':'sw', 'Haitian Creole':'fr', 'French':'fr', 'Afrikaans': 'af', 'Albanian': 'sq', 'Armenian': 'hy', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Chinese Simplified': 'zh-cn', 'Chinese Traditional': 'zh-tw', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'Esperanto': 'eo', 'English': 'en', 'Estonian': 'et', 'French': 'fr', 'Finnish': 'fi', 'Greek': 'el', 'Gujarati': 'gu', 'Hindi': 'hi', 'Hungarian': 'hu', 'Icelandic': 'is', 'Indonesian': 'id', 'Japanese': 'ja', 'Kannada': 'kn', 'Khmer': 'km', 'Korean': 'ko', 'Lao': 'lo', 'Macedonian': 'mk', 'Malayalam': 'ml', 'Burmese': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Serbian': 'sr', 'Sinhala': 'si', 'Swedish': 'sv', 'Tamil': 'ta', 'Telugu': 'te', 'Turkish': 'tr', 'Ukrainian': 'uk'}

    ## primary widgets

    combo = ttk.Combobox(frm, values = box)
    combo.set(SelectL)
    combo.pack(fill="x")

    input_text = scrolledtext.ScrolledText(root, height=10, width=35, fg=bu, bg=wh, wrap='word', undo="true", foreground=bu, selectbackground=bu)
    input_text.focus()
    input_text.pack(fill="both", expand='true')
    input_text2 = tk.Text(root, height=1, fg=bu, bg=bu, wrap='word', undo="true", foreground=bl, selectforeground=gr, selectbackground= bl)

    ## button definitions

    def verbalize_text():
        input_text2.pack_forget()
        V = vlc.MediaPlayer(tempmp3file)
        V.play()
        input_text.tag_add("start", "1.0","end-1c")
        input_text.tag_configure("start", foreground=bl)

    def translate_text():
        input_text2.pack_forget()
        X = combo.get()
        if X == SelectL:
            input_text.delete(1.0, "end-1c")
            input_text.insert(1.0, SelectL)
            pass
        else:
            Y = input_text.get(1.0, "end-1c")
            save3 = cwd+"/.Alex/Alex.mp3"
            translation=translator.translate(Y, dest=languages[X])
            NA = ['Georgian', 'Hausa', 'Hausa', 'Hebrew', 'Igbo', 'Odia', 'Yiddish', 'Yoruba', 'Kurdish', 'Malagasy', 'Marathi', 'Sesotho']
            if X in NA:
                Button.pack_forget()
            else:
                tts = gtts.gTTS((f"{translation.text}"), lang=spoken[X])
                tts.save(tempmp3file)
                Button.pack()
            input_text.delete(1.0, "end-1c")
            input_text.insert(1.0, translation.text)
            input_text.focus()

    def record_voice():
        input_text2.pack_forget()
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
        input_text.delete(1.0, "end-1c")
        input_text.tag_add("start", "1.0","end-1c")
        input_text.tag_configure("start", foreground=bu)
        input_text.insert(1.0, speech)
        input_text.focus()

    def wiki_search():
        input_text2.pack_forget()
        try:
            X = combo.get()
            Y = languages[X]
            wikipedia.set_lang(Y)
            try:
                wiki = wikipedia.summary(input_text.get(1.0, "end-1c"))
            except:
                wiki = "404"
            input_text.delete(1.0, "end-1c")
            input_text.insert(1.0, wiki)
            input_text.focus()
        except:
            sln = Error
            input_text.delete(1.0, "end-1c")
            input_text.insert(1.0, sln)
            combo.focus()

    ## keybindings

    input_text.bind("<Button-3>", popup_menu)
    root.bind("<Control_L><v>", paste)
    root.bind("<Control_L><x>", cut)
    root.bind("<Control_L><c>", copy)
    root.bind("<Control_L><a>", select_all)

    ## defining and packing buttons

    ttk.Button(image = btn1, command=translate_text).pack()
    Button = ttk.Button(image = btn2, command=verbalize_text)
    ttk.Button(image = btn3, command=record_voice).pack()
    ttk.Button(image= btn4, command=wiki_search).pack()

    root.mainloop()

    ## clearing tempfile

    os.unlink(tempmp3file)

if __name__ == "__main__":
    try:
        import gtts, googletrans, vlc, pyttsx3, os, os.path, wikipedia, speech_recognition, pprint, webbrowser, locale, sys, tempfile
        import tkinter as tk
        from tkinter import Tk, PhotoImage, ttk, Menu, filedialog, scrolledtext
        from googletrans import Translator, constants
        from googlesearch import search
        from urllib.request import urlopen
        alexander()
    except:
        print("Not set up. Please execute command: 'sudo python3 /home/[username]/.Alex/setup.py install'")
