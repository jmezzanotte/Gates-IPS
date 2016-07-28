Attribute VB_Name = "FormatSignificantResults"

Option Explicit



Sub FormatSignificantResult(sheetName As String, startRow As Integer, numRows As Integer, pvalColIndex As Integer, _
    diffColIndex As Integer)

    Dim wrkbk As Workbook
    Dim wrksht As Worksheet
    Dim targetCell As Range
    Dim i As Integer

    Set wrkbk = ActiveWorkbook
    Set wrksht = wrkbk.Worksheets(sheetName)

    For i = startRow To numRows
        If wrksht.Cells(i, pvalColIndex).Value <= 0.05 Then
            wrksht.Cells(i, diffColIndex).NumberFormat = "0.0%\*"
        ElseIf wrksht.Cells(i, diffColIndex).Value <> "." Then
             wrksht.Cells(i, diffColIndex).NumberFormat = "0.0%"
        End If
    Next i
    
End Sub


Sub main()

    Dim pvalCol As Integer
    
    For pvalCol = 8 To 38 Step 5
        'running a check of the loop
        'Debug.Print pvalCol & " " & pvalCol - 2
        Call FormatSignificantResult("Sheet1", 2, 45, pvalCol, pvalCol - 2)
        
    Next pvalCol
    

    
End Sub



