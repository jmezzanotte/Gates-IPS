Attribute VB_Name = "LabelDrillingDownItems"
Option Explicit

Sub LabelYAxis()
    
    Dim i As Range
    
    For Each i In Selection
        Select Case i.Value
            Case "q69a"
                i.Value = "Receive district/school-wide PD-q69a"
            Case "q69b"
                i.Value = "Receive training for new admins-q69b"
            Case "q69c"
                i.Value = "Receive mentoring/coaching-q69c"
            Case "q69d"
                i.Value = "Receive interschool collaboration-q69d"
            Case "q69e"
                i.Value = "Receive self-directed learning-q69e"
            Case "q69f"
                i.Value = "Receive other PD-q69f"
            Case "q71a"
                i.Value = "Training for Teacher Evaluation-q71a"
            Case "q71b"
                i.Value = "Classroom Observation-q71b"
            Case "q71c"
                i.Value = "Evaluation Feedback-q71c"
            Case "q71d"
                i.Value = "Other Evaluation Activities-q71d"
            Case "q71e"
                i.Value = ""
            Case "q70a_q70c"
                i.Value = "Provide teacher PD-q70a_q70c"
            Case "q70b"
                i.Value = "Provide non-teacher PD-q70b"
            Case "q72a"
                i.Value = "Staff supervision - q72a"
            Case "q72b"
                i.Value = "Operational management - q72b"
            Case "q72c"
                i.Value = "Data curriculum - q72c"
            Case "q72d"
                i.Value = "Scheduling - q72d"
            Case "q72e"
                i.Value = "Special education meetings - q72e"
            Case "q72f"
                i.Value = "District/State Activities - q72f"
            Case "q72g"
                i.Value = "Interactions w/ students and families - q72g"
            Case "q72h"
                i.Value = "Interactions w/ stackholders - q72h"
            Case "q72i"
                i.Value = "Other administration - q72i"
            
        End Select
    Next i
    


End Sub




