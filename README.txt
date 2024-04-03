How to run Vicii v1.1

0. overview
    application currently split into two routes
        * auth
            For internal SSO integration, not visible to end users 
        * db
            see ./db/operations.py for database API routes

1. set up virtual environment
    `-python3 -m venv env`

2. install requirements (if not already satisfied)
    `-pip3 install -r requirements.txt`

3. run application with uvicorn
    ```
    (env) junho@Junhongs-MacBook-Air project-vicii % uvicorn main:app --reload
    INFO:     Will watch for changes in these directories: ['/Users/junho/startups/project-vicii']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [69164] using StatReload
    INFO:     Started server process [69166]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```    


