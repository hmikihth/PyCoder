import sys


from PyQt6 import QtGui
from PyQt6.Qsci import QsciLexerHTML

# Platform specific fonts
if sys.platform == 'win32':
    defaultFont = 'Consolas'
elif sys.platform == 'darwin':
    defaultFont = 'Monaco'
else:
    defaultFont = 'Bitstream Vera Sans Mono'

propertyID = {'ASPPythonTripleSingleQuotedString': 112, 
                'JavaScriptCommentDoc': 44, 
                'PHPKeyword': 121, 
                'ASPPythonTripleDoubleQuotedString': 113, 
                'VBScriptUnclosedString': 77, 
                'ASPJavaScriptNumber': 60, 
                'PHPOperator': 127, 
                'PythonFunctionMethodName': 100, 
                'PythonTripleDoubleQuotedString': 98, 
                'PythonIdentifier': 102, 
                'ASPJavaScriptWord': 61, 
                'PHPVariable': 123, 
                'ASPPythonKeyword': 111, 
                'ASPPythonFunctionMethodName': 115, 
                'HTMLValue': 19, 
                'HTMLNumber': 5, 
                'HTMLSingleQuotedString': 7, 
                'JavaScriptNumber': 45, 
                'PythonTripleSingleQuotedString': 97, 
                'CDATA': 17, 
                'ASPJavaScriptStart': 55, 
                'ASPVBScriptComment': 82, 
                'HTMLComment': 9, 
                'ASPVBScriptNumber': 83, 
                'ASPJavaScriptSymbol': 65, 
                'JavaScriptSymbol': 50, 
                'PHPSingleQuotedString': 120, 
                'Attribute': 3, 
                'VBScriptStart': 70, 
                'PHPDefault': 118, 
                'ASPVBScriptUnclosedString': 87, 
                'PythonNumber': 93, 
                'ASPVBScriptStart': 80, 
                'SGMLParameterComment': 30, 
                'PHPCommentLine': 125, 
                'ASPStart': 16, 
                'ASPVBScriptIdentifier': 86, 
                'SGMLEntity': 28, 
                'VBScriptKeyword': 74, 
                'HTMLDoubleQuotedString': 6, 
                'Script': 14, 
                'XMLEnd': 13, 
                'Tag': 1, 
                'SGMLError': 26, 
                'ASPVBScriptKeyword': 84, 
                'JavaScriptKeyword': 47, 
                'JavaScriptWord': 46, 
                'ASPPythonOperator': 116, 
                'ASPJavaScriptKeyword': 62, 
                'ASPVBScriptDefault': 81, 
                'PythonKeyword': 96, 
                'UnknownTag': 2, 
                'ASPJavaScriptUnclosedString': 66, 
                'Entity': 10, 
                'ASPPythonComment': 107, 
                'VBScriptIdentifier': 76, 
                'PHPDoubleQuotedString': 119, 
                'XMLTagEnd': 11, 
                'ASPXCComment': 20, 
                'SGMLDoubleQuotedString': 24, 
                'VBScriptString': 75, 
                'JavaScriptComment': 42, 
                'ASPPythonStart': 105, 
                'JavaScriptDefault': 41, 
                'PHPDoubleQuotedVariable': 126, 
                'SGMLBlockDefault': 31, 
                'PythonDefault': 91, 
                'ASPPythonIdentifier': 117, 
                'ASPPythonNumber': 108, 
                'JavaScriptDoubleQuotedString': 48, 
                'JavaScriptSingleQuotedString': 49, 
                'PythonDoubleQuotedString': 94, 
                'ASPJavaScriptSingleQuotedString': 64, 
                'PHPStart': 18, 
                'SGMLParameter': 23, 
                'SGMLSpecial': 27, 
                'VBScriptNumber': 73, 
                'SGMLComment': 29, 
                'ASPJavaScriptRegex': 67, 
                'JavaScriptUnclosedString': 51, 
                'SGMLDefault': 21, 
                'SGMLSingleQuotedString': 25, 
                'Default': 0, 
                'ASPJavaScriptComment': 57, 
                'SGMLCommand': 22, 
                'PythonClassName': 99, 
                'ASPJavaScriptDoubleQuotedString': 63, 
                'ASPPythonClassName': 114, 
                'OtherInTag': 8, 
                'PHPNumber': 122, 
                'VBScriptComment': 72, 
                'ASPPythonDoubleQuotedString': 109, 
                'ASPPythonSingleQuotedString': 110, 
                'PHPComment': 124, 
                'PythonOperator': 101, 
                'VBScriptDefault': 71, 
                'PythonComment': 92, 
                'JavaScriptRegex': 52, 
                'ASPVBScriptString': 85, 
                'UnknownAttribute': 4, 
                'ASPJavaScriptDefault': 56, 
                'ASPAtStart': 15, 
                'ASPJavaScriptCommentLine': 58, 
                'ASPPythonDefault': 106, 
                'PythonStart': 90, 
                'JavaScriptCommentLine': 43, 
                'PythonSingleQuotedString': 95, 
                'XMLStart': 12, 'JavaScriptStart': 40, 
                'ASPJavaScriptCommentDoc': 59}

