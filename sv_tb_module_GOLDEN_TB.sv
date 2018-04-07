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

interface sv_tb_dut_if(input bit clk, reset);
  logic [7:0] cout;
  logic load, enable;
  logic [7:0] data;
endinterface: sv_tb_dut_if


module test (sv_tb_dut_if test_intf);
initial 
  begin
    test_intf.enable=0;
    test_intf.load=0;
    test_intf.data='1;  // all ones on data input 
    #100;
    test_intf.load=1;
    #100;
    test_intf.load=0;
    #100;
    repeat(5)
      begin
        #100;
        test_intf.enable=1;
        #500;
        test_intf.enable=0;
        #100;
      end
    #500;
    $finish;
  end
endmodule
 

module sv_tb_module();
  bit clk, reset;
  sv_tb_dut_if inst_intf(clk, reset);
  
  vhdl_dut inst_dut(
  .cout(inst_intf.cout), 
  .data(inst_intf.data), 
  .load(inst_intf.load), 
  .enable(inst_intf.enable), 
  .clk(clk), 
  .reset(reset)
  );
  
  // sva_wrapper_module instance Binds the    
  // SystemVerilog sva_wrapper_module.sv to VHDL DUT instance below .....
  
  sva_wrapper_module sva_wrapper_module_u1 (.*);
  
  // // // bind vhdl_dut : vhdl_dut_u1 sva_module : sva_module_u1 (.*);
  

  // Instantiate test module
  test inst_test(inst_intf);
  
  initial
    begin
    	reset = 0;
    	#10;
    	reset = 1;
    	#100;
    	reset = 0;
      forever #(10) clk=~clk;
    end
  
endmodule