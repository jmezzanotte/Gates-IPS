Attribute VB_Name = "FormatAppendixTables"
Option Explicit

Sub main()
    
    Dim wrkbk As Workbook
    Dim wrksht As Worksheet
    Dim i As Integer
    Dim lastCol As Integer
    Dim lastRow As Integer
 
    Set wrkbk = ActiveWorkbook
    Set wrksht = wrkbk.Worksheets(1)

    lastRow = wrksht.UsedRange.Rows(wrksht.UsedRange.Rows.Count).Row
       
    Const ADMIN_ROW_START = 2
    Const ADMIN_ROW_END = 10
    Const PDR_ROW_START = 11
    Const PDR_ROW_END = 16
    Const PDP_ROW_START = 17
    Const PDP_ROW_END = 18
    Const EVAL_ROW_START = 19
    Const EVAL_ROW_END = 23
    
    InsertColumns colRange:=wrksht.Range("A:A"), header:="Site", wrksht:=wrksht
    InsertColumns colRange:=wrksht.Range("B:B"), header:="Category", wrksht:=wrksht
    MergeRows mergeRng:=wrksht.Range("B" & ADMIN_ROW_START & ":B" & ADMIN_ROW_END), sectionName:="Administration"
    MergeRows mergeRng:=wrksht.Range("B" & PDR_ROW_START & ":B" & PDR_ROW_END), sectionName:="PD Received"
    MergeRows mergeRng:=wrksht.Range("B" & PDP_ROW_START & ":B" & PDP_ROW_END), sectionName:="PD Provided"
    MergeRows mergeRng:=wrksht.Range("B" & EVAL_ROW_START & ":B" & EVAL_ROW_END), sectionName:="Evaluation"
    
    lastCol = wrksht.UsedRange.Columns(wrksht.UsedRange.Columns.Count).Column
        
    Call ChangeHeaders
        
    For i = 1 To lastCol
        wrksht.Range(Cells(ADMIN_ROW_START, i), Cells(ADMIN_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(PDR_ROW_START, i), Cells(PDR_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(PDP_ROW_START, i), Cells(PDP_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
        wrksht.Range(Cells(EVAL_ROW_START, i), Cells(EVAL_ROW_END, i)).BorderAround ColorIndex:=1, Weight:=xlThin
    Next i

    AddSite rng:=wrksht.Range("A2:A" & lastRow), site:="Aspire"
    wrksht.Range("C1").Value = "2012/2015 Question Item"

    
End Sub


Sub ChangeHeaders()

    Dim wrkbk As Workbook
    Dim wrksht As Worksheet
    Dim c As Range
    Dim headers As Range
    Set wrkbk = ActiveWorkbook
    Set wrksht = wrkbk.Worksheets(1)
    Dim lastCol As Integer
    
    lastCol = wrksht.UsedRange.Columns(wrksht.UsedRange.Columns.Count).Column
    Set headers = wrksht.Range(Cells(1, 1), Cells(1, lastCol))
    headers.Select
    headers.Borders.ColorIndex = 1
    
    For Each c In headers
        c.Font.Bold = True
        Select Case c.Value
            Case "mean2011"
                c.Value = "2011 Mean"
            Case "mean2012"
                c.Value = "2012 Mean"
            Case "mean2013"
                c.Value = "2013 Mean"
            Case "mean2014"
                c.Value = "2014 Mean"
            Case "mean2015"
                c.Value = "2015 Mean"
            Case "dif11_12"
                c.Value = "2011-2012 Difference"
            Case "dif12_13"
                c.Value = "2012-2013 Difference"
            Case "dif13_14"
                c.Value = "2013-2014 Difference"
            Case "dif14_15"
                c.Value = "2014-2015 Difference"
            Case "dif11_13"
                c.Value = "2011-2013 Difference"
            Case "dif11_14"
                c.Value = "2011-2014 Difference"
            Case "dif11_15"
                c.Value = "2011-2015 Difference"
            Case "dif12_14"
                c.Value = "2012-2014 Difference"
            Case "dif12_15"
                c.Value = "2012-2015 Difference"
            Case "dif13_15"
                c.Value = "2013-2015 Difference"
        End Select
    Next c
    
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

