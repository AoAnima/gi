# Copyright (c) 2019, The GoKi Authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# to run this python version of the demo:
# * install gopy, currently in fork at https://github.com/goki/gopy
#   e.g., 'go get github.com/goki/gopy -u ./...' and then cd to that package
#   and do 'go install'
# * go to the python directory in this repository, read README.md there, and 
#   type 'make' -- if that works, then type make install (may need sudo)
# * cd back here, and run 'pygi' which was installed into /usr/local/bin
# * then type 'import widgets' and this should run

from gi import go, gi, giv, units, ki, gimain

def strdlgcb(recv, send, sig, data):
    dlg = gi.Dialog(handle=send)
    if sig == gi.DialogAccepted:
        val = gi.StringPromptDialogValue(dlg)
        print("got string value: ", val)

def button1cb(recv, send, sig, data):
    """ callback for button1 press -- lambda functions in python are only 1 line.. """
    sb = gi.Button(handle=send)
    print("Received button signal:", sig, "from button:", sb.Name())
    if sig == gi.ButtonClicked: # note: 3 diff ButtonSig sig's possible -- important to check
        gi.StringPromptDialog(sb.Viewport, "", "Enter value here..",
             gi.DlgOpts(Title="Button1 Dialog", Prompt="This is a string prompt dialog!  Various specific types of dialogs are available."), sb, strdlgcb)

def button2cb(recv, send, sig, data):
    sb = gi.Button(handle=send)
    print("Received button signal:", sig, "from button:", sb.Name())
    if sig == gi.ButtonClicked:
        giv.GoGiEditorDialog(sb.Viewport)

def menu1cb(recv, send, sig, data):
    sa = gi.Action(handle=send)
    print("Received menu action from menu action", sa.Name())

def slidercb(recv, send, sig, data):
    sa = gi.Slider(handle=send)
    print("Received slider signal:", sig, "from slider:", sa.Name(), "val:", sa.Value)

def scrollcb(recv, send, sig, data):
    sa = gi.ScrollBar(handle=send)
    print("Received scroll signal:", sig, "from scrollbar:", sa.Name(), "val:", sa.Value)

def textcb(recv, send, sig, data):
    sa = gi.TextField(handle=send)
    print("Received text signal:", sig, "from field:", sa.Name(), "val:", data)

def spinboxcb(recv, send, sig, data):
    sa = gi.SpinBox(handle=send)
    print("Received spinbox signal:", sig, "from:", sa.Name(), "val:", sa.Value)

def combocb(recv, send, sig, data):
    sa = gi.ComboBox(handle=send)
    print("Received combobox signal:", sig, "from:", sa.Name(), "index:", sa.CurIndex)

def winclosecb(recv, send, sig, data):
    sa = gi.Action(handle=send)
    print("Received menu action from menu action", sa.Name())
    sa.Win.CloseReq()

