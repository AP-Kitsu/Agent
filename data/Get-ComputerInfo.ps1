

function makeJson () {
	
	$a = Get-ComputerInfo | ConvertTo-Json
	
	$a.replace('null', '"Null"').replace('true', '"True"').replace('false', '"False"')
	
	Out-File -InputObject $a -FilePath $PWD\psjsonUTF8.json -Force -Encoding utf8
}

makeJson