#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:28:56 2021

@author: v_data
"""

# import libraries
import pandas as pd
import streamlit as st
import hvplot
import hvplot.pandas
import holoviews as hv

st.title('A Netflix story in numbers')

#%% loading data

@st.cache
def get_data():
    df = pd.read_csv('netflix_history.csv', parse_dates=['date'])
	#df['Duration'] = pd.to_timedelta(df['Duration'])
    return df

df = get_data()

if st.checkbox('Show raw data'):
	st.subheader('Data')
	st.write(df)

st.subheader('Netflix timeline') 

# creating a holoviews plot
h=df.groupby(['date', 'show_name'], as_index=True)['hours'].sum()
#netflix_timeline = 
timeline = h.hvplot.heatmap(x='date', y='show_name', C='hours', width=950, height=1000, 
				title='Netflix timeline', cmap='Oranges')
st.write(hv.render(timeline, backend='bokeh'))

# Some number in the range 0-23 
# >>> But in my case a dropdown box to pick the show name
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)

show = st.selectbox('Pick a Show', df['show_name'].unique())
selected_show = df[df.show_name == show]
selected_show

st.subheader('Netflix watching history') 

#w = df.groupby(['Start Time', 'show_name', 'season', 'episode_name'], as_index=True)['minutes'].sum()
nice_plot = df.sort_values(by='Start Time').hvplot.scatter(x='Start Time', y='minutes', frame_width=800, color='minutes',
                  hover_cols=['show_name', 'season', 'episode_name'], rot=70, frame_height=400, cmap='YlGnBu',
                  xlabel='Date', ylabel='Minutes watching', size=80, grid=True, colorbar=False,)

#st.bokeh_chart(hv.render(nice_plot, backend='bokeh'))
st.write(hv.render(nice_plot, backend='bokeh'))




