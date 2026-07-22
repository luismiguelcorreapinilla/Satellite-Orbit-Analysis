# Orbital Mechanics

## Introduction

Artificial satellites follow predictable trajectories governed by Newton's law of gravitation.

Their orbital state can be described using Keplerian orbital elements and propagated using numerical models.

## Two-Line Element (TLE)

A TLE is a standardized data format describing the orbit of an Earth-orbiting satellite.

It includes:

- Inclination
- Right Ascension of the Ascending Node
- Eccentricity
- Argument of Perigee
- Mean Anomaly
- Mean Motion

## SGP4

The Simplified General Perturbations 4 (SGP4) model is the standard algorithm used to propagate Earth satellite orbits from TLE data.

It accounts for gravitational perturbations and atmospheric drag.

## Ground Tracks

A ground track represents the projection of a satellite's orbit onto Earth's surface.

Ground tracks are fundamental for Earth Observation missions because they determine where and when a satellite can observe a region.

## Coverage Analysis

Coverage analysis estimates the spatial and temporal visibility of satellites over a region of interest.

In this project, coverage is evaluated over Colombia and its major cities.
