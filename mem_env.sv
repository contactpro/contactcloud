//-------------------------------------------------------------------------
//     UVM ENV   
//-------------------------------------------------------------------------
import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_MODELSIM/project_mem_eda_5r89/sim/tb/mem_agent.sv"
`include "C:/Users/HP/WORK_MODELSIM/project_mem_eda_5r89/sim/tb/mem_scoreboard.sv"

`ifndef MEM_MODEL_ENV_SV
`define MEM_MODEL_ENV_SV

class mem_model_env extends uvm_env;
  
  //---------------------------------------
  // agent and scoreboard instance
  //---------------------------------------
  mem_agent      mem_agnt;
  mem_scoreboard mem_scb;
  
  `uvm_component_utils(mem_model_env)
  
  //--------------------------------------- 
  // constructor
  //---------------------------------------
  function new(string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new

  //---------------------------------------
  // build_phase - crate the components
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);

    mem_agnt = mem_agent::type_id::create("mem_agnt", this);
    mem_scb  = mem_scoreboard::type_id::create("mem_scb", this);
  endfunction : build_phase
  
  //---------------------------------------
  // connect_phase - connecting monitor and scoreboard port
  //---------------------------------------
  function void connect_phase(uvm_phase phase);
    mem_agnt.monitor.item_collected_port.connect(mem_scb.item_collected_export);
  endfunction : connect_phase

endclass : mem_model_env

`endif

