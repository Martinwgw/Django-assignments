from django.shortcuts import render
import pandas as pd

def movie(request):
    df = pd.read_csv(r'C:\Users\acer\Downloads\IMDB-Movie-Data.csv')

    analysis = {
      'total_movies': df.shape[0],
      'title': df['Title'],
      'genre': df['Genre']  
    }

    return render(request, 'index.html', {'analysis': analysis})


