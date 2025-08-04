#!/usr/bin/env bash
# Build script for Render

# Install dependencies
pip install -r requirements.txt

# Create database and populate with data
python scripts/criar_admin.py
python scripts/popular_exercicios.py
