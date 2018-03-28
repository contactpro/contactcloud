library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.all;
use ieee.std_logic_textio.all;
use std.textio.all; 


-- entity declaration for your testbench. 
-- Notice that the entity port list is empty here 
-- for the testbench (up_counter_load_tb.vhd).
entity up_counter_load_tb is
end up_counter_load_tb;

architecture behavior of up_counter_load_tb is

-- component declaration for the design under test (dut)
component up_counter_load is
port (
	  cout   :out std_logic_vector (7 downto 0);  -- Output of the counter
    data   :in  std_logic_vector (7 downto 0);  -- Parallel load for the counter
    load   :in  std_logic;                      -- Parallel load enable
    enable :in  std_logic;                      -- Enable counting
    clk    :in  std_logic;                      -- Input clock
    reset  :in  std_logic                       -- Input reset
	);
end component;

--declaring inputs and initializing them to initialization values. 
signal data  : std_logic_vector (7 downto 0) := X"05";
signal load : std_logic := '0';
signal enable : std_logic := '0';
signal clk : std_logic := '0';
signal reset : std_logic := '0';

--declare outputs
signal cout : std_logic_vector (7 downto 0);

-- Defining the period of clock here.
constant CLK_PERIOD : time := 10 ns;

begin

-- Instantiate the design unit under test (dut)
   dut : up_counter_load port map (
   	        cout => cout,
   	        data => data,
   	        load => load,
   	        enable => enable,
   	        clk => clk,
   	        reset => reset
        );      

   -- Clock process definition (clock with 50% duty cycle is generated here).
   clk_process :process
   begin
        clk <= '0';
        wait for CLK_PERIOD/2;  --for half of clock period clk stays at '0'.
        clk <= '1';
        wait for CLK_PERIOD/2;  --for next half of clock period clk stays at '1'.
   end process;
    
  -- Stimulus process, Apply inputs here.
  stim_proc: process
  variable loaded_data_str : line;
  variable counted_data1_str : line;
  variable counted_data2_str : line;
   begin        
        wait for CLK_PERIOD*10; --wait for 10 clock cycles.
        reset <='1';            --then assert reset for 2 clock cycles.
        wait for CLK_PERIOD*2;
        reset <='0';            --then de-assert reset for 10 clock cycles.
        wait for CLK_PERIOD*10;
        load <= '1';           --then apply load for one clock cycle to load data to counter.
        wait for CLK_PERIOD;
        load <= '0';           --then pull down load and wait 5 clock cycles. 
        wait for CLK_PERIOD*5;
        --
        write(loaded_data_str,cout);
        -- assert (cout = X"05") -- assert that counter cout output equals loaded value of HEX 05 should pass.
        assert (cout = X"05") report time'image(now) & " : Expected HEX 05 cout but Current Count Value: " & loaded_data_str.all
        severity failure; -- stop the simulation here using severity of failure if cout does not match expected value.
        deallocate(loaded_data_str);
        --
        enable <= '1';         --then apply enable for 10 clock cycles.
        wait for CLK_PERIOD*10;
        enable <= '0';        --then de-assert enable to stop counting
        --
        write(counted_data1_str,cout);
        assert (cout = X"0F") report time'image(now) & " : *** ERROR ***: Expected HEX 0F cout but Current Count Value: " & counted_data1_str.all
        severity error;       -- print error here using severity of error if cout does not match expected value.
        deallocate(counted_data1_str);
        --
        wait for CLK_PERIOD*5;
        --
        enable <= '1';         -- enable counting
        wait for CLK_PERIOD*10;
        enable <= '0';         --then de-assert enable to stop counting
        --
        write(counted_data2_str,cout);
        assert (cout = X"19") report time'image(now) & " : *** FAILURE ***: Expected HEX 19 cout but Current Count Value: " & counted_data2_str.all
        severity failure;      -- stop simulation using severity of falure if cout does not match expected value.
        deallocate(counted_data2_str);
        --
        wait for CLK_PERIOD*5;
        --
        enable <= '1';
        wait for CLK_PERIOD*10;
        enable <= '0';         --then de-assert enable to stop counting
        --
        assert false report "......... VHDL TB *** up_counter_load_tb *** Simulation Complete ........."
        severity note; 
        assert false report time'image(now) & 
         " .......... Simulation End has been asserted ........... "
        severity failure;  -- stop the simulation using severity of failure 
        wait;
  end process;
  
  -- Add Monitor to observe simulation.
  monitor_proc : process (clk)
  variable c_str : line;
  begin
     if (clk = '1' and clk'event) then
       write(c_str,cout);
       assert false report time'image(now) & 
         ": Current Count Value : " & c_str.all
       severity note;
       deallocate(c_str);
     end if;
  end process monitor_proc;


end behavior;