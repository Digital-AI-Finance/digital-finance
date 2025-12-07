@echo off
REM Compile all Module 3 lessons and clean up helper files
REM Run from module_03_ai_ml directory

echo ===============================================
echo Compiling Module 3: AI/ML in Finance
echo All 12 Lessons (25-36)
echo ===============================================
echo.

REM Create temp directory
if not exist temp mkdir temp

REM Compile each lesson
FOR %%f IN (20251207*.tex) DO (
    echo Compiling %%f...
    pdflatex -interaction=nonstopmode "%%f" > temp\compile_%%~nf.log 2>&1
    if errorlevel 1 (
        echo ERROR compiling %%f - check temp\compile_%%~nf.log
    ) else (
        echo SUCCESS: %%~nf.pdf created
    )
)

echo.
echo ===============================================
echo Cleaning up helper files...
echo ===============================================

REM Move all helper files to temp
move *.aux temp\ >nul 2>&1
move *.log temp\ >nul 2>&1
move *.nav temp\ >nul 2>&1
move *.out temp\ >nul 2>&1
move *.snm temp\ >nul 2>&1
move *.toc temp\ >nul 2>&1

echo.
echo ===============================================
echo Compilation Complete
echo ===============================================
echo.

REM Count PDF files
echo PDF files created:
dir /b *.pdf | find /c ".pdf"

echo.
echo All PDF files are in the current directory
echo Helper files moved to temp\
echo.
pause
