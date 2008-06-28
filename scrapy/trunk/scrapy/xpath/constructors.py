"""
This module provides functions for generating libxml2 documents (xmlDoc).

Constructors must receive a Response object and return a xmlDoc object.
"""

import libxml2

xml_parser_options = libxml2.XML_PARSE_RECOVER + \
                     libxml2.XML_PARSE_NOERROR + \
                     libxml2.XML_PARSE_NOWARNING

html_parser_options = libxml2.HTML_PARSE_RECOVER + \
                      libxml2.HTML_PARSE_NOERROR + \
                      libxml2.HTML_PARSE_NOWARNING

def xmlDoc_from_html(response):
    """Return libxml2 doc for HTMLs"""
    try:
        lxdoc = libxml2.htmlReadDoc(response.body.to_string('utf-8'), response.url, 'utf-8', html_parser_options)
    except TypeError:  # libxml2 doesn't parse text with null bytes
        lxdoc = libxml2.htmlReadDoc(response.body.to_string('utf-8').replace("\x00", ""), response.url, 'utf-8', html_parser_options)
    return lxdoc

def xmlDoc_from_xml(response):
    """Return libxml2 doc for XMLs"""
    return libxml2.readDoc(response.body.to_string('utf-8'), response.url, 'utf-8', xml_parser_options)

