javac GradeCalculator.java
java GradeCalculator
import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("성적을 입력하세요: ");
        int score = scanner.nextInt();
        
        String grade;
        
        if (score >= 90) {
            grade = "A";
        } else if (score >= 80) {
            grade = "B";
        } else if (score >= 70) {
            grade = "C";
        } else if (score >= 60) {
            grade = "D";
        } else {
            grade = "강해져서 돌아와라";
        }
        
        System.out.println("당신의 등급은 " + grade + "입니다.");
        
        scanner.close();
    }
}