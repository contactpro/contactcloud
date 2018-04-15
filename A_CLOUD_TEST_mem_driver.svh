///////////////////////////////////////////////
//
// The SystemVerilog for the mem_driver BFM
// that drives the protocol signals with 
// the drive_mem task to apply stimulus
// to the Memory DUT (or other DUT).
// 
// Note that the mem_ports INTERFACE
// is used to import the INTERFACE
// signals used in this mem_driver.
//
// Note that we are using the 
// mem_base_object class instance
// in the drive_mem task to implement
// the memory driver BFM.
//
// rd_wr is 1 for write and 0 for read
//
//////////////////////////////////////////

import sv_tb_pkg::*;

`ifndef MEM_DUT_DRIVER_SV
`define MEM_DUT_DRIVER_SV

class mem_driver;

virtual mem_ports ports;

function new(virtual mem_ports ports);
  begin
    this.ports = ports;
    ports.address    = 0;
    ports.chip_en    = 0;
    ports.read_write = 0;
    ports.data_in    = 0;
  end
endfunction

task drive_mem (mem_base_object object);
  begin
    @ (posedge ports.clock);
    ports.address    = object.addr;
    ports.chip_en    = 1;
    ports.read_write = object.rd_wr;
    ports.data_in    = (object.rd_wr) ? object.data : 0;
    if (object.rd_wr) begin
      $display("MEMORY DUT DRIVER : Memory Write Access --> Address : %x Data : %x/n", 
        object.addr,object.data);
    end else begin
      $display("MEMORY DUT DRIVER : Memory Read  Access --> Address : %x/n", 
        object.addr);
    end
    @ (posedge ports.clock);
    ports.address    = 0;
    ports.chip_en    = 0;
    ports.read_write = 0;
    ports.data_in    = 0;
 end
endtask

endclass

`endif