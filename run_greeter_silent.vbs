' Silent launcher for Wave Greeter
' This VBS script runs the batch file without showing a command window

Set WshShell = CreateObject("WScript.Shell")
scriptPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WshShell.Run chr(34) & scriptPath & "\run_greeter.bat" & Chr(34), 0
Set WshShell = Nothing