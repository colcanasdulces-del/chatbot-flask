#!/bin/bash
# Asegura que pip esté actualizado y reinstala dependencias
pip install --upgrade pip
pip install -r requirements.txt
# Arranca la app con gunicorn
exec gunicorn app:app