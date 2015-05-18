Option Explicit


 
Dim wshShell, shortcut
Dim lnkpath, targetpath

lnkpath = WScript.Arguments(0)
targetpath = WScript.Arguments(1)

'WScript.Echo lnkpath
'WScript.Echo targetpath


Set wshShell = WSH.CreateObject("WScript.Shell")
'  strDir = wshShell.SpecialFolders("Startup")
  Set shortcut = wshShell.CreateShortcut(lnkpath)
    shortcut.TargetPath = targetpath
    shortcut.WindowStyle = 1
    shortcut.Save
  Set shortcut = Nothing
Set wshShell = Nothing


