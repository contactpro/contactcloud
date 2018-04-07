REM 
REM *************************************************************************
REM
REM        MODELSIM COMPILE SCRIPT 
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting modelsim_compile_script.bat ********************
REM 
REM Printing scripts Working Directory:
REM 
cd
REM 
REM Changing Working Directory ..................... 
REM 
cd C:\Users\HP\WORK_MODELSIM\project_one\sim\
REM 
REM Printing sim Working Directory:
REM   
cd
REM  
vlib work
REM 
vlog -sv C:\Users\HP\WORK_MODELSIM\project_one\sim\tb\sv_tb_module.sv
vlog -sv C:\Users\HP\WORK_MODELSIM\project_one\sim\tb\sva_module.sv
vlog -sv C:\Users\HP\WORK_MODELSIM\project_one\sim\tb\sva_wrapper_module.sv
REM 
REM 
vcom C:\Users\HP\WORK_MODELSIM\project_one\hdl\vhdl\vhdl_dut.vhd
REM 
REM We have removed the VHDL Testbench and letting SystemVerilog control everything.
REM   vcom C:\Users\HP\WORK_MODELSIM\project_one\sim\tb\vhdl_dut_tb.vhd
REM 
@ECHO ON
REM 
REM 
REM *************** Completed modelsim_compile_script.bat ******************
REM 
REM 