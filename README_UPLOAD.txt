SUPPLIER CAPABILITY HUB — STREAMLIT DEPLOYMENT

The core app needs two files. To ensure the purple-and-white light theme is consistent, also add the supplied .streamlit/config.toml to the repository.

1. Open the GitHub repository used by your existing Streamlit app (verify it under Streamlit → Manage app).
2. In the repository root, replace app.py with the app.py in this folder.
3. Replace requirements.txt with the requirements.txt in this folder.
4. In GitHub, click Add file → Create new file. Type .streamlit/config.toml as the filename. Paste the contents of .streamlit/config.toml from this package and commit. (Skip this if the correct theme config is already in your repository.)
5. Commit changes; Streamlit Community Cloud will redeploy using app.py.
6. Reboot under Manage app if your existing browser session keeps an old version.

Do not upload the ZIP itself.
The application is self-contained: its engine, assessments and synthetic data are bundled inside app.py.
Older engine.py / workspace.py / data/*.json in the repository are not needed by this version.

It is an evaluation environment: all four supplier cases are fictional, and the 55 questionnaire questions are newly written illustrative items, NOT the official Siemens questionnaire. The bundled research search contains synthetic method notes, NOT original internal documents. Copilot and Snowflake are not live-connected.

Local run on Mac:
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py

No credentials, Snowflake client or LLM key is required.
Changes stay in the current Streamlit server session. Export before restarting.
Only publish with the appropriate corporate approvals. Do not imply Siemens Energy has approved this demonstration.
