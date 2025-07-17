param(
    [int]$p = 2
)

.\venv\Scripts\activate

try{
    if ($p -eq 1) {
        # Write-Host "project: $p"

        cd C:\Tiarles\cs50_python_js_2\2_SQL\django_project\airline
        # python .\manage.py makemigrations auctions
        python .\manage.py migrate
        python .\manage.py runserver 127.0.0.1:8000
        cd ..\..\..\
    }
    elseif ($p -eq 2) {
        # Write-Host "project: $p"
        cd C:\Tiarles\cs50_python_js_2\0_project_2\commerce
        python .\manage.py makemigrations auctions
        python .\manage.py migrate
        python .\manage.py runserver 127.0.0.1:8000
        cd ..\..\
    }
    else {
        Write-Host "Unknown project: $p"
    }
} finally {
    cd C:\Tiarles\cs50_python_js_2
}
