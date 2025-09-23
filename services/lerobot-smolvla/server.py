from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok", "robot":"waveshare_m3", "smolvla_loaded":True}

@app.post("/natural_command")
def natural_command(cmd: dict):
    return {"ok": True, "command_received": cmd.get("command","")}
