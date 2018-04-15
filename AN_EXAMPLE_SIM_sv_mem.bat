REM 
REM *************************************************************************
REM
REM        MODELSIM SIMULATION SCRIPT 
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting sim_sv_mem.bat ********************
REM 
REM Printing Working Directory:
REM 
cd
REM 
REM Changing Working Directory .....................
REM 
@ECHO ON
cd C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\
REM 
REM Printing sim Working Directory to verify we are there ........  
REM  
cd
@ECHO OFF
SET UVM_HOME="C:\Users\HP\WORK_UVM\uvm-1.1d"
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
SET SV_TB_DIR="C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb"
echo SV_TB_DIR: %SV_TB_DIR%
echo SV_TB_DIR: %SV_TB_DIR%
echo SV_TB_DIR: %SV_TB_DIR%
REM 
REM vsim -voptargs="+acc" +UVM_TESTNAME=your_uvm_testname 
REM vsim -voptargs="+acc" top
REM dual top would also have memory_tb memory_top
vsim -c -voptargs="+acc" memory_tb -modelsimini ./modelsim_uvm_1_1d.ini +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d -msgmode both -do C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sim.do -wlf C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\memory_wlf.wlf
REM 
REM Optional to load the wlf file and add add waves.
vsim -view memory_wlf.wlf -do memory_waves.do 
REM
REM Optional to bring waves up automatically .......
REM vsim -do memory_waves.do 
REM
@ECHO ON
REM 
REM
REM *************** Completed sim_sv_mem.bat ******************
REM 
REM 