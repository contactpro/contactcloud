///////////////////////////////////////////////////
//
// The SystemVerilog for the SCOREBOARD
// that uses the post_input task and the
// post_output task and the mem_object[*]
// keyed list to compare the memory dut 
// output with the the memory dut expected 
// data for each address in the keyed list
// called mem_object[*].
//
// The MEM DUT SCOREBOARD reports *** ERROR *** 
// when the MEM DUT Expected Data and 
// MEM DUT Actual Data do not Match.
//
////////////////////////////////////////////////////

import sv_tb_pkg::*;
`ifndef MEM_DUT_SCOREBOARD_SV
`define MEM_DUT_SCOREBOARD_SV

class mem_scoreboard;
  // Create a keyed list mem_object [*] to store the written data
  // The Key to the list is the address of the write access
  mem_base_object mem_object [*];

  // The post_input method is used to store write data
  // at the memory write address.
task post_input (mem_base_object  input_object);
  begin
    mem_object[input_object.addr] = input_object;
  end
endtask
  // The post_output method is used by the memory output monitor to 
  // compare the output of memory with expected data.
task post_output (mem_base_object  output_object);
  begin
   // Check to see that the address exists in the SCOREBOARD.  
   if (mem_object[output_object.addr] != null) begin 
      mem_base_object  in_mem = mem_object[output_object.addr];
      $display("MEM DUT SCOREBOARD : Found Address %x in the mem_object Keyed List: ",output_object.addr);
      if (output_object.data != in_mem.data)  begin
        $display ("MEM DUT SCOREBOARD : *** ERROR *** : Expected Data and MEM DUT Actual Data do not Match.");
        $display("MEM DUT SCOREBOARD Expected Data  --> %x",
          in_mem.data);
        $display("MEM DUT SCOREBOARD Actual Data  --> %x",
          output_object.data);
      end else begin
        $display("MEM DUT SCOREBOARD : *** Data Compare GOOD - MEM DUT Expected Data and MEM DUT Actual Data Match.");
      end
   end 
  end 
endtask

endclass

`endif