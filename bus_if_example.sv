//-----------------------------------------------------
//
// Design Name : bus_if (SystemVerilog)
// File Name   : bus_if.sv
// Function    : Bus Interface
//
//-----------------------------------------------------

interface bus_if;

logic clk;
logic resetn;
logic[31:0] addr;
logic[31:0] write_data;
logic rnw;
logic valid;
logic ready;
logic[31:0] read_data;
logic error;

endinterface: bus_if
  