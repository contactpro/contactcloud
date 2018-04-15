//////////////////////////////////////////
//
// The SystemVerilog Base Object Class
// for the Memory DUT (or other DUT).
// 
// rd_wr is 1 for write and 0 for read
//
//////////////////////////////////////////
import sv_tb_pkg::*;
`ifndef MEM_DUT_BASE_OBJECT_SV
`define MEM_DUT_BASE_OBJECT_SV
class mem_base_object;
  bit [7:0] addr;
  bit [7:0] data;
  // Read = 0, Write = 1
  bit rd_wr;
endclass
`endif