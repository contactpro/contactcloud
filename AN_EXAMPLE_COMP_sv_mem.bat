REM 
REM *************************************************************************
REM
REM        MODELSIM COMPILE SCRIPT  
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting comp_sv_mem.bat ********************
REM 
REM Printing scripts Working Directory:
REM 
cd
REM 
REM Changing Working Directory ..................... 
REM 
cd C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\
REM 
REM Printing sim Working Directory: 
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
vlib work
REM
REM  Compile your own UVM .... 
REM vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm_pkg.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm_macros.svh +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\dpi\uvm_dpi.cc +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src\dpi

REM  Compile your testbench code  ...... 
vlog -sv C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\mem_ports.sv
vlog -sv C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\sv_tb_pkg.sv
vlog -sv C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\mem_base_object.svh C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\mem_txgen.svh C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\mem_driver.svh C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\mem_ip_monitor.svh C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\mem_op_monitor.svh C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\mem_scoreboard.svh 
vlog -sv C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\memory.sv
vlog -sv C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\memory_tb.sv
vlog -sv C:\Users\HP\WORK_MODELSIM\project_sv_mem\sim\sv_tb\memory_top.sv
REM 
@ECHO ON
REM 
REM 
REM *************** Completed comp_sv_mem.bat ******************
REM 
REM 