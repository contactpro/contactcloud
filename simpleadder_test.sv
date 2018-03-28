import uvm_pkg::*;  // added this to include uvm package 
import simpleadder_pkg::*; // added this package
`include "uvm_macros.svh"  // added this to include macros
// `include "C:/Users/HP/WORK_UVM/uvm-1.2/src/uvm_macros.svh" // added this with full path  

class simpleadder_test extends uvm_test;
		`uvm_component_utils(simpleadder_test)

		simpleadder_env sa_env;

		function new(string name, uvm_component parent);
			super.new(name, parent);
		endfunction: new

		function void build_phase(uvm_phase phase);
			super.build_phase(phase);
			sa_env = simpleadder_env::type_id::create(.name("sa_env"), .parent(this));
		endfunction: build_phase

		task run_phase(uvm_phase phase);
			simpleadder_sequence sa_seq;

			phase.raise_objection(.obj(this));
				sa_seq = simpleadder_sequence::type_id::create(.name("sa_seq"), .contxt(get_full_name()));
				assert(sa_seq.randomize());
				sa_seq.start(sa_env.sa_agent.sa_seqr);
			phase.drop_objection(.obj(this));
		endtask: run_phase
endclass: simpleadder_test