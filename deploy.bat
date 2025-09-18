@echo off
:: =================================================================
:: Script to deploy a local Frappe app to a running Docker container
:: =================================================================

:: --- CONFIGURATION ---
:: Please set the following variables to match your environment

:: 1. The name or ID of your running Frappe Docker container
set CONTAINER_NAME=frappe_docker-backend-1

:: 2. The full path to your local custom app directory
set "LOCAL_APP_PATH=E:\github\erpnext_china_translation"

:: 3. The name of your app's folder (the part that gets copied)
set APP_NAME=erpnext_china_translation

:: 4. The name of your site inside the container
set SITE_NAME=frontend

:: --- SCRIPT ---
echo [1/4] Copying app files to the container...
docker cp "%LOCAL_APP_PATH%\." %CONTAINER_NAME%:/home/frappe/frappe-bench/apps/%APP_NAME%/

:: Check if the copy was successful
if %errorlevel% neq 0 (
    echo ERROR: Failed to copy files. Please check paths and Docker status.
    pause
    exit /b
)

echo [2/4] Changing file ownership inside the container...
docker exec -u root %CONTAINER_NAME% chown -R frappe:frappe /home/frappe/frappe-bench/apps/%APP_NAME%

echo [3/4] Clearing cache...
docker exec %CONTAINER_NAME% bench --site %SITE_NAME% clear-cache

echo [4/4] Restarting Frappe services...
docker exec %CONTAINER_NAME% bench restart

echo.
echo =================================
echo  Deployment script finished!
echo =================================
echo.
pause
