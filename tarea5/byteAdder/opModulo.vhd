library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

entity opModulo is
	Port( S0 : in STD_LOGIC;
			S1 : in STD_LOGIC;
			S2 : in STD_LOGIC;
			S3 : in STD_LOGIC;
			S4 : in STD_LOGIC;
			S5 : in STD_LOGIC;
			S6 : in STD_LOGIC;
			S7 : in STD_LOGIC;
			finalOutput : out STD_LOGIC_VECTOR(7 downto 0));
end opModulo;

architecture Behavioral of opModulo is

	signal totalInput : std_logic_vector (7 downto 0) := S7 & S6 & S5 & S4 & S3 & S2 & S1 & S0;
	signal input : integer;
	signal modResult : integer;
	
	begin
	process (S0,S1,S2,S3,S4,S5,S6,S7)
		begin
			input <= to_integer(unsigned(totalInput));
			modResult <= input mod 27;
			finalOutput <= std_logic_vector(to_unsigned(modResult, finalOutput'LENGTH));
--			finalOutput <= totalInput;
	end process;
end Behavioral;