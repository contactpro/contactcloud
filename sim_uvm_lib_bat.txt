REM 
REM *************************************************************************
REM
REM        MODELSIM SIMULATION SCRIPT 
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting sim_uvm_lib.bat ********************
REM 
REM Printing Working Directory:
REM 
cd
REM 
REM Changing Working Directory .....................
REM 
@ECHO ON
cd C:\Users\HP\WORK_MODELSIM\project_eda_296\sim\
REM 
REM Printing sim Working Directory to verify we are there ........  
REM  
cd
@ECHO OFF
SET UVM_HOME="C:\Users\HP\WORK_UVM\uvm-1.1d"
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
REM 
REM vsim -voptargs="+acc" +UVM_TESTNAME=your_uvm_testname
REM
vsim -c top -modelsimini ./modelsim_uvm_1_1d.ini +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d -msgmode both -do C:\Users\HP\WORK_MODELSIM\project_uvm_lib\sim\sim.do -wlf C:\Users\HP\WORK_MODELSIM\project_uvm_lib\sim\dut.wlf
REM 
REM Optional to load the wlf file and add add waves.
REM vsim -view up_counter_load.wlf
REM
REM Optional to bring waves up automatically .......
REM vsim -do up_counter_load_waves.do 
REM
@ECHO ON
REM 
REM
REM *************** Completed sim_uvm_lib.bat ******************
REM 
REM 