REM 
REM *************************************************************************
REM
REM        MODELSIM COMPILE SCRIPT  
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting comp_uvm_mem.bat ********************
REM 
REM Printing scripts Working Directory:
REM 
cd
REM 
REM Changing Working Directory ..................... 
REM 
cd C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\
REM 
REM Printing sim Working Directory:  
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
SET UVM_SIM_DIR="C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim"
echo UVM_SIM_DIR: %UVM_SIM_DIR%
echo UVM_SIM_DIR: %UVM_SIM_DIR%
echo UVM_SIM_DIR: %UVM_SIM_DIR%
REM   
REM
REM
REM
REM
vlib work
REM
REM
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM  Compile your own UVM ....  
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm_pkg.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
REM
REM
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\uvm_macros.svh +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_UVM\uvm-1.1d\src\dpi\uvm_dpi.cc +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src\dpi
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\memory.sv
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_interface.sv
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_seq_item.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_sequence.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_sequencer.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_agent.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_base_test.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_driver.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src 
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_env.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_monitor.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_scoreboard.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\mem_wr_rd_test.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
vlog -sv C:\Users\HP\WORK_MODELSIM\project_mem_eda_5r89\sim\tb\testbench_top.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM
REM
REM
echo "  "
echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
echo "  "
REM
REM
REM
REM Compile the SystemVerilog for this UVM Verification Infrastructure. 
REM vlog -sv VLOG_SC_COMMAND_LIST +incdir+C:\Users\HP\WORK_UVM\uvm-1.2\src

REM  Compile your testbench code  ...... 
REM REF THIS COMPILE ORDER ... vlog -sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_seq_item.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_sequence.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_rd_seq.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_wr_seq.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_sequencer.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_driver.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_monitor.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_agent.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_scoreboard.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_model_env.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\mem_model_test.sv C:\Users\HP\WORK_MODELSIM\project_uvm_mem\uvm_tb\tbench_top.sv +incdir+C:\Users\HP\WORK_UVM\uvm-1.1d\src
REM 
@ECHO ON
REM 
REM 
REM *************** Completed comp_uvm_mem.bat ******************
REM 
REM 