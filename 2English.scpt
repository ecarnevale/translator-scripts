(*
Created by Emanuel Carnevale
Copyright (c) 2008 emanuelcarnevale.com . All rights reserved.

http://www.opensource.org/licenses/mit-license.php



*)

property openhandle : "http://ajax.googleapis.com/ajax/services/language/translate?v=1.0\\&"
property my_query : "大"
property lang_from : ""
property lang_to : "en"

using terms from application "Quicksilver"
	on process text t
		getHandle(t)
	end process text
end using terms from

on getHandle(my_query)
	
	set shell_script to "/usr/bin/python ~/translator-scripts/translator_json_parser.py -t " & my_query
	
	set answer to do shell script shell_script
		
	tell application "Quicksilver"
		show large type answer
	end tell
	
	set the clipboard to answer
	
end getHandle