def mainrun():
    width = 1024
    height = 768

    # turn these on to see a traces of various stages of processing..
    # gi.Update2DTrace = True
    # gi.Render2DTrace = True
    # gi.Layout2DTrace = True
    # ki.SignalTrace = True

    gi.SetAppName("widgets")
    gi.SetAppAbout('This is a demo of the main widgets and general functionality of the <b>GoGi</b> graphical interface system, within the <b>GoKi</b> tree framework.  See <a href="https://github.com/goki">GoKi on GitHub</a>. <p>The <a href="https://github.com/goki/gi/blob/master/examples/widgets/README.md">README</a> page for this example app has lots of further info.</p>')

    win = gi.NewWindow2D("gogi-widgets-demo", "GoGi Widgets Demo", width, height, True) # True = pixel sizes
    
    icnm = "widget-wedge-down"

    vp = win.WinViewport2D()
    updt = vp.UpdateStart()

    # style sheet
    css = ki.Props()
    bg = ki.Props()
    ki.SetPropStr(bg, "background-color", "#FFF0F0FF")
    ki.SetSubProps(css, "button", bg)
    cmbo = ki.Props()
    ki.SetPropStr(cmbo, "background-color", "#F0FFF0FF")
    ki.SetSubProps(css, "#combo", cmbo)
    hsld = ki.Props()
    ki.SetPropStr(hsld, "background-color", "#F0E0FFFF"),
    ki.SetSubProps(css, ".hslides", hsld)
    kbd = ki.Props()
    ki.SetPropStr(kbd, "color", "blue")
    ki.SetSubProps(css, "kbd", kbd)
    vp.CSS = css

    mfr = win.SetMainFrame()
    mfr.SetPropStr("spacing", "1ex")
    # mfr.SetProp("background-color", "linear-gradient(to top, red, lighter-80)")
    # mfr.SetProp("background-color", "linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet)")
    # mfr.SetProp("background-color", "linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1))")
    # mfr.SetProp("background-color", "radial-gradient(red, lighter-80)")

    trow = gi.Layout(mfr.AddNewChild(gi.KiT_Layout(), "trow"))
    trow.Lay = gi.LayoutHoriz
    trow.SetStretchMaxWidth()

    # giedsc = gi.ActiveKeyMap().ChordForFun(gi.KeyFunGoGiEditor())
    # prsc = gi.ActiveKeyMap().ChordForFun(gi.KeyFunPrefs())

    giedsc = "Ctrl+Alt+I"
    prsc = "Alt+P"
    
    title = gi.Label(trow.AddNewChild(gi.KiT_Label(), "title"))
    title.Text = 'This is a <b>demonstration</b> of the <span style="color:red">various</span> <a href="https://github.com/goki/gi/gi">GoGi</a> <i>Widgets</i><br> <large>Shortcuts: <kbd>' + prsc + '</kbd> = Preferences, <kbd>' + giedsc + '</kbd> = Editor, <kbd>Ctrl/Cmd +/-</kbd> = zoom</large><br> See <a href="https://github.com/goki/gi/blob/master/examples/widgets/README.md">README</a> for detailed info and things to try.'
    title.SetPropStr("white-space", "normal") # wrap
    title.SetPropStr("text-align", "center")       # note: this also sets horizontal-align, which controls the "box" that the text is rendered in..
    title.SetPropStr("vertical-align", "center")
    title.SetPropStr("font-family", "Times New Roman, serif")
    title.SetPropStr("font-size", "x-large")
    # # title.SetProp("letter-spacing", 2)
    # title.SetProp("line-height", 1.5)
    title.SetStretchMaxWidth()
    title.SetStretchMaxHeight()

    # Buttons

    mfr.AddNewChild(gi.KiT_Space(), "blspc")
    blrow = gi.Layout(mfr.AddNewChild(gi.KiT_Layout(), "blrow"))
    blab = gi.Label(blrow.AddNewChild(gi.KiT_Label(), "blab"))
    blab.Text = "Buttons:"
    blab.Selectable = True

    brow = gi.Layout(mfr.AddNewChild(gi.KiT_Layout(), "brow"))
    brow.Lay = gi.LayoutHoriz
    brow.SetPropStr("spacing", "2ex")

    brow.SetPropStr("horizontal-align", "left")
    # brow.SetProp("horizontal-align", gi.AlignJustify)
    brow.SetStretchMaxWidth()

    button1 = gi.Button(brow.AddNewChild(gi.KiT_Button(), "button1"))
    # button1.SetProp("#icon", ki.Props{ # note: must come before SetIcon
    # "width":  units.NewValue(1.5, units.Em),
    # "height": units.NewValue(1.5, units.Em),
    # })
    button1.Tooltip = "press this <i>button</i> to pop up a dialog box"

    button1.SetIcon(icnm)
    button1.ButtonSig.Connect(win.This(), button1cb)

    button2 = gi.Button(brow.AddNewChild(gi.KiT_Button(), "button2"))
    button2.SetText("Open GoGiEditor")
    # # button2.SetProp("background-color", "#EDF")
    button2.Tooltip = "This button will open the GoGi GUI editor where you can edit this very GUI and see it update dynamically as you change things"
    button2.ButtonSig.Connect(win.This(), button2cb)

    checkbox = gi.CheckBox(brow.AddNewChild(gi.KiT_CheckBox(), "checkbox"))
    checkbox.Text = "Toggle"

    # # note: receiver for menu items with shortcuts must be a Node2D or Window
    mb1 = gi.MenuButton(brow.AddNewChild(gi.KiT_MenuButton(), "menubutton1"))
    mb1.SetText("Menu Button")
    mb1.Menu.AddAction(gi.ActOpts(Label="Menu Item 1", Shortcut="Shift+Control+1", Data=1), win.This(), menu1cb)
    mi2 = mb1.Menu.AddAction(gi.ActOpts(Label="Menu Item 2", Data=2), go.nil(), go.nil())

    mi2.Menu.AddAction(gi.ActOpts(Label="Sub Menu Item 2", Data=2.1), win.This(), menu1cb)

    mb1.Menu.AddSeparator("sep1")

    mb1.Menu.AddAction(gi.ActOpts(Label="Menu Item 3", Shortcut="Control+3", Data=3),
        win.This(), menu1cb)

    # //////////////////////////////////////////
    #       Sliders

    mfr.AddNewChild(gi.KiT_Space(), "slspc")
    slrow = gi.Layout(mfr.AddNewChild(gi.KiT_Layout(), "slrow"))
    slab = gi.Label(slrow.AddNewChild(gi.KiT_Label(), "slab"))
    slab.Text = "Sliders:"

    srow = gi.Layout(mfr.AddNewChild(gi.KiT_Layout(), "srow"))
    srow.Lay = gi.LayoutHoriz
    srow.SetPropStr("spacing", "2ex")
    srow.SetPropStr("horizontal-align", "left")
    srow.SetStretchMaxWidth()

    slider1 = gi.Slider(srow.AddNewChild(gi.KiT_Slider(), "slider1"))
    slider1.Dim = gi.X
    slider1.Class = "hslides"
    slider1.Defaults()
    slider1.SetMinPrefWidth(units.NewValue(20, units.Em))
    slider1.SetMinPrefHeight(units.NewValue(2, units.Em))
    slider1.SetValue(0.5)
    slider1.Snap = True
    slider1.Tracking = True
    slider1.Icon = "widget-circlebutton-on"

    slider2 = gi.Slider(srow.AddNewChild(gi.KiT_Slider(), "slider2"))
    slider2.Dim = gi.Y
    slider2.Defaults()
    slider2.SetMinPrefHeight(units.NewValue(10, units.Em))
    slider2.SetMinPrefWidth(units.NewValue(1, units.Em))
    slider2.SetStretchMaxHeight()
    slider2.SetValue(0.5)

    slider1.SliderSig.Connect(win.This(), slidercb)
    slider2.SliderSig.Connect(win.This(), slidercb)

    scrollbar1 = gi.ScrollBar(srow.AddNewChild(gi.KiT_ScrollBar(), "scrollbar1"))
    scrollbar1.Dim = gi.X
    scrollbar1.Class = "hslides"
    scrollbar1.Defaults()
    scrollbar1.SetMinPrefWidth(units.NewValue(20, units.Em))
    scrollbar1.SetMinPrefHeight(units.NewValue(1, units.Em))
    scrollbar1.SetThumbValue(0.25)
    scrollbar1.SetValue(0.25)
    scrollbar1.Snap = True
    scrollbar1.Tracking = True
    scrollbar1.SliderSig.Connect(win.This(), scrollcb)

    scrollbar2 = gi.ScrollBar(srow.AddNewChild(gi.KiT_ScrollBar(), "scrollbar2"))
    scrollbar2.Dim = gi.Y
    scrollbar2.Defaults()
    scrollbar2.SetMinPrefHeight(units.NewValue(10, units.Em))
    scrollbar2.SetMinPrefWidth(units.NewValue(1, units.Em))
    scrollbar2.SetStretchMaxHeight()
    scrollbar2.SetThumbValue(0.1)
    scrollbar2.SetValue(0.5)
    scrollbar2.SliderSig.Connect(win.This(), scrollcb)

    # //////////////////////////////////////////
    # #      Text Widgets

    mfr.AddNewChild(gi.KiT_Space(), "tlspc")
    txlrow = gi.Layout(mfr.AddNewChild(gi.KiT_Layout(), "txlrow"))
    txlab = gi.Label(txlrow.AddNewChild(gi.KiT_Label(), "txlab"))
    txlab.Text = "Text Widgets:"
    txrow = gi.Layout(mfr.AddNewChild(gi.KiT_Layout(), "txrow"))
    txrow.Lay = gi.LayoutHoriz
    txrow.SetPropStr("spacing", "2ex")
    # # txrow.SetProp("horizontal-align", gi.AlignJustify)
    txrow.SetStretchMaxWidth()

    edit1 = gi.TextField(txrow.AddNewChild(gi.KiT_TextField(), "edit1"))
    edit1.Placeholder = "Enter text here..."
    # edit1.SetText("Edit this text")
    edit1.SetPropStr("min-width", "20em")
    # edit1.SetCompleter(edit1, Complete, CompleteEdit) # gets us word demo completion
    edit1.TextFieldSig.Connect(win.This(), textcb)
    # edit1.SetProp("inactive", True)

    sb = gi.SpinBox(txrow.AddNewChild(gi.KiT_SpinBox(), "spin"))
    sb.Defaults()
    sb.HasMin = True
    sb.Min = 0.0
    sb.SpinBoxSig.Connect(win.This(), spinboxcb)

    cb = gi.ComboBox(txrow.AddNewChild(gi.KiT_ComboBox(), "combo"))
    cbitms = go.Slice_string(["Item1", "AnotherItem", "Item3"])
    cb.ItemsFromStringList(cbitms, True, 50)
    cb.ComboSig.Connect(win.This(), combocb)

    # //////////////////////////////////////////
    # #      Main Menu

    appnm = gi.AppName()
    mmen = win.MainMenu
    mmen.ConfigMenus(go.Slice_string([appnm, "File", "Edit", "Window"]))

    amen = gi.Action(mmen.ChildByName(appnm, 0))
    # amen.Menu = make(gi.Menu, 0, 10)
    amen.Menu.AddAppMenu(win)

    # note: use KeyFunMenu* for standard shortcuts
    # Command in shortcuts is automatically translated into Control for
    # Linux, Windows or Meta for MacOS
    fmen = gi.Action(win.MainMenu.ChildByName("File", 0))
    fmen.Menu.AddAction(gi.ActOpts(Label="New", ShortcutKey=gi.KeyFunMenuNew), win.This(), menu1cb)
    fmen.Menu.AddAction(gi.ActOpts(Label="Open", ShortcutKey=gi.KeyFunMenuOpen), win.This(), menu1cb)
    fmen.Menu.AddAction(gi.ActOpts(Label="Save", ShortcutKey=gi.KeyFunMenuSave), win.This(), menu1cb)
    fmen.Menu.AddAction(gi.ActOpts(Label="Save As..", ShortcutKey=gi.KeyFunMenuSaveAs), win.This(), menu1cb)
    fmen.Menu.AddSeparator("csep")
    fmen.Menu.AddAction(gi.ActOpts(Label="Close Window", ShortcutKey=gi.KeyFunMenuClose), win.This(), winclosecb)

    emen = gi.Action(win.MainMenu.ChildByName("Edit", 1))
    emen.Menu.AddCopyCutPaste(win)

    # inQuitPrompt = False
    # gi.SetQuitReqFunc(func() {
    # if inQuitPrompt {
    # return
    # }
    # inQuitPrompt = True
    # gi.PromptDialog(vp, gi.DlgOpts{Title: "Really Quit?",
    # Prompt: "Are you <i>sure</i> you want to quit?"}, True, True,
    # win.This(), func(recv, send ki.Ki, sig int64, data interface{}) {
    # if sig == int64(gi.DialogAccepted) {
    # gi.Quit()
    # } else {
    # inQuitPrompt = False
    # }
    # })
    # })

    # gi.SetQuitCleanFunc(func() {
    # print("Doing final Quit cleanup here..")
    # })

    # inClosePrompt = False
    # win.SetCloseReqFunc(func(w gi.Window) {
    # if inClosePrompt {
    # return
    # }
    # inClosePrompt = True
    # gi.PromptDialog(vp, gi.DlgOpts{Title: "Really Close Window?",
    # Prompt: "Are you <i>sure</i> you want to close the window?  This will Quit the App as well."}, True, True,
    # win.This(), func(recv, send ki.Ki, sig int64, data interface{}) {
    # if sig == int64(gi.DialogAccepted) {
    # gi.Quit()
    # } else {
    # inClosePrompt = False
    # }
    # })
    # })

    # win.SetCloseCleanFunc(func(w gi.Window) {
    # print("Doing final Close cleanup here..")
    # })

    win.MainMenuUpdated()
    vp.UpdateEndNoSig(updt)
    win.GoStartEventLoop()

    # note: in python, we use GoStartEventLoop so control returns here
    # to handle cleanup above using QuitCleanFunc, which happens before all
    # windows are closed etc

mainrun()


