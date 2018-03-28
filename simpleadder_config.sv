import uvm_pkg::*;  // added this to include uvm package 
import simpleadder_pkg::*; // added this package
`include "uvm_macros.svh"  // added this to include macros

class simpleadder_configuration extends uvm_object;
	`uvm_object_utils(simpleadder_configuration)

	function new(string name = "");
		super.new(name);
	endfunction: new
endclass: simpleadder_configuration
