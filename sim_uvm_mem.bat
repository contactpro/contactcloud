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
cd C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\
REM 
REM Printing sim Working Directory to verify we are there ........  
REM  
cd
@ECHO OFF
SET UVM_HOME="C:\Users\HP\WORK_UVM\uvm-1.1d"
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
SET UVM_TB_DIR="C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb"
echo UVM_TB_DIR: %UVM_TB_DIR%
echo UVM_TB_DIR: %UVM_TB_DIR%
echo UVM_TB_DIR: %UVM_TB_DIR%
SET UVM_TB_DIR="C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim"
echo UVM_SIM_DIR: %UVM_SIM_DIR%
echo UVM_SIM_DIR: %UVM_SIM_DIR%
echo UVM_SIM_DIR: %UVM_SIM_DIR%
REM 
REM vsim -voptargs="+acc" +UVM_TESTNAME=mem_wr_rd_test
REM
vsim -c -voptargs="+acc" testbench_top -modelsimini ./modelsim_uvm_1_1d.ini +incdir+C:/Users/HP/WORK_UVM/uvm-1.1d/src -msgmode both -do C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\sim.do -wlf C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\mem_dut_wlf.wlf
REM 
REM
REM vsim -c -voptargs="+acc" testbench_top -modelsimini ./modelsim_uvm_1_1d.ini +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d -msgmode both -do C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\sim.do -wlf C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\mem_dut_wlf.wlf
REM 
REM Optional to load the wlf file and add add waves.
REM vsim -view mem_dut_wlf.wlf
REM
REM Optional to bring waves up automatically .......
REM vsim -do mem_dut_waves.do 
REM
@ECHO ON
REM 
REM
REM *************** Completed sim_uvm_lib.bat ******************
REM 
REM 
