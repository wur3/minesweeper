package labs;

import java.util.Scanner;

public class MinesweeperDriver {
	public static void main(String[] args) {		
		//set up	
		Minesweeper.makeMinefield();
		Minesweeper.makeMines();

		Minesweeper.printMinefield();
		
		//user starts guessing
		Minesweeper.guess();
		Minesweeper.printMinefield();
	
	}
}
