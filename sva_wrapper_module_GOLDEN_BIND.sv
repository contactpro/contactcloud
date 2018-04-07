//
//
////////////////////////////////////////////////////////////////
//
//   Fielname: sva_wrapper_module.sv
//
//   Description: SVA Wrapper module for SystemVerilog Assertions
//
//   Note 1: Implement Long Label Assertion Names
//
//   Note 2: Use macros to shorten assertion property/sequence
//           `assert_async_reset and `assert_clk
//
//   Note 3: Bind the SVA to the VHDL DUT using this
//           sva_wrapper.sv module.
//           Review this step for BINDING SVA's to VHDL.
//
/////////////////////////////////////////////////////////////////
//
//
module sva_wrapper_module;

bind vhdl_dut    // bind the following to vhdl_dut 

// bind the sva_module to vhdl_dut and  
// call this instantiation sva_module_bind
sva_module sva_module_bind  
                                  
// .SV_PORT(VHDL_PORTS)  then  .SV_PORT(VHDL_INTERNAL_SIGNALS)
// Connect the SystemVerilog ports to 
// VHDL DUT ports (cout, data,load, enable, clk, reset)
(
.cout(cout),
.data(data),
.load(load),
.enable(enable),
.clk(clk),
.reset(reset)
); 
            
endmodule