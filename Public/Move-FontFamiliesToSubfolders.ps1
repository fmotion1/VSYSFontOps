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

            # This is our font file
            $File = $_

            # Storing the folder the font being processed resides within
            $FontBaseDirectory = [System.IO.Directory]::GetParent($File).FullName

            # Font Family Name: Convert to TitleCase if the family name is all uppercase.
            [System.String]$FontFamilyName = & $Using:PythonCMD $Using:Script $File
            $FontFamilyName = Remove-InvalidFilenameCharacters $FontFamilyName

            if($FontFamilyName -ceq $FontFamilyName.ToUpper()){
                $FontFamilyName = $FontFamilyName.ToLower()
                $NewFamilyName = (Get-Culture).TextInfo.ToTitleCase($FontFamilyName)
            } else {
                $NewFamilyName = $FontFamilyName
            }

            # Font Filename: Convert to TitleCase if the filename is all uppercase.
            $fontFileName = [System.IO.Path]::GetFileNameWithoutExtension($File)
            if($fontFileName -ceq $fontFileName.ToUpper()){
                $fontFileName = $fontFileName.ToLower()
                $NewFileName = (Get-Culture).TextInfo.ToTitleCase($fontFileName)
            } else {
                $NewFileName = $fontFileName
            }

            # Convert extension to lowercase
            $fontExtension = [System.IO.Path]::GetExtension($File)
            $fontExtension = [System.IO.Path]::ChangeExtension($fontExtension, $fontExtension.ToLower())

            # Construct path segments
            $finalFileName = "$($NewFileName)$fontExtension"
            $FinalFile = [System.IO.Path]::Combine($FontBaseDirectory, $NewFamilyName, $finalFileName)

            # Create the final directory to move the font to if it doesn't exist.
            $FinalDirectory = [System.IO.Directory]::GetParent($FinalFile)
            if(-not($FinalDirectory | Test-Path)){
                New-Item $FinalDirectory -ItemType Directory -Force | Out-Null
            }
            
            # Move the damn file
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