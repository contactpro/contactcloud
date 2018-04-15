///////////////////////////////////////////////////
//
// The SystemVerilog for the mem_op_monitor
// that listens to or monitors the Memory DUT 
// protocol signals with the output_monitor task 
// to acquire the mem_object from
// the Memory DUT (or other DUT).
//  
// Note that the mem_ports INTERFACE
// is used to import the INTERFACE
// signals used in this mem_op_monitor.
//
// Note that we are using the 
// mem_base_object class instance
// in this mem_op_monitor class and 
// the output_monitor task.
// 
// rd_wr is 1 for write and 0 for read.
//
////////////////////////////////////////////////////

import sv_tb_pkg::*;
`ifndef MEM_DUT_OP_MONITOR_SV
`define MEM_DUT_OP_MONITOR_SV
class mem_op_monitor;
  mem_base_object mem_object;
  mem_scoreboard sb;
  virtual mem_ports ports;

function new (mem_scoreboard sb,virtual mem_ports ports);
  begin
    this.sb    = sb;
    this.ports = ports;
  end
endfunction
  

task output_monitor();
  begin
    while (1) begin
      @ (negedge ports.clock);
      if ((ports.chip_en == 1) && (ports.read_write == 0)) begin
        mem_object = new();
        $display("MEMORY DUT OUTPUT MONITOR : Memory Read Access --> Address : %x Data : %x", 
          ports.address,ports.data_out);
        mem_object.addr = ports.address;
        mem_object.data = ports.data_out;
        sb.post_output(mem_object);
      end
    end
  end
endtask


endclass

`endif