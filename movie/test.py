import pandas as pd
movies_df = pd.read_excel("/workspaces/blank-app/movie.xlsx")

selected = ["action", "animation"]


#filter out all the movie in moviews_df that is genre isd in temp
print(movies_df["genre"].apply(lambda x : any(gene in x for gene in selected)))