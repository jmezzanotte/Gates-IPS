Attribute VB_Name = "FixRows"
Option Explicit

Sub FixRowVals()
    
    Dim oCell As Variant
    
    For Each oCell In Selection
        oCell.Value = oCell.Value
    
    Next oCell
End Sub
