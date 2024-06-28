# Social Network Django App

## Overview

This is a social networking application built using Django. The app allows users to register, login, update their profiles, send friend requests, and post media. Additionally, it includes an API to fetch user details and a WebSocket-based chat feature.

## Features

- User registration and login
- Profile updates including status updates and profile pictures
- Friend requests management
- Media posting
- WebSocket-based real-time chat
- REST API to fetch user details

## Setup

### Create a virtual environment and install dependencies:

```bash
cd MTproj
python3 -m venv myvenv
source venv/bin/activate  # On Windows, use `myvenv\Scripts\activate`
pip install -r requirements.txt