"""Screenshot any page of a CDP browser by URL substring, using a long timeout."""
import asyncio, base64, json, sys, urllib.request
import websockets

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
MATCH = sys.argv[2] if len(sys.argv) > 2 else "accounts.google.com"
OUT = sys.argv[3] if len(sys.argv) > 3 else "/tmp/shot.png"

def find():
    d = json.load(urllib.request.urlopen(f"http://{HOST}:9222/json"))
    pages = [t for t in d if t.get("type") == "page" and MATCH in t.get("url", "")]
    if not pages:
        raise SystemExit("no matching page: " + ", ".join(t.get("url","")[:50] for t in d if t.get("type")=="page"))
    return pages[0]["webSocketDebuggerUrl"], pages[0]["url"]

async def main():
    ws_url, url = find()
    async with websockets.connect(ws_url, max_size=64*1024*1024, open_timeout=20) as ws:
        async def call(i, method, **params):
            await ws.send(json.dumps({"id": i, "method": method, "params": params}))
            while True:
                m = json.loads(await ws.recv())
                if m.get("id") == i:
                    if "error" in m: raise SystemExit(str(m["error"]))
                    return m.get("result", {})
        r = await asyncio.wait_for(call(1, "Page.captureScreenshot", format="png"), timeout=120)
        open(OUT, "wb").write(base64.b64decode(r["data"]))
        print("saved", OUT, "from", url[:80])

asyncio.run(main())
