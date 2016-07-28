Attribute VB_Name = "SigTableFormaterPlusMin"
Option Explicit


Sub FormatSignPlusMinus(sheetName As String, startRow As Integer, numRows As Integer, pvalColIndex As Integer, _
    diffColIndex As Integer)
    
    '''''
    ' Written by : John Mezzanotte jmezzanotte@air.org
    ' Date : 6-28-16
    '
    ' Params
    ' sheetName(STRING) - The sheetname that holds the data you wish to format
    ' startRow(INTEGER) - The row number where your data starts
    ' numRows(INTEGER) - The number of total rows of data to be formatted
    ' pValColIndex(INTEGER) - The column index number of the column that contains the P-Value
    ' diffColIndex(INTEGER) - The number of columns from the p-val column where the formatting should be applied
    '
    ''''
    Dim wrkbk As Workbook
    Dim wrksht As Worksheet
    Dim targetCell As Range
    Dim i As Integer

    Set wrkbk = ActiveWorkbook
    Set wrksht = wrkbk.Worksheets(sheetName)

    For i = startRow To numRows
        If wrksht.Cells(i, pvalColIndex).Value <= 0.05 And _
            wrksht.Cells(i, diffColIndex).Value < 0 Then
                'wrksht.Cells(i, diffColIndex).NumberFormat = "0.0%\*"
                wrksht.Cells(i, diffColIndex) = "-"
        ElseIf wrksht.Cells(i, pvalColIndex).Value <= 0.05 And _
            wrksht.Cells(i, diffColIndex).Value >= 0 Then
                wrksht.Cells(i, diffColIndex) = "+"
        ElseIf wrksht.Cells(i, pvalColIndex).Value > 0.05 Then
            wrksht.Cells(i, diffColIndex).Value = ""
        End If
    Next i
    
End Sub

Sub FormatPlusMinus()

    Dim pvalCol As Integer
    
    For pvalCol = 9 To 36 Step 3
        'running a check of the loop
        'Debug.Print pvalCol & " " & pvalCol - 2
                                  
        Call FormatSignPlusMinus("ovearll district sig rev", 2, 8, pvalCol, pvalCol - 2)
        
    Next pvalCol
    

    
End Sub

