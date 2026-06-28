# 🛰️ Satellite Orbit Analysis over Colombia

This project analyzes satellite trajectories using real TLE (Two-Line Element) data, implementing orbital propagation models to visualize and calculate coverage over Colombia.

## 🚀 Features
- **Orbital Propagation:** Using Keplerian models to predict satellite positioning.
- **Ground Track Visualization:** Mapping 2D and 3D paths relative to Earth's surface.
- **Coverage Analysis:** Statistical evaluation of satellite passes over major Colombian cities.
- **Interactive Dashboard:** Core analysis deployed into a user-friendly interface using Streamlit.

## 📂 Project Structure
- `Notebooks/` → Step-by-step mathematical and exploratory analysis.
- `data/` → TLE datasets.
- `Images/` → Output visualizations and assets.
- `app.py` → Interactive dashboard codebase.

## 📊 Analysis Workflow (Notebooks)
1. Data loading and preprocessing of TLE structures.
2. Extraction of Keplerian orbital elements.
3. Orbital propagation algorithms & ground track generation.
4. Geospatial coverage analysis filtered by Colombian city coordinates.

## 🛠️ Technologies
- **Core Language:** Python
- **Data & Math:** NumPy, Pandas
- **Visualization & Geospatial:** Matplotlib, Folium
- **Deployment:** Streamlit

## ▶️ Run the Dashboard Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```


## Images

### Ground Tracks
![img](/Images/groundtracks.png)



### Orbits over Colombia
![img](/Images/map.png)



## Dashboard

### Counting satellites over cities
![img](/Images/cities.png)





## 👨‍💻 Author

# Luis Miguel Correa
