REM 
REM *************************************************************************
REM
REM        MODELSIM VIEW WAVES SCRIPT 
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting modelsim_view_waves_script.bat ********************
REM 
REM Printing Working Directory:
REM 
cd
REM 
REM Changing Working Directory .....................
REM 
@ECHO ON
cd C:\Users\HP\WORK_MODELSIM\project_one\sim\
REM 
REM Printing sim Working Directory to verify we are there ........ 
REM 
cd
@ECHO OFF
REM 
REM Load the wlf file and preselected waves and view and/or add add waves.
vsim -view dut_vhdl.wlf -msgmode both -do dut_vhdl_waves.do 
REM
REM
@ECHO ON
REM 
REM
REM *************** Completed modelsim_view_waves_script.bat ******************
REM
REM 