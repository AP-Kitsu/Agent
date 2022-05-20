﻿<#	
	.NOTES
	===========================================================================
	 Created with: 	SAPIEN Technologies, Inc., PowerShell Studio 2022 v5.8.199
	 Created on:   	20/05/2022 15:35
	 Created by:   	AlessandroPruna
	 Organization: 	A.S
	 Filename:     	
	===========================================================================
	.DESCRIPTION
		A description of the file.
#>

function makeJson (){

	Get-ComputerInfo | ConvertTo-Json | out-file C:\test.json
	
	(Get-Content C:\test.json).replace('null',"'Null'").replace('true',"'True'") | Set-Content C:\test.json
	
}
makeJson
