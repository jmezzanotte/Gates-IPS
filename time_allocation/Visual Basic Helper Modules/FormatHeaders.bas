Attribute VB_Name = "FormatHeaders"
Sub FormatHeader()
    
    For Each oCell In Selection
        Select Case oCell.Value
            Case "admin", "A_Administration"
                oCell.Value = "Administration"
            Case "evalteach", "C_Evaluation"
                oCell.Value = "Evaluation"
            Case "instruction", "B_Instruction"
                oCell.Value = "Instruction"
            Case "PD_give", "E_PD Provided"
                oCell.Value = "PD Provided"
            Case "PD_receive", "D_PD Received"
                oCell.Value = "PD Received"
            Case "recruit", "F_Recruitment"
                oCell.Value = "Recruitment"
            Case "reform", "G_Reform"
                oCell.Value = "Reform"
            Case "Mean2011"
                oCell.Value = 2011
            Case "Mean2012"
                oCell.Value = 2012
            Case "Mean2013"
                oCell.Value = 2013
            Case "Mean2014"
                oCell.Value = 2014
            Case "Mean2015"
                oCell.Value = 2015
            Case "mean_prin_2011", "mean_prin_2012", "mean_prin_2013", "mean_prin_2014", "mean_prin_2015"
                oCell.Value = "Principal"
            Case "mean_ap_2011", "mean_ap_2012", "mean_ap_2013", "mean_ap_2014", "mean_ap_2015"
                oCell.Value = "AP"

        End Select
    Next oCell
    

End Sub

