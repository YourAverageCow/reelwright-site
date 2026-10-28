"""Minimal CDP driver for the headed Chromium on display :99 (ws on [::1]:9222)."""
import asyncio, json, sys, urllib.request
import websockets

def page_ws():
    d = json.load(urllib.request.urlopen("http://[::1]:9222/json"))
    for t in d:
        if t.get("type") == "page" and t.get("url", "").startswith("http"):
            return t["webSocketDebuggerUrl"]
    raise SystemExit("no page")

class CDP:
    def __init__(self, ws):
        self.ws_url = ws
        self.id = 0

    async def __aenter__(self):
        self.ws = await websockets.connect(self.ws_url, max_size=64 * 1024 * 1024)
        return self

    async def __aexit__(self, *a):
        await self.ws.close()

    async def call(self, method, **params):
        self.id += 1
        mid = self.id
        await self.ws.send(json.dumps({"id": mid, "method": method, "params": params}))
        while True:
            msg = json.loads(await self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    async def js(self, expr):
        r = await self.call("Runtime.evaluate", expression=expr, returnByValue=True, awaitPromise=True)
        return r.get("result", {}).get("value")

    async def goto(self, url):
        await self.call("Page.navigate", url=url)
        await asyncio.sleep(3)

async def main():
    async with CDP(page_ws()) as c:
        cmd = sys.argv[1] if len(sys.argv) > 1 else "eval"
        if cmd == "eval":
            print(await c.js(sys.argv[2]))
        elif cmd == "goto":
            await c.goto(sys.argv[2])
            print(await c.js("document.title"))
        elif cmd == "script":
            src = open(sys.argv[2]).read()
            print(await c.js(src))

asyncio.run(main())
