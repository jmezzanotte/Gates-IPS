Attribute VB_Name = "FormatDrillingDownPrinVsAPTable"
Option Explicit

Sub Main()

    Dim wrkbk As Workbook
    Dim wrksht As Worksheet
    Dim c As Range
    Dim headers As Range
    Set wrkbk = ActiveWorkbook
    Set wrksht = wrkbk.Worksheets(1)
    Dim lastCol As Integer
    Dim lastRow As Integer
    Dim i As Integer
    
    Const ADMIN_ROW_START = 2
    Const ADMIN_ROW_END = 10
    Const PDR_ROW_START = 11
    Const PDR_ROW_END = 16
    Const PDP_ROW_START = 17
    Const PDP_ROW_END = 18
    Const EVAL_ROW_START = 19
    Const EVAL_ROW_END = 23
    Const CMO_OFFSET = 22
    
    lastCol = wrksht.UsedRange.Columns(wrksht.UsedRange.Columns.Count).Column
    Set headers = wrksht.Range(Cells(1, 1), Cells(1, lastCol))
    headers.Select
    headers.Borders.ColorIndex = 1
    
    For i = 1 To lastCol
        wrksht.Range(Cells(ADMIN_ROW_START, i), Cells(ADMIN_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(PDR_ROW_START, i), Cells(PDR_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(PDP_ROW_START, i), Cells(PDP_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(EVAL_ROW_START, i), Cells(EVAL_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
    
        wrksht.Range(Cells(ADMIN_ROW_START + CMO_OFFSET, i), Cells(ADMIN_ROW_END + CMO_OFFSET, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(PDR_ROW_START + CMO_OFFSET, i), Cells(PDR_ROW_END + CMO_OFFSET, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(PDP_ROW_START + CMO_OFFSET, i), Cells(PDP_ROW_END + CMO_OFFSET, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(EVAL_ROW_START + CMO_OFFSET, i), Cells(EVAL_ROW_END + CMO_OFFSET, i)).BorderAround ColorIndex:=1, Weight:=xlThin
    Next i
    
   ChangeHeadersPrinAP headerRng:=headers
End Sub

Sub InsertColumns(colRange As Range, header As String, wrksht As Worksheet)

    colRange.EntireColumn.Insert
    With wrksht.Cells(colRange.Row, colRange.Column - 1)
        .Value = header
        .Font.Bold = True
    End With
   

End Sub

Sub MergeRows(mergeRng As Range, sectionName As String)
    
    With mergeRng
        .Merge
        .Value = sectionName
        .Font.Bold = True
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
    End With
    
End Sub

Sub AddSite(rng As Range, site As String)
    With rng
        .Merge
        .Value = site
        .Font.Bold = True
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
    End With
    
End Sub

Sub ChangeHeadersPrinAP(headerRng As Range)

    Dim i As Range
    
    For Each i In headerRng
        Select Case i.Value
            Case "Avg_prin2011"
                i.Value = "Prin. 2011"
            Case "Avg_ap2011"
                i.Value = "AP 2011"
            Case "PrinminusAp2011"
            Case "PrinminusAp2012"
            Case "PrinminusAp2013"
            Case "PrinminusAp2014"
            Case "PrinminusAp2015"
                i.Value = "Difference"
            Case "Avg_prin2012"
                i.Value = "Prin 2012"
            Case "Avg_ap2012"
                i.Value = "AP 2012"
            Case "Avg_prin2013"
                i.Value = "Prin. 2013"
            Case "Avg_ap2013"
                i.Value = "AP 2013"
            Case "Avg_prin2014"
                i.Value = "Prin. 2014"
            Case "Avg_ap2014"
                i.Value = "AP 2014"
            Case "Avg_prin2015"
                i.Value = "Prin 2015"
            Case "Avg_ap2015"
                i.Value = "AP 2015"
        End Select
    Next i

End Sub


