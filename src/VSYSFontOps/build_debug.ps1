Push-Location $PSScriptRoot -StackName DotnetBuild
dotnet build .\VSYSFontOps.csproj --configuration Debug
Pop-Location -StackName DotnetBuild


