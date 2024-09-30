#!/usr/bin/env python3

class HtmlCM:
    def __init__(self):
        pass

    def __enter__(self):
        self.__html_start= "<TABLE>\n<TR>\n     <TH>Number</TH><TH>Description</TH>\n</TR>"
        print (self.__html_start)
    
    def __exit__(self, type, value, traceback):
        self.__html_end = "</TABLE>"
        print (self.__html_end)

with HtmlCM() as call:
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD)")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD)")
    print(" </TR>")
