Set WshShell = WScript.CreateObject("WScript.Shell")

Sub OpenCMD()
    WshShell.Run "cmd /K cd C:\Users\User\Desktop\da", 1, True
    OpenCMD
End Sub

OpenCMD
