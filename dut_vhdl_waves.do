onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -radix hexadecimal /sv_tb_module/inst_dut/cout
add wave -noupdate /sv_tb_module/inst_dut/data
add wave -noupdate /sv_tb_module/inst_dut/load
add wave -noupdate /sv_tb_module/inst_dut/enable
add wave -noupdate /sv_tb_module/inst_dut/clk
add wave -noupdate /sv_tb_module/inst_dut/reset
add wave -noupdate -radix hexadecimal /sv_tb_module/inst_dut/count
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {1023 ps} 0}
quietly wave cursor active 1
configure wave -namecolwidth 258
configure wave -valuecolwidth 65
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ps
update
WaveRestoreZoom {0 ps} {4515 ps}
