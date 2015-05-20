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
If shortcut.TargetPath <> targetpath Then
    shortcut.TargetPath = targetpath
    shortcut.WindowStyle = 1
    shortcut.Save
End If
Set shortcut = Nothing
Set wshShell = Nothing

' return 1, if can not save shortcut, the script will return 0
WScript.Quit 1
