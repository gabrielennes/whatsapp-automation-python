import os
import sys
import requests

GRAPH = "https://graph.facebook.com/v21.0"


def load_env_file(path: str = ".env") -> None:
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = val


def send_text_message(body: str) -> dict:
    token = os.environ.get("WHATSAPP_TOKEN", "").strip()
    phone_id = os.environ.get("PHONE_NUMBER_ID", "").strip()
    to = os.environ.get("TO_NUMBER", "").strip()

    missing = [n for n, v in [
        ("WHATSAPP_TOKEN", token),
        ("PHONE_NUMBER_ID", phone_id),
        ("TO_NUMBER", to),
    ] if not v]
    if missing:
        print("Missing environment variables:", ", ".join(missing))
        print("Use a .env file (see .env.example) or export them in your system.")
        sys.exit(1)

    url = f"{GRAPH}/{phone_id}/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = { 
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to,
        "type": "text",
        "text": {"preview_url": False, "body": body},
    }

    r = requests.post(url, json=payload, headers=headers, timeout=30)
    try:
        data = r.json()
    except Exception:
        data = {"raw": r.text}

    if not r.ok:
        print(r.status_code, data)
        sys.exit(1)
    return data


if __name__ == "__main__":
    load_env_file()
    msg = " ".join(sys.argv[1:]).strip() or "WhatsApp Cloud API integration working successfully via Python."
    out = send_text_message(msg)

    print("Message sent successfully")
    print(f"Recipient: {out['contacts'][0]['wa_id']}")
    print(f"Message ID: {out['messages'][0]['id']}")
