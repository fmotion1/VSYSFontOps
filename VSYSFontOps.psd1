@{
    RootModule = "VSYSFontOps.psm1"
    ModuleVersion = '1.0.0'
    GUID = '534d88ec-f4a6-5c23-bccb-067af498bb9d'
    Author = 'Futuremotion'
    CompanyName = 'Futuremotion'
    Copyright = '(c) Futuremotion. All rights reserved.'

    CompatiblePSEditions = @('Core')

    Description = 'Provides tools and functions for analyzing and manipulating font files.'
    PowerShellVersion = '7.0'

    CmdletsToExport = @()
    VariablesToExport = '*'
    AliasesToExport = @()
    ScriptsToProcess = @()
    TypesToProcess = @()
    FormatsToProcess = @()
    FileList = @()

    # Leave commented out to import into any host.
    # PowerShellHostName = ''

    RequiredModules =    ''

    RequiredAssemblies = @( "$PSScriptRoot\Lib\VSYSFontOps.dll" )

    FunctionsToExport = 'Move-FontFamiliesToSubfolders',
                        'Group-FontsByWidth'

    PrivateData = @{
        PSData = @{
            Tags = @('Fonts', 'Typefaces', 'Automation')
            LicenseUri = 'https://github.com/fmotion1/VSYSFontOps/blob/main/LICENSE'
            ProjectUri = 'https://github.com/fmotion1/VSYSFontOps'
            IconUri = ''
            ReleaseNotes = '1.0.0: (12/21/2023) - Initial Release'
        }
    }
}

