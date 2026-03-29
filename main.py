from fastapi import FastAPI, HTTPException, Header
import requests

app = FastAPI()

GITHUB_API_URL = "https://api.github.com"

def get_headers(token: str):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

@app.get("/")
def root():
    return {"message": "GitHub Connector API is running"}

@app.get("/repos")
def get_repos(username: str, authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        headers = get_headers(token)
        response = requests.get(f"{GITHUB_API_URL}/users/{username}/repos", headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/issues")
def list_issues(owner: str, repo: str, authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        headers = get_headers(token)
        response = requests.get(f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues", headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/create-issue")
def create_issue(owner: str, repo: str, title: str, body: str = "", authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        headers = get_headers(token)
        data = {"title": title, "body": body}

        response = requests.post(f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues", headers=headers, json=data)

        if response.status_code not in [200, 201]:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
