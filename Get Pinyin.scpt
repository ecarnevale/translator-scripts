(*
Created by Emanuel Carnevale
Copyright (c) 2008 emanuelcarnevale.com . All rights reserved.

http://www.opensource.org/licenses/mit-license.php



*)

property openhandle : "http://json-zh.appspot.com/pinyin"
property my_handle : "大"

using terms from application "Quicksilver"
	on process text t
		getHandle(t)
	end process text
end using terms from

on getHandle(handle)
	
	set shell_script to "/usr/bin/python ~/translator-scripts/translator_json_parser.py -p -t " & my_query
	
	set answer to do shell script shell_script
		
	tell application "Quicksilver"
		show large type answer
	end tell
	
	set the clipboard to answer
	
end getHandle