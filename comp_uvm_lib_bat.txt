REM 
REM *************************************************************************
REM
REM        MODELSIM COMPILE SCRIPT  
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting comp_uvm_lib.bat ********************
REM 
REM Printing scripts Working Directory:
REM 
cd
REM 
REM Changing Working Directory ..................... 
REM 
cd C:\Users\HP\WORK_MODELSIM\project_eda_296\sim\
REM 
REM Printing sim Working Directory: 
REM     
cd
@ECHO OFF
SET UVM_HOME="C:\Users\HP\WORK_UVM\uvm-1.1d"
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
echo UVM_HOME: %UVM_HOME%
REM   
vlib work
REM  Compile your own UVM ....
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm_pkg.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm_macros.svh +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\dpi\uvm_dpi.cc +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src\dpi

REM  Compile your testbench code  ......
vlog -sv C:\Users\HP\WORK_MODELSIM\project_eda_296\uvm_tb\design.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
vlog -sv C:\Users\HP\WORK_MODELSIM\project_eda_296\uvm_tb\my_testbench_pkg.svh +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
vlog -sv C:\Users\HP\WORK_MODELSIM\project_eda_296\uvm_tb\my_sequence.svh +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
vlog -sv C:\Users\HP\WORK_MODELSIM\project_eda_296\uvm_tb\my_driver.svh +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
vlog -sv C:\Users\HP\WORK_MODELSIM\project_eda_296\uvm_tb\testbench.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM 
@ECHO ON
REM 
REM 
REM *************** Completed comp_uvm_lib.bat ******************
REM 
REM 