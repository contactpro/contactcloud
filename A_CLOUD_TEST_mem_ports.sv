///////////////////////////////////////////////
//
// This is the mem_ports INTERFACE that 
// is used to reference the INTERFACE
// signals throughout the SystemVerilog 
// Verification Infrastructure.
// 
// read_write is 1 for write and 0 for read
// 
////////////////////////////////////////////////

`ifndef MEM_DUT_PORTS_SV
`define MEM_DUT_PORTS_SV

interface mem_ports(
 input  wire  clock,
 output logic [7:0] address,
 output logic chip_en,
 output logic read_write,
 output logic [7:0] data_in,
 input logic [7:0] data_out
);
endinterface

`endif