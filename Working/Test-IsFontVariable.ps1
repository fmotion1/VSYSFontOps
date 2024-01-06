function Test-IsFontVariable {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [String[]] $Font
    )

    begin {
        if(!(Test-Path -LiteralPath $Font)){
            throw "File doesn't exist."
        }
    }
    process {

        & "$PSScriptRoot\..\python\FontTools\Scripts\Activate.ps1"
        $Python = "$PSScriptRoot\..\python\FontTools\Scripts\python.exe"
        
        $VariableScript = "$PSScriptRoot\..\python\Scripts\FontOpsIsVariable.py"

        foreach ($F in $Font) {
            $isVariable = & $Python $VariableScript $F
            $Result = [System.Convert]::ToBoolean($isVariable)
            $Result
        }
    }
}