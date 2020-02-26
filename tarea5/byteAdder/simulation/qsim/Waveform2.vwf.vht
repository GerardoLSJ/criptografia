-- Copyright (C) 2018  Intel Corporation. All rights reserved.
-- Your use of Intel Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Intel Program License 
-- Subscription Agreement, the Intel Quartus Prime License Agreement,
-- the Intel FPGA IP License Agreement, or other applicable license
-- agreement, including, without limitation, that your use is for
-- the sole purpose of programming logic devices manufactured by
-- Intel and sold by Intel or its authorized distributors.  Please
-- refer to the applicable agreement for further details.

-- *****************************************************************************
-- This file contains a Vhdl test bench with test vectors .The test vectors     
-- are exported from a vector file in the Quartus Waveform Editor and apply to  
-- the top level entity of the current Quartus project .The user can use this   
-- testbench to simulate his design using a third-party simulation tool .       
-- *****************************************************************************
-- Generated on "02/25/2020 22:52:04"
                                                             
-- Vhdl Test Bench(with test vectors) for design  :          byteAdder
-- 
-- Simulation tool : 3rd Party
-- 

LIBRARY ieee;                                               
USE ieee.std_logic_1164.all;                                

ENTITY byteAdder_vhd_vec_tst IS
END byteAdder_vhd_vec_tst;
ARCHITECTURE byteAdder_arch OF byteAdder_vhd_vec_tst IS
-- constants                                                 
-- signals                                                   
SIGNAL A0 : STD_LOGIC;
SIGNAL A1 : STD_LOGIC;
SIGNAL A2 : STD_LOGIC;
SIGNAL A3 : STD_LOGIC;
SIGNAL A4 : STD_LOGIC;
SIGNAL A5 : STD_LOGIC;
SIGNAL A6 : STD_LOGIC;
SIGNAL A7 : STD_LOGIC;
SIGNAL Cout : STD_LOGIC;
SIGNAL finalOutput : STD_LOGIC_VECTOR(7 DOWNTO 0);
COMPONENT byteAdder
	PORT (
	A0 : IN STD_LOGIC;
	A1 : IN STD_LOGIC;
	A2 : IN STD_LOGIC;
	A3 : IN STD_LOGIC;
	A4 : IN STD_LOGIC;
	A5 : IN STD_LOGIC;
	A6 : IN STD_LOGIC;
	A7 : IN STD_LOGIC;
	Cout : OUT STD_LOGIC;
	finalOutput : OUT STD_LOGIC_VECTOR(7 DOWNTO 0)
	);
END COMPONENT;
BEGIN
	i1 : byteAdder
	PORT MAP (
-- list connections between master ports and signals
	A0 => A0,
	A1 => A1,
	A2 => A2,
	A3 => A3,
	A4 => A4,
	A5 => A5,
	A6 => A6,
	A7 => A7,
	Cout => Cout,
	finalOutput => finalOutput
	);

-- A7
t_prcs_A7: PROCESS
BEGIN
	A7 <= '0';
WAIT;
END PROCESS t_prcs_A7;

-- A6
t_prcs_A6: PROCESS
BEGIN
	A6 <= '0';
WAIT;
END PROCESS t_prcs_A6;

-- A5
t_prcs_A5: PROCESS
BEGIN
	A5 <= '0';
WAIT;
END PROCESS t_prcs_A5;

-- A4
t_prcs_A4: PROCESS
BEGIN
	A4 <= '1';
WAIT;
END PROCESS t_prcs_A4;

-- A3
t_prcs_A3: PROCESS
BEGIN
	A3 <= '1';
WAIT;
END PROCESS t_prcs_A3;

-- A2
t_prcs_A2: PROCESS
BEGIN
	A2 <= '0';
WAIT;
END PROCESS t_prcs_A2;

-- A1
t_prcs_A1: PROCESS
BEGIN
	A1 <= '1';
WAIT;
END PROCESS t_prcs_A1;

-- A0
t_prcs_A0: PROCESS
BEGIN
	A0 <= '0';
WAIT;
END PROCESS t_prcs_A0;
END byteAdder_arch;
