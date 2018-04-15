/////////////////////////////////////////////////////////////////////////
//
// file: sv_tb_pkg.sv 
//
// This SystemVerilog Testbench Package contains the
// CLASSES utilized in this Verification Infrastructure.
//
// We import this SystemVerilog Testbench Package, containing the
// CLASSES utilized in this Verification Infrastructure,
// to all SystemVerilog code that utilizes these CLASSES.
//  
/////////////////////////////////////////////////////////////////////////
//
package sv_tb_pkg;
  `include "C:/Users/HP/WORK_MODELSIM/project_sv_mem/sim/sv_tb/mem_base_object.svh"
  `include "C:/Users/HP/WORK_MODELSIM/project_sv_mem/sim/sv_tb/mem_driver.svh"
  `include "C:/Users/HP/WORK_MODELSIM/project_sv_mem/sim/sv_tb/mem_txgen.svh"
  `include "C:/Users/HP/WORK_MODELSIM/project_sv_mem/sim/sv_tb/mem_scoreboard.svh"
  `include "C:/Users/HP/WORK_MODELSIM/project_sv_mem/sim/sv_tb/mem_ip_monitor.svh"
  `include "C:/Users/HP/WORK_MODELSIM/project_sv_mem/sim/sv_tb/mem_op_monitor.svh"
endpackage