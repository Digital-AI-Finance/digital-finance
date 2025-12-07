@echo off
REM Compile all Module 4 Traditional Digital Finance lessons 40-48
REM Created: 2025-12-07

echo Compiling Module 4 Traditional Digital Finance Lessons 40-48...
echo.

echo Compiling Lesson 40: Electronic Trading and Orders...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_40_electronic_trading.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 40 compilation failed
) else (
    echo Lesson 40 compiled successfully
)
echo.

echo Compiling Lesson 41: Market Microstructure and HFT...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_41_market_microstructure.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 41 compilation failed
) else (
    echo Lesson 41 compiled successfully
)
echo.

echo Compiling Lesson 42: Risk Management Systems...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_42_risk_management.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 42 compilation failed
) else (
    echo Lesson 42 compiled successfully
)
echo.

echo Compiling Lesson 43: RegTech and Compliance...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_43_regtech_compliance.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 43 compilation failed
) else (
    echo Lesson 43 compiled successfully
)
echo.

echo Compiling Lesson 44: Capital Markets Technology...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_44_capital_markets_tech.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 44 compilation failed
) else (
    echo Lesson 44 compiled successfully
)
echo.

echo Compiling Lesson 45: Derivatives Technology...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_45_derivatives_technology.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 45 compilation failed
) else (
    echo Lesson 45 compiled successfully
)
echo.

echo Compiling Lesson 46: Wealth Management Systems...
pdflatex -interaction=nonstopmode 20251207_2115_lesson_46_wealth_management.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 46 compilation failed
) else (
    echo Lesson 46 compiled successfully
)
echo.

echo Compiling Lesson 47: Financial Data Vendors...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_47_data_vendors.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 47 compilation failed
) else (
    echo Lesson 47 compiled successfully
)
echo.

echo Compiling Lesson 48: CBDCs and Future...
pdflatex -interaction=nonstopmode 20251207_2030_lesson_48_cbdc_future.tex
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Lesson 48 compilation failed
) else (
    echo Lesson 48 compiled successfully
)
echo.

echo.
echo ========================================
echo Compilation Summary
echo ========================================
echo All 9 lessons (40-48) compilation attempted.
echo Check above for any errors.
echo.
echo Cleaning up auxiliary files...
del *.aux *.log *.nav *.out *.snm *.toc 2>nul

echo.
echo PDF files created:
dir *.pdf | find "lesson_4"
echo.
echo Compilation complete!
pause
