//-------------------------------------------------------------------------
//     UVM SEQUENCER 
//-------------------------------------------------------------------------
import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_MODELSIM/project_mem_eda_5r89/sim/tb/mem_seq_item.sv"

`ifndef MEM_SEQUENCER_SV
`define MEM_SEQUENCER_SV

class mem_sequencer extends uvm_sequencer#(mem_seq_item);

  `uvm_component_utils(mem_sequencer) 

  //---------------------------------------
  //constructor
  //---------------------------------------
  function new(string name, uvm_component parent);
    super.new(name,parent);
  endfunction
  
endclass

`endif