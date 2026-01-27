#!/bin/bash
# --- Load Environment Variables ---
# Temporarily enable automatic export of all variables
set -a 
# Source the .env file located one directory up
source .env
# Disable automatic export
set +a
# ---------------------------------

# Deploy to Cloud Run
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION_CLOUD_RUN \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH