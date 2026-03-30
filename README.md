# WhatsApp Automation with Python

## Overview

This project demonstrates how to send WhatsApp messages programmatically using the Meta WhatsApp Cloud API.

It simulates a real-world backend integration scenario, where a system communicates with external services to automate workflows.

## Features

- Send real WhatsApp messages via API
- Secure authentication using environment variables
- Clean and simple Python implementation

## Tech Stack

- Python
- Requests
- WhatsApp Cloud API (Meta)

## Requirements

- Python 3.8+
- requests

## Setup

Create a `.env` file with the following variables:

```env
WHATSAPP_TOKEN=your_token_here
PHONE_NUMBER_ID=your_phone_number_id_here
TO_NUMBER=5511999999999
```


## Output

Message sent successfully
Recipient: 5511970626081
Message ID: ...

## Run

```bash
python automation.py
```