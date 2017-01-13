package labs;
import java.util.*;
import java.math.*;

public class Minesweeper {
	private static int row, column, amount;
	private static char[][] minefield;
	private static ArrayList<int[]> answer = new ArrayList<int[]>();
	
	
	public static void makeMinefield() {
		Scanner scan = new Scanner(System.in);
		
		System.out.print("# of rows: ");
		row = scan.nextInt();
		System.out.print("# of columns: ");
		column = scan.nextInt();
		
		minefield = new char[row][column];
		for(int r = 0; r < row; r++) {
			for(int c = 0; c < column; c++) {
				minefield[r][c] = '?';
			}
		}
	}
	
	//randomly chooses coordinates to be mines
	public static void makeMines() {
		Scanner scan = new Scanner(System.in);
		
		System.out.print("# of mines: ");
		amount = scan.nextInt();
		for(int i = 0; i < amount; i++) {
			double x = Math.random() * (column + 1);
			double y = Math.random() * (row + 1);
			int[] coordinates = {row, column};
			
			//no duplicates
			if(!answer.contains(coordinates)) {
				answer.add(coordinates);
			}
		}
	}
	
	//displays minefield
	public static void printMinefield() {
		for(int r = 0; r < row; r++) {
			for(int c = 0; c < column; c++) {
				System.out.print(minefield[r][c] + " ");
			}
			System.out.println();
		}
	}
	
	//asks user to guess coordinates of a mine
	public static void guess() {
		Scanner scan = new Scanner(System.in);
		System.out.print("Guess the x coordinate: ");
		int gx = scan.nextInt();
		System.out.print("Guess the y coordinate: ");
		int gy = scan.nextInt();
		//...
	}

}
