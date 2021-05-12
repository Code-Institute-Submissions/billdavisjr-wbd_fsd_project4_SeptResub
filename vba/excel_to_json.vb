Sub json_export()
' Quoatation JSON export format
'
' 2021-04-02 WBD Created first version to export spreadsheet in JSON format
'
' [
'     {"pk": 1, "model": "quotations.quotation",
'        "fields": {
'            "quotation": "the text of the quote goes here",
'            "person": "John Smith",
'            "source": "The Book",
'            "category": 1,
'        }
'    }
' ]
'

'      Application.ScreenUpdating = False
      
     ' TODO: ADD CODE HERE TO GET COLUMN HEADERS FOR USE IN JSON, in an array.
      'TODO: get field labels from first row rather than hardwiring and lower-case them
    
     ' set numcols = number of columns of data (based on header row A1)

      Range("A1").Select

      'ActiveSheet.Cells(1, Columns.Count).End(xlToLeft).Column
      numcols = ActiveSheet.UsedRange.Columns.Count
      
      ' there are 2 ways to check (at least) make sure they match; UsedRange might not be accurate?
      If numcols <> ActiveSheet.Cells(1, Columns.Count).End(xlToLeft).Column Then
        numcols = ActiveSheet.Cells(1, Columns.Count).End(xlToLeft).Column
      End If
      
      ' Set numrows = number of rows of data until blank line found
      numrows = Range("A2", Range("A2").End(xlDown)).Rows.Count           ' to first blank row  TODO: DO WE NEED A MINUS ONE HERE?
      
      Dim colsBackwards As Integer
      colsBackwards = -(numcols - 1)
      
      ' Select uppper left cell of data rows, skipping column headings on row 1.
      Range("A2").Select
      
      Dim debugging As Boolean
      Dim verbose As Boolean
      debugging = True
      verbose = False
            
      Dim id As Double
      Dim category As Integer
      Dim text As String
      Dim person As String
      Dim source As String
      Dim dateSaid As Date
      Dim strDateSaid As String
      Dim yearsLived As String
      Dim stars As String
      Dim occupation As String
      Dim realName As String
      Dim birthdate As Date
      Dim strBirthDate As String
      Dim notes As String
            
    Dim jsonFile As String: jsonFile = ThisWorkbook.Path & ":quotes.json"
    ' TODO: PROMPT FOR A FILENAME AND OPEN A NEW  TEXT FILE FOR THE JSON
    
    Open jsonFile For Output As #1
    
    Print #1, "["
    If debugging And verbose Then Debug.Print "["
    
    Dim row As Integer

    For row = 1 To numrows
        DoEvents ' give time  back to system so Excel doesn't lock up while converting data.
        If debugging And Not verbose Then Debug.Print row, "/", numrows
        
        id = ActiveCell.Value
         
         ActiveCell.Offset(0, 1).Select
         category = ActiveCell.Value
         
        ' skip over VLOOKUPed column of category display name
        ActiveCell.Offset(0, 1).Select
         
         ActiveCell.Offset(0, 1).Select
         text = ActiveCell.Value
         
         ' The backslash (\) needs in text needs to be "escaped" by making it \\
         ' TODO: What if it already IS escaped?  Search for \\ and replace with \ first?
         '    or assume spaces e.g. change " \ " to " \\ " only?
         text = Replace(text, "\", "\\")
                  
        'TODO: Do a similar Replace() for double quotes to single in any field,
        ' or at least in text, person, source.
        ' Other things;
        '  - Dates must be yyyy-mm-dd
         ' - Strip parentheses out of dateSaid
         ' - Also strip whitespace and collapse (9999 - 9999) to 9999-9999.
         '    - Watch out for (9999 - formatted dates where person is alive
                  
         ActiveCell.Offset(0, 1).Select
         person = ActiveCell.Value
                  
         ActiveCell.Offset(0, 1).Select
         source = ActiveCell.Value
              
        'TODO: Add error trap to date to handle conversion errors
            
         ActiveCell.Offset(0, 1).Select
         dateSaid = ActiveCell.Value
         If dateSaid = 0 Or dateSaid = #12:00:00 AM# Then
             strDateSaid = "null"  ' no quotes around null
        Else
            strDateSaid = """" + Format(dateSaid, "yyyy-mm-dd") + """"
        End If
              
         ActiveCell.Offset(0, 1).Select
         yearsLived = ActiveCell.Value
              
        ActiveCell.Offset(0, 1).Select
        stars = ActiveCell.Value

         ActiveCell.Offset(0, 1).Select
         occupation = ActiveCell.Value ''

         ActiveCell.Offset(0, 1).Select
         realName = ActiveCell.Value

         'TODO: Add error trap to date to handle conversion errors

         ActiveCell.Offset(0, 1).Select
         birthdate = ActiveCell.Value
         If birthdate = 0 Or birthdate = #12:00:00 AM# Then
             strBirthDate = "null"
        Else
            strBirthDate = Format(birthdate, "yyyy-mm-dd")
        End If
        
         ActiveCell.Offset(0, 1).Select
         notes = ActiveCell.Value
        
        If debugging And Not verbose Then Debug.Print id, category, text, person, source
                     
        
        Dim jsonRow As String
        jsonRow = "     { ""pk"": " + Str(id) + ", ""model"":  ""quotations.quotation""," + vbCrLf
        
            jsonRow = jsonRow + "          ""fields"": {" + vbCrLf
            jsonRow = jsonRow + "                              ""text"": " + """" + Trim(text) + """," + vbCrLf
            jsonRow = jsonRow + "                              ""person"": " + """" + Trim(person) + """," + vbCrLf
            jsonRow = jsonRow + "                              ""source"": " + """" + Trim(source) + """," + vbCrLf
            
            jsonRow = jsonRow + "                              ""category"": " + """" + Trim(Str(category)) + """" + "," + vbCrLf
            
            jsonRow = jsonRow + "                              ""dateSaid"": " + strDateSaid + "," + vbCrLf
            
            jsonRow = jsonRow + "                              ""yearsLived"": " + """" + Trim(yearsLived) + """," + vbCrLf
            
            If Len(stars) <= 0 Then stars = "***"
            If Len(stars) > 5 Then stars = "*****"
            
            Dim lenStars As Single
            Dim strStars As String
            lenStars = Len(stars)
            strStars = Format(lenStars, "#.0")
            
            jsonRow = jsonRow + "                              ""stars"": " + """" + Trim(strStars) + """" + "," + vbCrLf
            
            jsonRow = jsonRow + "                              ""occupation"": " + """" + Trim(occupation) + """," + vbCrLf
            jsonRow = jsonRow + "                              ""realName"": " + """" + Trim(realName) + """," + vbCrLf
            
            If strBirthDate = "null" Then
                jsonRow = jsonRow + "                              ""birthdate"": " + strBirthDate + "," + vbCrLf
            Else
            jsonRow = jsonRow + "                              ""birthdate"": " + """" + Trim(strBirthDate) + """," + vbCrLf
            End If
            
            If Len(stars) >= 4 Then
                jsonRow = jsonRow + "                              ""favorite"": " + """" + "True" + """" + "" + vbCrLf
            Else
                jsonRow = jsonRow + "                              ""favorite"": " + """" + "False" + """" + "" + vbCrLf
            End If
            
            ' no Notes field in Django model at present
            'jsonRow = jsonRow + "                              ""notes"": " + """" + Trim(notes) + """" + vbCrLf
            
            jsonRow = jsonRow + "          }" + vbCrLf
            
            If row <> numrows Then
                jsonRow = jsonRow + "     }," + vbCrLf  '  trailing comma cause problem? ONLY ON THE LAST RECORD.
            Else
                jsonRow = jsonRow + "     }" + vbCrLf  '  so don't output on the last record
            End If
                
        Print #1, jsonRow
        If debugging And verbose Then Debug.Print jsonRow
         
         ' Move active cell down one row and back to the first column
        ActiveCell.Offset(1, colsBackwards).Select
        
    Next
    
    If debugging And verbose Then Debug.Print "]"
    Print #1, "]"
    
    Close #1
     
    Application.ScreenUpdating = True
    
End Sub 'json_export


' tojson()
'   source code: https://superuser.com/questions/1249898/saving-excel-sheet-as-json-file
Public Sub tojson()
    Dim fso As Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    jsonFilename = fso.GetBaseName(ActiveWorkbook.Name) & ".json"
    fullFilePath = Application.ActiveWorkbook.Path & "\" & jsonFilename

    Dim fileStream As Object
    Set fileStream = CreateObject("ADODB.Stream")
    fileStream.Type = 2 'Specify stream type - we want To save text/string data.
    fileStream.Charset = "utf-8" 'Specify charset For the source text data.
    fileStream.Open 'Open the stream And write binary data To the object

    Dim wkb As Workbook
    Set wkb = ThisWorkbook

    Dim wks As Worksheet
    Set wks = wkb.Sheets(1)

    lcolumn = wks.Cells(1, Columns.Count).End(xlToLeft).Column
    lrow = wks.Cells(Rows.Count, "A").End(xlUp).row
    Dim titles() As String
    ReDim titles(lcolumn)
    For i = 1 To lcolumn
        titles(i) = wks.Cells(1, i)
    Next i
    fileStream.WriteText "["
    dq = """"
    escapedDq = "\"""
    For j = 2 To lrow
        For i = 1 To lcolumn
            If i = 1 Then
                fileStream.WriteText "{"
            End If
            cellvalue = Replace(wks.Cells(j, i), dq, escapedDq)
            fileStream.WriteText dq & titles(i) & dq & ":" & dq & cellvalue & dq
            If i <> lcolumn Then
                fileStream.WriteText ","
            End If
        Next i
        fileStream.WriteText "}"
        If j <> lrow Then
            fileStream.WriteText ","
        End If
    Next j
    fileStream.WriteText "]"
    fileStream.SaveToFile fullFilePath, 2 'Save binary data To disk
    a = MsgBox("Saved to " & fullFilePath, vbOKOnly)
End Sub


' TODO: Write a HIGHLIGHT duplicate rows/quotes function  (use soundex search algorithm to find similar dupes?)
'  UPDATE: Not needed;  Excel Home tab>Conditional Formatting button> Highlight Cell Rules > Duplicate values will do this well enough, though it slows down the sheet
'  Leaving this here in case we decide I need to do it myself anyway; cleaning up 11,000 quotes can use all the help it can get.
'
' There is a lot of duplication in this quote spreadsheet we need to clean out. 11,000 quotes will make de-duping a lot of work.
'   1. Sort all rows, keyed on the Quote text column
'   2. Look through all rows and compare last row's quote text to this row. If the same, change the text font in this row to red, or the background to yellow.
'  This assumes we'll manually go through the results and remove dupe lines, however we could also compare each column of this row to the last row's
'   and if all are the same, delete the current row or move it to a dupes sheet.

'      Dim lc As Range
'     Dim cc As Range
'        cc = ActiveCell
'        lc = ActiveCell.Offset(-1, 0)  '  this will error out if first row, plus don't forget column headers.
'      If Trim(LCase(c.Value)) = Trim(LCase(cc.Value)) Then
'            cc.Font.Color = vbRed
' or       cc.Font.Background=vbYellow ' or RGB(255, 255, 0)
'        End If
'
'  ALSO: use soundex to generate soundex code for each line, if previous and current line have same soundex, mark current line as dupe.
'  This may help with slight spelling differences etc.
' NOTE: Need to add SoundExCode column!
'
Function soundex(ByVal s As String)
    'http://j-walk.com/ss/excel/tips/tip77.htm
    'http://en.wikipedia.org/wiki/Soundex
    
    ' but with length 7 since company names are longer than person names
    
    slength = 7
    
    s = Trim(s)
    s = UCase(s)
    s = Replace(s, "1", "ONE")
    s = Replace(s, "2", "TWO")
    s = Replace(s, "3", "THREE")
    s = Replace(s, "4", "FOUR")
    s = Replace(s, "5", "FIVE")
    s = Replace(s, "6", "SIX")
    s = Replace(s, "7", "SEVEN")
    s = Replace(s, "8", "EIGHT")
    s = Replace(s, "9", "NINE")
    s = Replace(s, "0", "ZERO")
    s = Replace(s, """", "")
    s = Replace(s, "'", "")
    s = Replace(s, " ", "")
    s = Replace(s, ".", "")
    s = Replace(s, ",", "")
    s = Replace(s, "/", "")
    s = Replace(s, "(", "")
    s = Replace(s, ")", "")
    s = Replace(s, "#", "")
    s = Replace(s, "&", "")
    s = Replace(s, "-", "")
    s = Replace(s, "?", "")

'TODO: What other punctuation should we add?
    
    's = Replace(s, " OF ", "")
    's = Replace(s, " LTD", "")
    's = Replace(s, " LLC", "")'
    's = Replace(s, " L.L.C.", "")
    's = Replace(s, " CO.", "")
    's = Replace(s, "HOLDINGS", "")
    
    's = Replace(s, "1ST", "FIRST")
    's = Replace(s, "2ND", "SECOND")
    's = Replace(s, "3RD", "THIRD")
    's = Replace(s, "DEPARTMENT", "DEPT")
    's = Replace(s, "COMMONWEALTH", "CW")
    's = Replace(s, "UNIVERSITY", "U")
    's = Replace(s, "GOVERNMENT", "GOV")
    's = Replace(s, "AMERICA", "AM")
    's = Replace(s, "MC ", "MC")
    
    'Code    Letter
    ' 1   B F P V
    ' 2   C G J K Q S X Z
    ' 3   D T
    ' 4   L
    ' 5   M N
    ' 6   R
    ' No code A E H I O U Y W

    L = Len(s)
    soundex = Left(s, 1)
    
    For i = 2 To L
    
        ch = Mid(s, i, 1)
        
        If ch = "B" Or ch = "F" Or ch = "P" Or ch = "V" Then
            soundex = soundex & "1"
        ElseIf ch = "C" Or ch = "G" Or ch = "J" Or ch = "K" Or ch = "Q" Or ch = "S" Or ch = "X" Or ch = "Z" Then
            soundex = soundex & "2"
        ElseIf ch = "D" Or ch = "T" Then
            soundex = soundex & "3"
        ElseIf ch = "L" Then
            soundex = soundex & "4"
        ElseIf ch = "M" Or ch = "N" Then
            soundex = soundex & "5"
        ElseIf ch = "R" Then
            soundex = soundex & "6"
        End If
        
        'check for repeated code
        
        If Len(soundex) > 2 Then
            If Right(soundex, 1) = Mid(soundex, Len(soundex) - 1, 1) Then
                soundex = Left(soundex, Len(soundex) - 1)
            End If
        End If
    
        If Len(soundex) = slength Then 'END
            i = L
        End If
        
    Next
    
    ' fill with zeroes
    If Len(soundex) < slength Then
        soundex = Left(soundex & "0000000", slength)
    End If
    
End Function 'soundex()
