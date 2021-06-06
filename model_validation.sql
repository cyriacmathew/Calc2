SELECT 
a.employee_id, A.Ethnicity, a.Gender, a.annual_rt,  a.predicted_Annual_Rt.value, b.predicted_Annual_Rt.value
 FROM 
 `poetic-emblem-309702.prediction_Annual_Pay_without_gend_eth_2021_06_06T08_49_15_062Z.predictions_2021_06_06T08_49_15_062Z` A,
 `poetic-emblem-309702.prediction_untitled_1620700602701_202151123840_2021_06_02T19_11_50_377Z.predictions` B
 where A.Employee_ID = B.Employee_ID
 and b.predicted_Annual_Rt.value -  a.predicted_Annual_Rt.value > 4000
 and (A.Gender = 'F' or A.Ethnicity <> 'White')
and cast(A.Annual_Rt as float64) < b.predicted_Annual_Rt.value
