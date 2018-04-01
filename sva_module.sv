//
//
////////////////////////////////////////////////////////////////
//
//   SVA module - SystemVerilog Assertions
//
//   Note 1: Implement Long Label Assertion Names
//
//   Note 2: Use macros to shorten assertion property/sequence
//           `assert_async_reset and `assert_clk
//
//   Note 3: In the SystemVerilog Testbench Top, 
//           Bind SVA File to VHDL DUT Instance. 
//           Review this step for BINDING SVA's to VHDL.
//
///////////////////////////////////////////////////////////////// 
//
//
module sva_module (
  input [7:0] cout, data,
  input load, enable, clk, reset);
  
  ERROR_counter_enable_did_not_enable_cout:
    assert property (@(posedge clk) disable iff (reset) !enable |=> cout == $past(cout) )
       else $error("....... COUNTER ENABLE ERROR - ERROR_counter_enable_did_not_enable_cout");
    
  ERROR_counter_load_input_data_did_not_produce_cout:
    assert property (@(posedge clk) disable iff (reset) enable && load |=> cout == $past(data) )
       else $error("....... COUNTER LOAD ERROR - ERROR_counter_load_input_data_did_not_produce_cout");
    
  ERROR_counter_increment_did_not_increment_at_cout:
    assert property (@(posedge clk) disable iff (reset) enable && !load |=> cout == $past(cout) + 8'b1)
       else $error("....... COUNTER INCREMENT ERROR - ERROR_counter_increment_did_not_increment_at_cout");
    
  ERROR_counter_reset_did_not_reset_cout: 
    assert property (@(posedge reset) reset |=> cout == 8'b0 )
       else $error("....... COUNTER RESET ERROR - ERROR_counter_reset_did_not_reset_cout");
  
  // assert property (@(posedge Clock) Req |-> ##[1:2] Ack);
  
  
  //ERROR_LONG_ASSERTION_LABEL_ONE:
  //`assert_async_reset(reset |-> ...

  //ERROR_LONG_ASSERTION_LABEL_TWO:
  //`assert_clk ...
  
endmodule

