# Registers the SQR language in Komodo.

import logging
from koUDLLanguageBase import KoUDLLanguage

log = logging.getLogger("koSQRLanguage")
#log.setLevel(logging.DEBUG)

def registerLanguage(registry):
    log.debug("Registering language SQR")
    registry.registerLanguage(KoSQRLanguage())

class KoSQRLanguage(KoUDLLanguage):

    # ------------ Komodo Registration Information ------------ #

    name = "SQR"
    lexresLangName = "SQR"
    _reg_desc_ = "%s Language" % name
    _reg_contractid_ = "@activestate.com/koLanguage?language=%s;1" % name
    _reg_categories_ = [("komodo-language", name)]
    _reg_clsid_ = "95f294ad-e4ec-4006-9c38-fd6bdf7527f8"
    defaultExtension = '.sqr'

    # ------------ Commenting Controls ------------ #

    commentDelimiterInfo = {
        "line": [
                #'//',   # C-style one line comments
                #'#',    # Hash-style one line comments
                #'--',   # SQL-style one line comments
                '!',   # SQL-style one line comments
                #';',    # Lisp-style one line comments
                #'%',    # Erlang-style one line comments
                ],
        "block": [
                #('/*', '*/')   # C-style block comments
                #('(*', '*)')   # Pascal-style block comments
                ],
    }

    # ------------ Indentation Controls ------------ #

    # To support automatic indenting and dedenting after "{([" and "})]"
    #supportsSmartIndent = "brace"
    supportsSmartIndent = "keyword"
    # Other smart indenting types are:
    #   'text', 'python', 'XML' and 'keyword'

    # Indent/dedent after these words.
    _indenting_statements = ['#IF','#ELSE','#IFDEF','#IFNDEF',
                             'BEGIN-DOCUMENT','BEGIN-EXECUTE','BEGIN-FOOTING','BEGIN-HEADING','BEGIN-PROCEDURE',
                             'BEGIN-PROGRAM','BEGIN-SELECT','BEGIN-SETUP','BEGIN-SQL',
                             'DECLARE-CHART','DECLARE-COLOR-MAP','DECLARE-CONNECTION','DECLARE-IMAGE','DECLARE-LAYOUT',
                             'DECLARE-PRINTER','DECLARE-PROCEDURE','DECLARE-REPORT','DECLARE-TOC','DECLARE-VARIABLE'
                             'IF','ELSE',
                             '#if','#else','#ifdef','#ifndef',
                             'begin-document','begin-execute','begin-footing','begin-heading','begin-procedure',
                             'begin-program','begin-select','begin-setup','begin-sql',
                             'declare-chart','declare-color-map','declare-connection','declare-image','declare-layout',
                             'declare-printer','declare-procedure','declare-report','declare-toc','declare-variable'
                             'if','else']
    _dedenting_statements = ['end-declare','end-document','end-evaluate','end-execute','end-footing','end-heading',
                             'end-if','end-procedure','end-program','end-select','end-setup','end-sql','end-while',
                             'END-DECLARE','END-DOCUMENT','END-EVALUATE','END-EXECUTE','END-FOOTING','END-HEADING',
                             'END-IF','END-PROCEDURE','END-PROGRAM','END-SELECT','END-SETUP','END-SQL','END-WHILE']

    # ------------ Sub-language Controls ------------ #

    #Check: Update 'lang_from_udl_family' as appropriate for your
    #      lexer definition. There are four UDL language families:
    #           M (markup), i.e. HTML or XML
    #           CSL (client-side language), e.g. JavaScript
    #           SSL (server-side language), e.g. Perl, PHP, Python
    #           TPL (template language), e.g. RHTML, Django, Smarty
    #      'lang_from_udl_family' maps each UDL family code (M,
    #      CSL, ...) to the sub-language name in your language.
    #      Some examples:
    #        lang_from_udl_family = {   # A PHP file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'PHP',           #   PHP
    #           'CSL': 'JavaScript',    #   JavaScript
    #        }
    #        lang_from_udl_family = {   # An RHTML file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'Ruby',          #   Ruby
    #           'CSL': 'JavaScript',    #   JavaScript
    #           'TPL': 'RHTML',         #   RHTML template code
    #        }
    #        lang_from_udl_family = {   # A plain XML can just contain
    #           'M': 'XML',             #   XML
    #        }
    lang_from_udl_family = {'SSL': 'SQR'}