def styleDescriptions():
    return propertyID.keys()


def defaultStyle():
    defaultStyle = {'Entity': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PHPComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'Script': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPVBScriptComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'XMLEnd': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptCommentDoc': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PythonNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPPythonIdentifier': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'VBScriptKeyword': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLBlockDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPVBScriptDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLSpecial': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPXCComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'JavaScriptRegex': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PHPDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PythonTripleDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'SGMLDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PHPDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLError': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptKeyword': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPPythonTripleDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PHPCommentLine': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPPythonStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptWord': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonTripleSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'HTMLValue': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPPythonComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'JavaScriptSymbol': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptCommentLine': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPPythonDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPVBScriptString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'HTMLComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'VBScriptNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'HTMLDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PythonIdentifier': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLEntity': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonFunctionMethodName': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptUnclosedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptSymbol': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPAtStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPPythonDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'UnknownAttribute': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPVBScriptUnclosedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PythonClassName': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLParameter': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'XMLStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PHPStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPVBScriptStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'OtherInTag': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptUnclosedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'VBScriptIdentifier': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'Default': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'VBScriptDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPPythonNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'Attribute': [defaultFont, '#0000ff', 10, False, False, '#ffffff'], 
                    'ASPPythonOperator': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'Tag': [defaultFont, '#E72500', 10, False, False, '#ffffff'], 
                    'CDATA': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPPythonSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPVBScriptIdentifier': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'UnknownTag': [defaultFont, '#71AB71', 10, False, False, '#ffffff'], 
                    'VBScriptComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptCommentLine': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'VBScriptUnclosedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PHPNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptDoubleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptWord': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'XMLTagEnd': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'SGMLParameterComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'VBScriptStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PHPSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPPythonFunctionMethodName': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonKeyword': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PHPKeyword': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLCommand': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PHPDoubleQuotedVariable': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptCommentDoc': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPVBScriptKeyword': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'SGMLDefault': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PHPOperator': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'VBScriptString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPPythonKeyword': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptKeyword': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'JavaScriptStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptStart': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'HTMLSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'PHPVariable': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptComment': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPPythonClassName': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'JavaScriptNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPPythonTripleSingleQuotedString': [defaultFont, '#00B500', 10, False, False, '#ffffff'], 
                    'ASPVBScriptNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'ASPJavaScriptRegex': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'HTMLNumber': [defaultFont, '#000000', 10, False, False, '#ffffff'], 
                    'PythonOperator': [defaultFont, '#000000', 10, False, False, '#ffffff']}

    return defaultStyle


class HtmlLexer(QsciLexerHTML):

    def __init__(self, style, paper):
        QsciLexerHTML.__init__(self)

        self.lexerPaper = paper

        for key, attrib in style.items():
            value = propertyID[key]
            self.setColor(QtGui.QColor(attrib[1]), value)
            self.setEolFill(True, value)
            self.setPaper(QtGui.QColor(attrib[5]), value)
            if self.lexerPaper[0] == "Plain":
                self.setPaper(QtGui.QColor(attrib[5]), value)
            else:
                self.setPaper(QtGui.QColor(self.lexerPaper[1]), value)

            font = QtGui.QFont(attrib[0], attrib[2])
            font.setBold(attrib[3])
            font.setItalic(attrib[4])
            self.setFont(font, value)

        if self.lexerPaper[0] == "Plain":
            self.setDefaultPaper(QtGui.QColor("#ffffff"))
        else:
            self.setDefaultPaper(QtGui.QColor(self.lexerPaper[1]))
