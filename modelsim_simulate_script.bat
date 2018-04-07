REM 
REM *************************************************************************
REM
REM        MODELSIM SIMULATION SCRIPT 
REM 
REM *************************************************************************
REM 
@ECHO OFF
REM 
REM *************** Starting modelsim_simulation_script.bat ********************
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
REM vsim -voptargs="+acc" +UVM_TESTNAME=your_uvm_testname
REM 
REM NOTE: Dual Top and also we have BINDING per procedure explaining BINDING.
REM
vsim -c sv_tb_module -msgmode both -do C:\Users\HP\WORK_MODELSIM\project_one\sim\sim.do -wlf C:\Users\HP\WORK_MODELSIM\project_one\sim\dut_vhdl.wlf
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
REM *************** Completed modelsim_simulation_script.bat ******************
REM 
REM 