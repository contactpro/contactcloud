////////////////////////////////////////////////////////////
//   
// The SystemVerilog to generate transactions
// for the Memory DUT (or other DUT)
// using the Memory Base Object Class:
// mem_base_object defined in mem_base_object.svh
//
// The SystemVerilog task called gen_cmds 
// creates an instance of mem_object and
// creates the mem_object and delivers these transactions
// in the form of mem_object to the mem_driver:
//
// mem_driver.drive_mem(mem_object); 
// 
// rd_wr is 1 for write and 0 for read
//
/////////////////////////////////////////////////////////////

import sv_tb_pkg::*;
`ifndef MEM_DUT_TXGEN_SV
`define MEM_DUT_TXGEN_SV
class mem_txgen;
  mem_base_object  mem_object;
  mem_driver  mem_driver;
  
  integer num_cmds;

function new(virtual mem_ports ports);
  begin
    num_cmds = 50;
    mem_driver = new(ports);
  end
endfunction


task gen_cmds();
  begin
    integer i = 0;
    for (i=0; i < num_cmds; i ++ ) begin
      mem_object = new();
      mem_object.addr = $random();
      mem_object.data = $random();
      mem_object.rd_wr = 1;
      mem_driver.drive_mem(mem_object);
      mem_object.rd_wr = 0;
      mem_driver.drive_mem(mem_object);
    end
  end
endtask

endclass

`endif