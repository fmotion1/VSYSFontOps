function Convert-FontToNerdFont {
    param (
        [Parameter(Mandatory,ValueFromPipeline)]
        $File
    )

    begin {
        try {
            Get-Command "$PSScriptRoot\..\bin\FontForge\bin\fontforge.exe"
        }
        catch {
            Write-Error "Can't find bundled fontforge."
            return
        }
    }
}