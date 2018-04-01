//
//
////////////////////////////////////////////////////////////////
//
//   Filename: sv_tb_module.sv 
//  
//   Description: SystemVerilog Testbench.
//
//   Note 1: DUT Instantiation and SVA Binding will be here.
//
//   Note 2: In this SystemVerilog Testbench, 
//           Bind SVA File to VHDL DUT Instance. 
//           Review this step for BINDING SVA's to VHDL.
// 
/////////////////////////////////////////////////////////////////
//
//
module sv_tb_module (
  logic [7:0] cout,
  logic load, enable, clk, reset,
  logic [7:0] data);
  
  // sva_wrapper_module instance Binds the
  // SystemVerilog sva_wrapper_module.sv to VHDL DUT instance below .....
  
  sva_wrapper_module sva_wrapper_module_u1 (.*);
  
  // bind vhdl_dut : vhdl_dut_u1 sva_module : sva_module_u1 (.*);
  
endmodule