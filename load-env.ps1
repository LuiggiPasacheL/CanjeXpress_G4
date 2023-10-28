$envVariables = Get-Content .\backend\login\.env
foreach ($line in $envVariables) {
    if ($line -match "^(.+)=(.+)$") {
        $varName = $matches[1]
        $varValue = $matches[2]
        [Environment]::SetEnvironmentVariable($varName, $varValue, "Process")
    }
}
