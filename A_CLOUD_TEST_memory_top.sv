import sv_tb_pkg::*;

// Memory DUT 
module memory_top(mem_ports ports);
`include "mem_base_object.svh"
`include "mem_driver.svh"
`include "mem_txgen.svh"
`include "mem_scoreboard.svh"
`include "mem_ip_monitor.svh"
`include "mem_op_monitor.svh"
  mem_txgen txgen;
  mem_scoreboard sb;
  mem_ip_monitor ipm;
  mem_op_monitor opm;

initial begin
  sb    = new();
  ipm   = new (sb, ports);
  opm   = new (sb, ports);
  txgen = new(ports);
  fork
    ipm.input_monitor();
    opm.output_monitor();
  join_none
  txgen.gen_cmds();
  repeat (250) @ (posedge ports.clock);
end

endmodule
