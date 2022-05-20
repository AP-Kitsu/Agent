<#	
	.NOTES
	===========================================================================
	 Created with: 	SAPIEN Technologies, Inc., PowerShell Studio 2022 v5.8.199
	 Created on:   	20/05/2022 15:35
	 Created by:   	AlessandroPruna
	 Organization: 	A.S
	 Filename:     	
	===========================================================================
	.DESCRIPTION
		prende le info e le mette in json
#>

function makeJson (){
	
	$a = Get-ComputerInfo | ConvertTo-Json
	
	$a.replace('null','"Null"').replace('true','"True"').replace('false','"False"') 
	
}

$b = makeJson
$b