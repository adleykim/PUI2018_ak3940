Very good idea and interesting thing to investigate. The Null hypothesis formulation si correct and consistent with the idea. 

The data is not fully processed: you still have not obtained your rations. But you are on the right track in splitting the months and the geneder. 

From the plot onwoard however I think you may be going in the wrong direction (and I realize this is not part of the assignment)

1 - issues with the plot: The plot shows only July. It should show both July and January. I am not sure why it does not since your dataframe looked right above. 
2 - an esthetic note: we try to stay away from assigning obviously geneder biased colors to genders: you used pink for women and blue for man. those colors trigger associations in the reader preventing them from being able to have an impartial objective read of your work (same as plotting red for bad, or people ethnicity by the assumed skin color)
3 - you actually do not need percentages because you are comparing ratios. Not a big deal but you are doing a bunch of unnecessary operations loosing precision and wasting computational resources

*test* 

you are comparing ratios this is a very common occurrence in, e.g., medical sciences: think about comparing the ratio of something before and after a treatment.
here you are comparing ratios, but your independent variable is not time (before/after) but gender (also commonly done in medical studies by the way)

you can use for proportions (e.g. chisq) or you can also use a test for means (t-test) using the normalized mean ride count (basically you are assuming that July is "normalized" by Jan). For the last setup it is better to use the fraction of July to total, so tet W(July) / W(July+Jan) against M(July) / M(July+Jan)
Basically this is the same setup as the Hard to Employ exercise



