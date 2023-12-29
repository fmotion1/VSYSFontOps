<#
.SYNOPSIS
Moves font files to subfolders based on their font family names.

.DESCRIPTION
The Move-FontFamiliesToSubfolders function is used to organize font files by moving
them to subfolders based on their font family names. It takes a list of font file
paths as input and moves each file to a subfolder named after its font family. The
function also converts the font family name and file name to title case if they are
in all uppercase. This function relies on external Python scripts for some
operations.

.PARAMETER Font
Specifies the font files to be processed. Accepts an array of strings representing
file paths.

.PARAMETER MaxThreads
Specifies the maximum number of threads to use for processing the font files. Default
value is 16.

.EXAMPLE
Move-FontFamiliesToSubfolders -Font "C:\Fonts\Arial.ttf", "C:\Fonts\Times New Roman.ttf"

This example moves two font files, Arial.ttf and Times New Roman.ttf, to subfolders
named "Arial" and "Times New Roman" respectively, within the original "C:\Fonts"
directory.

.INPUTS
System.String

.OUTPUTS
None (void)
#>
function Move-FontFamiliesToSubfolders {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string[]]$Font,
        [Int32]$MaxThreads = 16
    )

    begin {
        & "$PSScriptRoot\..\python\FontTools\Scripts\Activate.ps1"
        $PythonCMD = "$PSScriptRoot\..\python\FontTools\Scripts\python.exe"
        $Script = "$PSScriptRoot\..\python\Scripts\FontOpsGetFontFamily.py"
        $List = [System.Collections.Generic.List[String]]::new()
    }

    process {
        try {
            foreach ($P in $Font) {
                if	 ($P -is [String])   { $List.Add($P) }
                elseif ($P.Path)		 { $List.Add($P.Path) }
                elseif ($P.FullName)	 { $List.Add($P.FullName) }
                elseif ($P.PSPath)		 { $List.Add($P.PSPath) }
                else { Write-Error "Invalid argument passed to files parameter."; return; }
            }
        }
        catch {
            $Error[0] | Format-List * -Force
            $PSCmdlet.ThrowTerminatingError($PSItem)
        }
    }

    end {

        $List | ForEach-Object -Parallel {
            function ConvertToTitleCaseIfUpperCase($inputString) {
                if($inputString -ceq $inputString.ToUpper()){
                    $inputString = $inputString.ToLower()
                    return (Get-Culture).TextInfo.ToTitleCase($inputString)
                } else {
                    return $inputString
                }
            }

            $File = $_
            $FontBaseDirectory = [System.IO.Directory]::GetParent($File).FullName

            [System.String]$FontFamilyName = & $Using:PythonCMD $Using:Script $File
            $FontFamilyName = Remove-InvalidFilenameCharacters $FontFamilyName
            $NewFamilyName = ConvertToTitleCaseIfUpperCase $FontFamilyName

            $fontFileName = [System.IO.Path]::GetFileNameWithoutExtension($File)
            $NewFileName = ConvertToTitleCaseIfUpperCase $fontFileName

            $fontExtension = [System.IO.Path]::GetExtension($File).ToLower()
            $finalFileName = "$($NewFileName)$fontExtension"
            $FinalFile = [System.IO.Path]::Combine($FontBaseDirectory, $NewFamilyName, $finalFileName)

            $FinalDirectory = [System.IO.Directory]::GetParent($FinalFile)
            if(-not($FinalDirectory | Test-Path)){
                New-Item $FinalDirectory -ItemType Directory -Force | Out-Null
            }
            [IO.File]::Move($File, $FinalFile) | Out-Null

        } -ThrottleLimit $MaxThreads

        Start-Sleep -Milliseconds 200
        $wshell = New-Object -ComObject wscript.shell;
        $wshell.SendKeys("{F5}")
        Start-Sleep -Milliseconds 200
        $wshell.SendKeys("{F5}")

        & deactivate
    }
}