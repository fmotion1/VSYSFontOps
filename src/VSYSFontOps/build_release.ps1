Push-Location $PSScriptRoot -StackName DotnetBuild
dotnet build .\VSYSFontOps.csproj --configuration Release
Pop-Location -StackName DotnetBuild
Read-Host "Press any key to continue"


