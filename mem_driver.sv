//-------------------------------------------------------------------------
//      UVM DRIVER   
//-------------------------------------------------------------------------
import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_MODELSIM/project_mem_eda_5r89/sim/tb/mem_seq_item.sv"

`ifndef MEM_DRIVER_SV
`define MEM_DRIVER_SV

`define DRIV_IF vif.DRIVER.driver_cb

class mem_driver extends uvm_driver #(mem_seq_item);

  //--------------------------------------- 
  // Virtual Interface
  //--------------------------------------- 
  virtual mem_if vif;
  `uvm_component_utils(mem_driver)
    
  //--------------------------------------- 
  // Constructor
  //--------------------------------------- 
  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction : new

  //--------------------------------------- 
  // build phase
  //---------------------------------------
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
     if(!uvm_config_db#(virtual mem_if)::get(this, "", "vif", vif))
       `uvm_fatal("NO_VIF",{"virtual interface must be set for: ",get_full_name(),".vif"});
  endfunction: build_phase

  //---------------------------------------  
  // run phase
  //---------------------------------------  
  virtual task run_phase(uvm_phase phase);
    forever begin
      seq_item_port.get_next_item(req);
      drive();
      seq_item_port.item_done();
    end
  endtask : run_phase
  
  //---------------------------------------
  // drive - transaction level to signal level
  // drives the value's from seq_item to interface signals
  //---------------------------------------
  virtual task drive();
    `DRIV_IF.wr_en <= 0;
    `DRIV_IF.rd_en <= 0;
    @(posedge vif.DRIVER.clk);
    
    `DRIV_IF.addr <= req.addr;
    
    if(req.wr_en) begin // write operation
      `DRIV_IF.wr_en <= req.wr_en;
      `DRIV_IF.wdata <= req.wdata;
      @(posedge vif.DRIVER.clk);
    end
    else if(req.rd_en) begin //read operation
      `DRIV_IF.rd_en <= req.rd_en;
      @(posedge vif.DRIVER.clk);
      `DRIV_IF.rd_en <= 0;
      @(posedge vif.DRIVER.clk);
      req.rdata = `DRIV_IF.rdata;
    end
    
  endtask : drive
endclass : mem_driver

`endif