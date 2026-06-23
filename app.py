from flask import Flask, request, Response
import requests
import logging

app = Flask(__name__)

DJANGO_WEBHOOK = "https://<YOUR HOME SERVER WEBHOOK URL>"

logging.basicConfig(
    filename='/app/flask_proxy.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)



@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    update = request.get_json(force=True)

    try:
        requests.post(
            DJANGO_WEBHOOK,
            json=update,
            timeout=5
        )
    except Exception as e:
        print(e)

    return "OK", 200



@app.route('/bot<token>/<method>', methods=['GET', 'POST'])
def telegram_proxy(token, method):

    logging.error(f"METHOD={method}")
    logging.error(f"CONTENT_TYPE={request.content_type}")

    telegram_url = f"https://api.telegram.org/bot{token}/{method}"

    # --- FIX FILES ---
    files = {}
    for key, file in request.files.items():
        files[key] = (
            file.filename,
            file.stream,
            file.content_type
        )

    try:
        r = requests.request(
            method=request.method,
            url=telegram_url,
            params=request.args,
            data=request.form,
            json=request.get_json(silent=True),
            files=files if files else None,
            timeout=30
        )

        return Response(
            r.content,
            status=r.status_code,
            content_type=r.headers.get('Content-Type', 'application/json')
        )

    except Exception as e:
        logging.error(str(e))
        raise
