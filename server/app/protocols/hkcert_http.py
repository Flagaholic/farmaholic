import logging
import requests

from models import FlagStatus, SubmitResult

logger = logging.getLogger(__name__)
TIMEOUT = 5

def submit_flags(flags, config):
    url = config["SYSTEM_URL"]
    token = config["SYSTEM_TOKEN"]

    headers = {
        "Content-Type": "application/json",
        "Origin": "http://10.2.60.1",
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
    }

    for item in flags:
        payload = {"flag": item.flag, "token": token}
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=TIMEOUT)
        except Exception as e:
            yield SubmitResult(item.flag, FlagStatus.QUEUED, f"request_error={e}")
            continue

        try:
            j = r.json()
        except Exception:
            yield SubmitResult(item.flag, FlagStatus.QUEUED, f"HTTP {r.status_code}; non_json={r.text[:200]}")
            continue

        data = j.get("data") or {}
        is_pass = data.get("is_pass")
        is_dup = data.get("is_duplicate")
        code = j.get("code")

        if is_pass is False:
            st = FlagStatus.REJECTED
        elif is_pass is True:
            if is_dup is True:
                st = FlagStatus.DUPLICATED
            else:
                st = FlagStatus.ACCEPTED
        else:
            st = FlagStatus.QUEUED

        resp = f"HTTP {r.status_code}; code={code}; is_pass={is_pass}; is_duplicate={is_dup}"
        yield SubmitResult(item.flag, st, resp)
