import streamlit as st
import numpy as np
import pandas as pd
import folium
from streamlit_folium import st_folium

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(layout="wide")
st.title("🛰️ Satellite Coverage over Colombia")

# =========================
# LOAD TLE FILE
# =========================
def load_tle_file(filepath):
    sats = []

    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    i = 0
    while i < len(lines) - 2:
        name = lines[i]
        l1 = lines[i+1]
        l2 = lines[i+2]

        if l1.startswith("1") and l2.startswith("2"):
            sats.append({
                "name": name,
                "l1": l1,
                "l2": l2
            })
            i += 3
        else:
            i += 1

    return sats

# =========================
# ORBIT FUNCTIONS
# =========================
MU = 398600.4418

def mean_motion_to_semi_major_axis(n):
    n_rad = n * 2 * np.pi / 86400
    return (MU / n_rad**2)**(1/3)

def solve_kepler(M, e):
    E = M
    for _ in range(10):
        E = E - (E - e*np.sin(E) - M) / (1 - e*np.cos(E))
    return E

def propagate_satellite(sat, duration_minutes=1440, step_seconds=120):

    parts = sat["l2"].split()

    i = np.radians(float(parts[2]))
    raan = np.radians(float(parts[3]))
    e = float("0." + parts[4])
    argp = np.radians(float(parts[5]))
    M0 = np.radians(float(parts[6]))
    n = float(parts[7])

    a = mean_motion_to_semi_major_axis(n)

    lats, lons = [], []

    for t in range(0, duration_minutes * 60, step_seconds):

        M = M0 + (n * 2*np.pi / 86400) * t
        E = solve_kepler(M, e)

        x = a * (np.cos(E) - e)
        y = a * np.sqrt(1 - e**2) * np.sin(E)

        X = x * np.cos(raan) - y * np.cos(i) * np.sin(raan)
        Y = x * np.sin(raan) + y * np.cos(i) * np.cos(raan)
        Z = y * np.sin(i)

        r = np.sqrt(X**2 + Y**2 + Z**2)
        lat = np.degrees(np.arcsin(Z / r))
        lon = np.degrees(np.arctan2(Y, X))

        lats.append(lat)
        lons.append(lon)

    return lats, lons

# =========================
# CITIES
# =========================
cities = {
    "Bogotá": (4.7110, -74.0721),
    "Medellín": (6.2442, -75.5812),
    "Cali": (3.4516, -76.5320),
    "Barranquilla": (10.9639, -74.7964),
    "Cartagena": (10.3910, -75.4794),
    "Bucaramanga": (7.1193, -73.1227),
    "Pereira": (4.8143, -75.6946),
    "Santa Marta": (11.2408, -74.1990),
    "Manizales": (5.0703, -75.5138),
    "Cúcuta": (7.8891, -72.4967)
}

# =========================
# CACHE (IMPORTANT)
# =========================
@st.cache_data
def compute_satellites(filepath, city_lat, city_lon):

    sats = load_tle_file(filepath)
    passing = []

    for sat in sats[:3000]:  # limitar para rendimiento

        lats, lons = propagate_satellite(sat)

        for lat, lon in zip(lats, lons):
            if abs(lat - city_lat) < 2 and abs(lon - city_lon) < 2:
                passing.append(sat["name"])
                break

    return passing

# =========================
# UI
# =========================
city = st.selectbox("Select a city", list(cities.keys()))
lat, lon = cities[city]

st.subheader(f"📍 {city}")
st.write(f"Latitude: {lat}, Longitude: {lon}")

# =========================
# COMPUTE
# =========================
with st.spinner("Analyzing satellite passes..."):
    sats_passing = compute_satellites("data/active.txt", lat, lon)

# =========================
# METRICS
# =========================
st.metric("Satellites passing (24h)", len(sats_passing))

# =========================
# TABLE
# =========================
df = pd.DataFrame(sats_passing, columns=["Satellite Name"])
st.dataframe(df, use_container_width=True)

# =========================
# MAP
# =========================
m = folium.Map(location=[lat, lon], zoom_start=6, tiles="CartoDB Voyager")

folium.Marker(
    [lat, lon],
    tooltip=city
).add_to(m)

st_folium(m, width=800)

for city, (lat, lon) in cities.items():
    count = len(compute_satellites("../data/active.txt", lat, lon))
